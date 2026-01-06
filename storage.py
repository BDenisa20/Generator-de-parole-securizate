import json
import hashlib
import base64
from datetime import datetime

def hash_password(password):
    sha=hashlib.sha256(password.encode()).digest()
    return base64.b64encode(sha).decode()

def save_analysis(result, file_path="history.json"):
    entry={
        "hash":hash_password(result["password"]),
        "entropy":result["entropy"],
        "strength":result["strength"],
        "score":result["score"],
        "date":datetime.now().isoformat()
    }
    try:
        with open(file_path,"r",encoding="utf-8") as f:
             history=json.load(f)
    except FileNotFoundError:
        history=[]

    history.append(entry)

    with open(file_path,"w",encoding="utf-8") as f:
        json.dump(history,f,indent=4)  
def load_history(file_path="history.json"):
    try:
        with open(file_path, "r",encoding="utf-8") as f:
           return json.load(f)
    except FileNotFoundError:
        return [] 