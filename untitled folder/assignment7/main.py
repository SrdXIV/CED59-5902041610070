from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

class LoginForm(FlaskForm):
    name = StringField('Name :', validators=[InputRequired()])
    username = StringField('Username :', validators=[InputRequired()])
    email = StringField('Email :', validators=[InputRequired()])
    password = StringField('Password :', validators=[InputRequired()])


@app.route('/', methods = ['GET','POST' ])
def index():
    form = LoginForm()
    return render_template("index.html", form=form)




if __name__ == "__main__":
    app.run()