
from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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

app = Flask(__name__)


@app.route('/', methods=['POST'])
def respond():
    data = request.json
    command = data.get('request', {}).get('command', '')

    end_session = False

    if 'выход' in command:
        response_text = 'До свидания!'
        end_session = True
    elif command:
        response_text = f'Вы сказали {command, download_selenium()}'
    else:
        response_text = 'Привет! Вы ничего не сказали.'

    response = {
        'response': {
            'text': response_text,
            'end_session ': end_session
        },
        'version': '1.0'
    }
    return response


app.run(host='0.0.0.0', port=5000, debug=True)
