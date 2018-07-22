# coding:utf-8

from flask import Flask,request


app = Flask(__name__)


@app.route('/login',methods=['POST'])
def login():
    if request.form['username'] == 'ray' and request.form['password']=='123456':
        return """<html>
    <head></head>
    <body>
        <h1>欢迎</h1>
        <p>Login success</p>
    </body>
</html>"""
    else:
        return u"登录失败"

if __name__ == '__main__':
    app.run()