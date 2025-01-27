from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)