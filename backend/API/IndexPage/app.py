import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.append(project_root)

from flask import Flask, request, jsonify
from flask_cors import CORS
from module.MultiPage import *

app = Flask(__name__)
CORS(app)

#Index Page ==============================================================================
@app.route('/add/talmo-him')
def add_talmo_him():
    index_page = IndexPage()
    index_page.add_talmo_him()
    return "탈모 진행도가 1% 증가했습니다."

if __name__ == '__main__':
    app.run(687)