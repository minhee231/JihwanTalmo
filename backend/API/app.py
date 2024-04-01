from flask import Flask
from flask_cors import CORS
from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from CtrlJson import Control_Json

class IndexPage:
    def __init__(self):
        index_config = Control_Json("./config/index/config.json")
        self.talmo_gione_count = index_config.json_data['talmo_gione']
        self.talmo_him_count = index_config.json_data['talmo_jinhang']

talmo_gione_count = 0
talmo_him_count = 0

# def index_initialize_data():
#     global talmo_gione_count
#     global talmo_him_count

#     index_config = Control_Json("./config/index/config.json")
#     talmo_gione_count = index_config.json_data['talmo_gione']
#     talmo_him_count = index_config.json_data['talmo_jinhang']

# index_initialize_data() #한번만 실행

def index_save_data():
    global tal


def add_gione():
    global talmo_gione_count
    talmo_gione_count += 1

def jobs():
    add_gione()
    #하루에 한번 json 파일을 S3에 업로드
#================================================================================
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True #지우기

@app.route('/add/talmo-him')
def add_talmo_him():
    global talmo_him_count
    talmo_him_count += 1

    return "탈모 진행도가 1% 증가했습니다."

#================================================================================
@app.route('/get/talmo-him')
def get_talmo_him_count():
    global talmo_him_count
    talmo_him_content = f"  탈모 진행도 {talmo_him_count}%"
    return talmo_him_content

@app.route('/get/talmo-title')
def get_talmo_gione_count():
    global talmo_gione_count
    title = f"지환쌤 탈모기원 {talmo_gione_count}일차"
    return title

#================================================================
if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_job(add_gione, trigger='cron', hour=0, minute=0)
    scheduler.start()
    app.run()
