from flask import Flask
from flask_cors import CORS
from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
import json

# class CtrlJson:
#     def __

talmo_gione_count = 2
talmo_him_count = 0

def open_data_file():
    with open("./data.json", 'r') as file:
        data = json.load(file)
    return data

#def 

def add_gione():
    global talmo_gione_count
    talmo_gione_count += 1

def add_talmo_him():
    global talmo_him_count
    talmo_him_count += 1

app = Flask(__name__)
CORS(app)

@app.route('/add/talmo-him')
def pro_talmo_him():
    add_talmo_him()
    return "탈모 진행도가 1% 증가했습니다."

@app.route('/get/talmo-him')
def get_talmo_him_count():
    global talmo_him_count
    talmo_him_content = f"지환쌤의 탈모 진행도 {talmo_him_count}%"
    return talmo_him_content

@app.route('/get/talmo-title')
def get_talmo_gione_count():
    global talmo_gione_count
    title = f"지환쌤 탈모기원 {talmo_gione_count}일차"
    return title

if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_job(add_gione, trigger='cron', hour=0, minute=0)  # 매일 자정에 실행
    scheduler.start()
    app.run()
