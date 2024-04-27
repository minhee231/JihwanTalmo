import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.append(project_root)

from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.module.CtrlJson import Control_Json

app = Flask(__name__)
CORS(app)

config_file_path = "../config/index/config.json"
config_obj = Control_Json(config_file_path)
config_obj.file_load()

#Index Page ==============================================================================
@app.route('/add/talmo-him')
def add_talmo_him():
    config_obj.json_data['talmo_jinhang'] += 1
    config_obj.write_json_file()
    return "탈모 진행도가 1% 증가했습니다."

@app.route('/add/talmo-gione') 
def add_talmo_him():
    #누구나 접근이 가능하니 나중에 보안설정 만들기
    config_obj.json_data['talmo_gione'] += 1
    config_obj.write_json_file()
    return "날짜가 증가했습니다."

@app.route('/get/talmo-him')
def get_talmo_him_count():
    config_obj.json_data['talmo_jinhang'] += 1
    config_obj.write_json_file()
    talmo_him_content = f"지환쌤 탈모 진행도 {config_obj.json_data['talmo_jinhang']}%"
    return talmo_him_content

@app.route('/get/talmo-title')
def get_talmo_gione_count():
    title = f"지환쌤 탈모기원 {config_obj.json_data['talmo_gione']}일차"
    return title

if __name__ == '__main__':
    app.run(port=687)