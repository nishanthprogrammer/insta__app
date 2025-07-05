import json
from flask import Flask,Response
from flask import request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO USER"

@app.route("/privacy_policy")
def privacy_policy():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "privacy_policy.html")

    with open(file_path, "rb") as file:
        html = file.read()
        return Response(html, mimetype="text/html") 

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
