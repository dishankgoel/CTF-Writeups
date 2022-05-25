from __future__ import annotations
import hmac
import math
import os
import secrets

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


SECRET_KEY = secrets.token_bytes(32)    # random each time we run
TUCO_ACCT_NUM = 314159265

FLAG_FILE = os.environ.get("TUPLECOIN_FLAG_FILE", "flag.txt")
try:
    with open(FLAG_FILE) as fd:
        FLAG = fd.read().strip()
except:
    FLAG = "we has a fake flag for you, but it won't get you points at the CTF..."


app = FastAPI()
APP_DIST_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "client", "dist")
app.mount("/app", StaticFiles(directory=APP_DIST_DIR), name="static")


class Balance(BaseModel):
    acct_num: int
    num_tuco: float

    def serialize(self) -> bytes:
        return (str(self.acct_num) + '|' + str(self.num_tuco)).encode()
    
    def sign(self, secret_key: bytes) -> CertifiedBalance:
        return CertifiedBalance.parse_obj({
            "balance": {
                "acct_num": self.acct_num,
                "num_tuco": self.num_tuco,
            },
            "auth_tag": hmac.new(secret_key, self.serialize(), "sha256").hexdigest(),
        })


class CertifiedBalance(BaseModel):
    balance: Balance
    auth_tag: str

    def verify(self, secret_key: bytes) -> Balance:
        recreate_auth_tag = self.balance.sign(secret_key)
        if hmac.compare_digest(self.auth_tag, recreate_auth_tag.auth_tag):
            return self.balance
        else:
            raise ValueError("invalid certified balance")


class Transaction(BaseModel):
    from_acct: int
    to_acct: int
    num_tuco: float

    def serialize(self) -> bytes:
        return (str(self.from_acct) + str(self.to_acct) + str(self.num_tuco)).encode()

    def sign(self, secret_key: bytes) -> AuthenticatedTransaction:
        tuco_smash = self.serialize()
        tuco_hash = hmac.new(secret_key, tuco_smash, "sha256").hexdigest()
        
        return CertifiedTransaction.parse_obj({
            "transaction": {
                "from_acct": self.from_acct,
                "to_acct": self.to_acct,
                "num_tuco": self.num_tuco
            },
            "auth_tag": tuco_hash,
        })


class CertifiedTransaction(BaseModel):
    transaction: Transaction
    auth_tag: str

    def verify(self, secret_key: bytes) -> Transaction:
        recreated = self.transaction.sign(secret_key)
        if hmac.compare_digest(self.auth_tag, recreated.auth_tag):
            return self.transaction
        else:
            raise ValueError("invalid authenticated transaction")


@app.get('/', include_in_schema=False)
def home():
    return RedirectResponse("app/index.html")


@app.get('/robots.txt', include_in_schema=False)
def robots():
    return RedirectResponse("app/robots.txt")

@app.post("/api/account/claim")
async def account_claim(acct_num: int) -> CertifiedBalance:
    if acct_num == TUCO_ACCT_NUM:
        raise HTTPException(status_code=400, detail="That's Tuco's account number! Don't make Tuco mad!")
    
    balance = Balance.parse_obj({
        "acct_num": acct_num,
        "num_tuco": math.pi,
    })

    return balance.sign(SECRET_KEY)


@app.post("/api/transaction/certify")
async def transaction_certify(transaction: Transaction) -> CertifiedTransaction:
    if transaction.from_acct == TUCO_ACCT_NUM:
        raise HTTPException(status_code=400, detail="Ha! You think you can steal from Tuco so easily?!!")
    return transaction.sign(SECRET_KEY)


@app.post("/api/transaction/commit")
async def transaction_commit(certified_transaction: CertifiedTransaction) -> str:
    transaction = certified_transaction.verify(SECRET_KEY)
    if transaction.from_acct != TUCO_ACCT_NUM:
        return "OK"
    else:
        return FLAG
