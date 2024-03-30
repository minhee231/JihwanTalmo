from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="frontend")

@app.route('/')
def index_page():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()