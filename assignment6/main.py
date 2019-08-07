from flask import Flask, render_template, request, redirect, url_for
import pymysql
app = Flask(__name__)
conn = pymysql.connect('localhost','root','','memberdb')

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/insert", methods = ['POST'])
def insert():
    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        uname = request.form['uname']
        email = request.form['email']
        pword = request.form['pword']
        with conn.cursor() as cursor:
            sql = "Insert into `member` (`fname`, `lname`, `uname`, `email`, `pword`) values(%s, %s, %s, %s, %s)"
            cursor.execute(sql,(fname,lname,uname,email,pword))
            conn.commit()
        return redirect(url_for('member'))

@app.route('/member')
def member():
    cur = conn.cursor()
    cur.execute("select * from member")
    rows = cur.fetchall()
    return render_template("member.html",datas = rows)

if __name__ == "__main__":
    app.run(debug=True)