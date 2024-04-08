from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/harvest-hair')
def harvest_hair_page():
    return render_template('harvest_hair.html')

if __name__ == '__main__':
    app.run(port=3400)