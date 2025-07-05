import json
from flask import Flask,Response
from flask import request
import os
import requests
from dotenv import load_dotenv

load_dotenv()
***REMOVED***os.getenv("ACCESS_TOKEN")
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
    
    if request.method == 'POST':
        try:
            response = request.get_json()
            print(json.dumps(response, indent=2), flush=True)

            
            if (
                'entry' in response and
                'changes' in response['entry'][0] and
                response['entry'][0]['changes'][0]['field'] == 'comments'
            ):
                comment_data = response['entry'][0]['changes'][0]['value']
                commenter_id = comment_data['from']['id']
                comment_text = comment_data['text'].strip().lower()

                
                keyword = "done"

                if comment_text == keyword:
                    url = "https://graph.instagram.com/v23.0/me/messages" 
                    headers = {
                        "Authorization": ***REMOVED***,
                        "Content-Type": "application/json"
                    }
                    payload = {
                        "recipient": {
                            "id": commenter_id
                        },
                        "message": {
                            "text": "Thanks for saying done 😊"
                        }
                    }

                    res = requests.post(url, headers=headers, json=payload)
                    print("DM Status:", res.status_code, res.text, flush=True)

        except Exception as e:
            print("Error:", e, flush=True)

        return "This is a POST Request, Hello Webhook!", 200
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
