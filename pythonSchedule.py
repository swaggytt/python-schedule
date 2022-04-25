import schedule
import time
from dotenv import load_dotenv
import requests
import os
load_dotenv()

LINE_URL = os.getenv('LINE_URL')
LINE_TOKEN = os.getenv('LINE_TOKEN')


def main():
    lineNotify()


def lineNotify():
    headers = {
        'content-type':
        'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + LINE_TOKEN
    }
    msg = f'Test Send every 1 minute by Heroku'
    r = requests.post(LINE_URL, headers=headers, data={'message': msg})


schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
