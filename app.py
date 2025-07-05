import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO USER"

@app.route("/privacy_policy")
def privacy_policy():
    with open("D:\SDE\INSTAGRAM AUTOMATION PROJECT\insta_app\privacy_policy.html","rb") as file:
        privacy_policy_html = file.read()
        return privacy_policy_html
    

@app.route("/webhook",methods=['GET','POST'])
def webhook():
    if request.method=='POST':
        try:
            print(request.get_json(),indent=2)
        except:
            pass
        return "This is a POST Request, Hello Webhook!"
    elif request.method=='GET':
        hub_mode = request.args.get("hub.mode")
        hub_challenge = request.args.get("hub.challenge")
        hub_verify_token = request.args.get("hub.verify_token")
        if hub_challenge:
            return hub_challenge
        else:
            return "This is a GET REQUEST,Hello Webhook"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
