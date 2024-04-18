from flask import Flask, request, jsonify
from flask_cors import CORS
from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from MultiPage import *
from CtrlJson import Control_Json
import requests
import Encryption

def jobs():
    index_page = IndexPage()
    index_page.reset_json_daily()

#==========================================================================================
    
app = Flask(__name__)
CORS(app)

#Index Page API ============================================================================

@app.route('/add/talmo-him')
def add_talmo_him():
    index_page = IndexPage()
    index_page.add_talmo_him()

    return "탈모 진행도가 1% 증가했습니다."

@app.route('/get/talmo-him')
def get_talmo_him_count():
    index_page = IndexPage()
    talmo_him_content = f"지환쌤 탈모 진행도 {index_page.get_talmo_him()}%"
    return talmo_him_content

@app.route('/get/talmo-title')
def get_talmo_gione_count():
    index_page = IndexPage()
    title = f"지환쌤 탈모기원 {index_page.get_talmo_gione()}일차"
    return title

#User information============================================================================================================
@app.route('/get/login_url')
def login_redirect():
    login_json_obj = Control_Json("./config/key.json")
    CLIENT_ID = login_json_obj.get_key_data()["google_oauth"]["client_id"]
    REDIRECT_URI = login_json_obj.get_key_data()["google_oauth"]["redirect_uri"]
    SCOPE = login_json_obj.get_key_data()["google_oauth"]["scope"]

    login_url = f'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}'

    return login_url

@app.route('/get/access-token')
def get_access_token():
    auth_code = request.args.get('code')
    login_json_obj = Control_Json("./config/key.json")
    CLIENT_ID = login_json_obj.get_key_data()["google_oauth"]["client_id"]
    CLIENT_SECRET = login_json_obj.get_key_data()["google_oauth"]["client_secret"]
    REDIRECT_URI = login_json_obj.get_key_data()["google_oauth"]["redirect_uri"]
    ENCRYPTION_KEY = login_json_obj.get_key_data()["encryption_key"]

    token_request = requests.post(
        'https://oauth2.googleapis.com/token',
        data={
            'code': auth_code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code'
        }
    )

    if token_request.status_code != 200:
        return None

    token_response_data = token_request.json()
    access_token = token_response_data.get('access_token')
    
    return Encryption.encrypt_data(access_token, ENCRYPTION_KEY)

@app.route('/get/user-info')
def login_check():
    access_token = request.args.get('access_token')
    if not access_token:
        return jsonify({'error': 'No access token provided'}), 400

    try:
        login_json_obj = Control_Json("./config/key.json")
        ENCRYPTION_KEY = login_json_obj.get_key_data()["encryption_key"]
        
        access_token = Encryption.decrypt_data(access_token, ENCRYPTION_KEY)
    except Exception as e:

        return jsonify({'error': 'Failed to decrypt or load encryption key', 'details': str(e)}), 500
    
    userinfo_request = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    if userinfo_request.status_code != 200:

        return jsonify({'error': 'Failed to fetch user information', 'status_code': userinfo_request.status_code}), 502

    userinfo_response_data = userinfo_request.json()
    return jsonify(userinfo_response_data), 200

# @app.route('/login-check') #참고용 코드
# def login_check():
#     auth_code = request.args.get('googletoken')
#     if not auth_code:
#         return jsonify({"error": "not token"}), 400
    
#     login_json_obj = Control_Json("./config/key.json")
#     CLIENT_ID = login_json_obj.get_key_data()["google_oauth"]["client_id"]
#     CLIENT_SECRET = login_json_obj.get_key_data()["google_oauth"]["client_secret"]
#     REDIRECT_URI = login_json_obj.get_key_data()["google_oauth"]["redirect_uri"]

#     token_request = requests.post(
#         'https://oauth2.googleapis.com/token',
#         data={
#             'code': auth_code,
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#             'redirect_uri': REDIRECT_URI,
#             'grant_type': 'authorization_code'
#         }
#     )
#     if token_request.status_code != 200:
#         return jsonify({"error": "Failed to obtain access token"}), token_request.status_code
    
#     token_response_data = token_request.json()
#     access_token = token_response_data.get('access_token')
#     if not access_token:
#         return jsonify({"error": "Access token is missing"}), 400

#     userinfo_request = requests.get(
#         'https://www.googleapis.com/oauth2/v2/userinfo',
#         headers={'Authorization': f'Bearer {access_token}'}
#     )
#     if userinfo_request.status_code != 200:
#         return jsonify({"error": "Failed to fetch user info"}), userinfo_request.status_code
    
#     userinfo_response_data = userinfo_request.json()
#     userinfo_response_data['access_token'] = Encryption.encrypt_data(access_token)
#     return jsonify(userinfo_response_data)

#Harvest Hair Page============================================================================================================
#@app.route('')
#def 


#=================================================================================================================
if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_job(jobs, trigger='cron', hour=0, minute=0)
    scheduler.start()
    app.run()
