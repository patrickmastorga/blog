import os
import sys
import requests

api_key = os.environ.get("BUTTONDOWN_API_KEY")
commit_message = os.environ.get("COMMIT_MESSAGE", "")

# Read the email content from your repository
# with open("docs/newsletter.md", "r") as f:
#     body = f.read()

url = "https://api.buttondown.com/v1/emails"
headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json",
    "X-Buttondown-Live-Dangerously": "true" # Confirms you want to send instantly
}
data = {
    "subject": "test api",
    "body": "Hello, World!",
    "status": "about_to_send" 
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Newsletter successfully queued for sending!")
else:
    print(f"Failed to send: {response.text}")
    sys.exit(1)