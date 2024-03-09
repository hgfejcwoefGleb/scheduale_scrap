import json

from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging
app = Flask(__name__)

#
def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    auth_url = "https://auth.hse.ru/adfs/oauth2/authorize/?client_id=35db5abd-b262-4923-9d0e-00c56140be41&redirect_uri=https://lk.hse.ru/api/adfs-auth&response_mode=form_post&response_type=code"
    driver.get(auth_url)
    title = driver.title
    return title

logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["POST"])
def main():
    logging.info(request.json)

    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.json
    if req["session"]["new"]:
        response["response"]["text"] = download_selenium()
    else:
        if req["request"]["original_utterance"].lower() in ["хорошо", "отлично"]:
            response["response"]["text"] = "Супер! Я за вас рада!"
        elif req["request"]["original_utterance"].lower() in ["плохо", "скучно"]:
            response["response"]["text"] = "Это печально... нужно было позвать меня!"

    return json.dumps(response)