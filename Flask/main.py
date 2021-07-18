
"""
Configurar variable de entorno FLASK_APP
export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development
flask run
"""
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)
todos = ['todo_01','todo_02','todo_03','todo_04']


@app.errorhandler(404)
def bar(error):
        return render_template('error.html'), 404


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }
    return render_template('hello.html', **context)