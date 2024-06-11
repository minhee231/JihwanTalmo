import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.append(project_root)

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from backend.module.CtrlJson import Control_Json

app = Flask(__name__)
CORS(app)

config_file_path = "../config/index/config.json"
s3_file_path = ""
config_obj = Control_Json(config_file_path)
config_obj.file_load()

#Index Page ==============================================================================
@app.route('/backup')
def backup():
    try:
        config_obj.upload_json(s3_file_path)
        return "Upload Success"
    except:
        return "Upload Error"
    
@app.route('/add/talmo-him')
def add_talmo_him():
    config_obj.json_data['talmo_jinhang'] += 1
    config_obj.write_json_file()
    return "탈모 진행도가 1% 증가했습니다."

@app.route('/add/talmo-gione') 
def add_talmo_gione():
    auth_key = request.args.get('auth_key')
    LAMBDA_AUTH = config_obj.get_key_data()["lambda_auth_key"]
    if auth_key == LAMBDA_AUTH:
        config_obj.json_data['talmo_gione'] += 1
        config_obj.write_json_file()
        return make_response('', 200)
    
    return make_response('', 200)

@app.route('/get/talmo-him')
def get_talmo_him_count():
    talmo_him_content = f"지환쌤 탈모 진행도 {config_obj.json_data['talmo_jinhang']}%"
    return talmo_him_content

@app.route('/get/talmo-title')
def get_talmo_gione_count():
    title = f"지환쌤 탈모기원 {config_obj.json_data['talmo_gione']}일차"
    return title

if __name__ == '__main__':
    app.run(port=687)