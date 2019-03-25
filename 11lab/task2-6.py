
from flask import Flask, render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__)
#bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return 'Hello World and all the inhabitants!'

@app.route('/hey!')
def hey():
    return render_template('yes.html')

@app.route('/thing')
def thing():
    stuff = {'one': ['some things', 'some stuff', 'stuff and things'], 'two': 'more stuff', 'three': 'even more stuff'}
    return render_template('no.html', stuff=stuff)

if __name__ == '__main__':
    app.run(debug=True)

