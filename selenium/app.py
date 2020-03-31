from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from twitter import Twitter, OAuth
import json
from io import BytesIO
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    options = Options()
    options.add_argument('--headless')
    with webdriver.Chrome(options=options) as d:
        d.get('https://rank448.kirimasyaro.com')
        x = d.execute_script('return document.body.scrollWidth')
        y = d.execute_script('return document.body.scrollHeight')
        d.set_window_size(x, y + 100)
        d.save_screenshot('out.png')
    return send_file('out.png', mimetype='image/png')    

@app.route("/l")
def home_l():
    options = Options()
    options.add_argument('--headless')
    with webdriver.Chrome(options=options) as d:
        d.get('http://192.168.0.2:8088')
        x = d.execute_script('return document.body.scrollWidth')
        y = d.execute_script('return document.body.scrollHeight')
        d.set_window_size(x, y + 100)
        d.save_screenshot('out.png')
    return send_file('out.png', mimetype='image/png')   


@app.route("/tweet")
def tweet_img():
    path = 'downloads/out.png'
    options = Options()
    options.add_argument('--headless')
    with webdriver.Chrome(options=options) as d:
        d.get('https://rank448.kirimasyaro.com')
        x = d.execute_script('return document.body.scrollWidth') # 550
        y = d.execute_script('return document.body.scrollHeight')
        d.set_window_size(x, y + 50)
        d.save_screenshot(path)
    t, tm = auth()
    with open(path, 'rb') as f:
        mediaid = tm.media.upload(media=f.read())['media_id']
    today = str(datetime.now())[:10]
    t.statuses.update(status=f'{today} ', media_ids=mediaid)
    return 'done\n'

def auth():
    auth = OAuth(*json.load(open('var/config.json', 'r')))
    return Twitter(auth=auth), Twitter(auth=auth, domain='upload.twitter.com')

if __name__ == '__main__':
    app.run(debug=True)