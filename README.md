# Instagram Auto-DM Bot 💬

This Flask app listens for Instagram comment webhooks and sends an automated Direct Message to the commenter — only if the comment matches a specific keyword.

---

🚀 Features

- Detects new comments using Instagram Webhook
- Sends auto-reply DMs using Messenger API
- Supports keyword filtering
- Works with Reels or Posts

---

🛠 Stack

- Python + Flask
- Instagram Graph API
- Hosted on Render
- Pipenv for environment

---

⚙ Setup

1. Clone repo
2. Install with `pipenv install`
3. Add your 'access_token' in env in deployment(in my case it is render)
4. Deploy to Render

---
⚠️ **Important Consent Note**:  
 Instagram only allows your app to send a DM if the user has **messaged your business account** first.
 So ask the user to comment the keyword and also send the same post to the business account to initiate the DM Automation
If they haven’t, the API returns:  
`"User consent is required to access user profile."`
![image](https://github.com/user-attachments/assets/ce7d3394-9c29-47db-b6d2-a6868a1d0e8f)
ref : [link]https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login/messaging-api

🧠 Author

Made by Nishanth — [GitHub](https://github.com/nishanthprogrammer)
