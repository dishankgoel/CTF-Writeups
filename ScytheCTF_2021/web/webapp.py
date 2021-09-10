from flask import redirect, Flask, render_template, request
from flask import make_response,url_for, send_from_directory

app = Flask(__name__)

STORE = {}

@app.route('/', methods=["GET", "POST"])
def index():
    global STORE
    if request.method == "POST":
        if len(STORE) > 4000:
            STORE = {}
        message = str(request.form["echo"])
        if request.args.get("save") is not None and request.content_length is not None and request.content_length < 696:
            STORE[request.args.get("save")] = message
    else:
        message = "nothing"
    return render_template("index.html", msg=message)

@app.route('/pop/<id>', methods=["GET"])
def pop(id):
    try:
        return STORE.pop(id, "nothing")
    except:
        return "nothing"
     

if __name__ == '__main__':
    app.run()
