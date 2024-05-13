import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.append(project_root)

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import requests
from backend.module.CtrlJson import Control_Json
import backend.module.Encryption as Encryption

app = Flask(__name__)
CORS(app)

key_file_path = "../config/key.json"
keyfile_obj = Control_Json(key_file_path)
keyfile_obj.file_load()
CLIENT_ID = keyfile_obj.get_key_data()["google_oauth"]["client_id"]
CLIENT_SECRET = keyfile_obj.get_key_data()["google_oauth"]["client_secret"]
REDIRECT_URI = keyfile_obj.get_key_data()["google_oauth"]["redirect_uri"]
ENCRYPTION_KEY = keyfile_obj.get_key_data()["encryption_key"]

# {
#     "email": "goominhee123@gmail.com",
#     "id": "114342647946632437838",
#     "picture": "https://lh3.googleusercontent.com/a-/ALV-UjWZnl1eo1SlQL1IkQV7CFe_3vzrytc8O4hIfHVExLgyTa2EI6MS=s96-c",
#     "verified_email": true
# }
def get_login_time():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d-%H-%M")

    return formatted_date

def create_user_data(user_info):
    file_data = {}
    file_data["user_id"] = user_info['id']
    file_data["user_email"] = user_info['email']
    file_data["user_photo"] = user_info['picture']
    file_data["login_time"] = get_login_time()

    file_data["harvest_hair_page"] = {}
    file_data["harvest_hair_page"]["owned_hair_count"] = 0
    file_data["harvest_hair_page"]["total_hair_count"] = 0
    file_data["harvest_hair_page"]["item"] = {}

    return file_data #test

def create_user_file(user_info):
    file_name = user_info['id']
    file_path = f"./{file_name}.json"
    file_obj = Control_Json(file_path)

    file_obj.set_json_data(create_user_data(user_info))
    file_obj.write_json_file()

    return file_obj.json_data

def get_user_info(access_token):
    if not access_token:
        return {'error': 'No access token provided'}, 400
    try:
        ENCRYPTION_KEY = keyfile_obj.get_key_data()["encryption_key"]
        access_token = Encryption.decrypt_data(access_token, ENCRYPTION_KEY)
    except Exception as e:
        return {'error': 'Failed to decrypt or load encryption key', 'details': str(e)}, 500
    
    userinfo_request = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    if userinfo_request.status_code != 200:
        return {'error': 'Failed to fetch user information', 'status_code': userinfo_request.status_code}, 502

    userinfo_response_data = userinfo_request.json()
    return userinfo_response_data

def file_exists(file_name):
    file_path = os.path.join(".", file_name)  # 파일이 현재 디렉토리에 있는 경우
    return os.path.exists(file_path)

@app.route('/test') ### 테스트
def test():
    info = {
    "email": "goominhee123@gmail.com",
    "id": "114342647946632437838",
    "picture": "https://lh3.googleusercontent.com/a-/ALV-UjWZnl1eo1SlQL1IkQV7CFe_3vzrytc8O4hIfHVExLgyTa2EI6MS=s96-c",
    }
    create_user_file(info)
    return "dadasd"

@app.route('/set/user-info')
def set_user_info():
    access_token = request.args.get('access_token')
    user_info = get_user_info(access_token)

    if 'error' in user_info:
        return jsonify(user_info), user_info.get('status_code', 500)
    
    if file_exists(f"./{user_info['id']}.json"):
        return "파일이 이미 존재함"

    create_user_file(user_info)
    return jsonify(user_info), 200

if __name__ == '__main__':
    app.run(port=538)