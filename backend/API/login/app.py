from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from CtrlJson import Control_Json
import Encryption

app = Flask(__name__)
CORS(app)

key_file_path = "./key.json"
keyfile_obj = Control_Json(key_file_path)
keyfile_obj.file_load()

@app.route('/get/login_url')
def login_redirect():
    CLIENT_ID = keyfile_obj.get_key_data()["google_oauth"]["client_id"]
    REDIRECT_URI = keyfile_obj.get_key_data()["google_oauth"]["redirect_uri"]
    SCOPE = keyfile_obj.get_key_data()["google_oauth"]["scope"]

    login_url = f'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}'

    return login_url

@app.route('/get/access-token')
def get_access_token():
    auth_code = request.args.get('code')
    CLIENT_ID = keyfile_obj.get_key_data()["google_oauth"]["client_id"]
    CLIENT_SECRET = keyfile_obj.get_key_data()["google_oauth"]["client_secret"]
    REDIRECT_URI = keyfile_obj.get_key_data()["google_oauth"]["redirect_uri"]
    ENCRYPTION_KEY = keyfile_obj.get_key_data()["encryption_key"]

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
    
    #토큰 암호화
    return Encryption.encrypt_data(access_token, ENCRYPTION_KEY)

@app.route('/get/user-info')
def login_check():
    access_token = request.args.get('access_token')
    if not access_token:
        return jsonify({'error': 'No access token provided'}), 400

    try:
        ENCRYPTION_KEY = keyfile_obj.get_key_data()["encryption_key"]
        
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

if __name__ == '__main__':
    app.run(port=429)