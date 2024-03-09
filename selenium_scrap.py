from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return download_selenium()


if __name__ == "__main__":
    app.run(debug=True, port=3000) #вроде использоваться по дефолту будет 5000, мб будут проблемы