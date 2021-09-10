#!/usr/bin/env python

import sqlite3
from base64 import b64encode
import os
from sqlite3.dbapi2 import Error
from flask import Flask, render_template, redirect, url_for, request
from urllib.parse import parse_qs
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions, FirefoxOptions
import time
import os
from threading import Timer
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# opts = FirefoxOptions()
# opts.add_argument('headless')
# opts.add_argument('no-sandbox')
# options = ChromeOptions()
# options.add_argument('headless')
# options.add_argument('no-sandbox')
# admin_bot = webdriver.Chrome(chrome_options=options)
# time.sleep(20)

def touch(fname):
    try:
        os.utime(fname, None)
    except OSError:
        open(fname, 'a').close()

touch('db.sqlite3')
_conn = sqlite3.connect('db.sqlite3')
_conn.execute('create table if not exists comment (id integer primary key, name TEXT, comment TEXT)')
_conn.execute('create table if not exists reports (id integer primary key, name TEXT, comment TEXT)')
_conn.close()

def clear_comments():
    conn = sqlite3.connect('db.sqlite3')
    with conn:
        conn.execute('delete from comment')

    conn.commit()
    conn.close()

def clear_reports():
    conn = sqlite3.connect('db.sqlite3')
    with conn:
        conn.execute('delete from reports')

    conn.commit()
    conn.close()


def admin_visit():
    admin_bot.get("http://0.0.0.0:16057/reports")
    while True:
        try:
            admin_bot.switch_to_alert().accept()
        except:
            break
    time.sleep(10)

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

bot_cron = RepeatedTimer(30, admin_visit)
clear_cron = RepeatedTimer(3600, clear_comments)
clear_report_cron = RepeatedTimer(300, clear_reports)

app = Flask(__name__)
app.secret_key = "flag{<redacted>}"

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute"]
)

class Comment(object):
    def __init__(self, name, text):
        self.name = name
        self.comment = text


@app.route('/')
@limiter.exempt
def index():
    comments = []

    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    for row in c.execute('select name, comment from comment'):
        comments.append(Comment(*row))

    conn.close()
    nonce=b64encode(os.urandom(16)).decode()
    return render_template('index.html',nonce=nonce)


@app.route('/comment', methods=['POST'])
def comment():
    comment_name = request.form['name']
    comment_text = request.form['comment']

    conn = sqlite3.connect('db.sqlite3')
    with conn:
        conn.execute('insert into comment(name, comment) values (?, ?)', (comment_name, comment_text))
        newid = conn.execute('select last_insert_rowid()')
        comment_id = [id for id in newid][0][0]

    conn.commit()
    conn.close()
    return redirect('/comment/'+str(comment_id))

@app.route('/comment/<comment_id>', methods=["GET"])
@limiter.exempt
def view_comment(comment_id):
    try:
        comment_id = int(comment_id)
    except:
        return {'error': 'comment id should be an integer value'}, 400
    conn = sqlite3.connect('db.sqlite3')
    comments = []
    c = conn.cursor()
    for row in c.execute('select name, comment from comment where id='+str(comment_id)):
        comments.append(Comment(*row))
    
    if not len(comments):
        return {"error": "No comment with this id exists"}
    else:
        nonce=b64encode(os.urandom(16)).decode()
        return render_template('comment.html', comments=comments, id=comment_id ,nonce=nonce)

@app.route('/flag', methods=['GET', 'POST'])
@limiter.exempt
def flag():
    if request.remote_addr == '127.0.0.1':
        return app.secret_key
    else:
        return {"error": "The flag can only be accessed from inside the server i.e. from localhost(127.0.0.1)"}

@app.route('/report', methods=['POST'])
def report_comment():
    try:
        id = parse_qs(request.get_data().decode()).get('id')[0]
        try:
            id = int(id)
        except:
            return {'error': 'invalid id'}
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('select name, comment from comment where id='+str(id))
        comment = c.fetchone()
        c.execute('insert into reports(name, comment) values (?, ?)', comment)
        conn.commit()
        conn.close()
        return "ok"
    except:
        return "error"

@app.route('/reports', methods=['GET'])
@limiter.exempt
def reported_comments():
    if request.remote_addr != '127.0.0.1':
        return "You are not admin"
    comments = []
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    for row in c.execute('select name, comment from reports'):
        comments.append(Comment(*row))
    conn.close()
    nonce=b64encode(os.urandom(16)).decode()
    return render_template('reports.html', comments=comments,nonce=nonce)

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', 16057)
