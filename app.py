from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Stem Clothing Kenya')

@app.route('/Stem')
def Stem():
    return render_template('Stem.html', pageTitle='What We Sell')

if __name__ == '__main__':
    app.run(debug=True)