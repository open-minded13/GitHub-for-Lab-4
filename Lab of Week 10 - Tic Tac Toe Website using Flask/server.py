# To run:
# source ~/.bash_profile
# flask --app server --debug run

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        nickname1 = request.form['nickname1']
        nickname2 = request.form['nickname2']
        if len(nickname1) == 0 or len(nickname2) == 0:
            error = 'Invalid Input'
            return render_template('index.html', error=error)
        else:
            return render_template('play.html', messages={"player1": nickname1, "player2": nickname2})
    else:
        return render_template('index.html', error=error)


@app.route('/play')
def play():
    return render_template('play.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')
