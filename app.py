from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/Stem')
def Stem():
    return "hello welcome to Stem.clothing!"

if __name__ == '__main__':
    app.run(debug=True)