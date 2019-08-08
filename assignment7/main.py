from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/", methods = ['POST'])
def register():
    return 'Success!'


if __name__ == "__main__":
    app.run()