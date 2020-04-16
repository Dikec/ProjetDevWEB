#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, Blueprint
from flask import abort, request, make_response
from flask import render_template, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import login_required, current_user

from data import USERS
# Set API dev in an another file
from api import SITE_API

import json 
HELLO_STRINGS = {
        "cn": "你好世界\n",
        "du": "Hallo wereld\n",
        "en": "Hello world\n",
        "fr": "Bonjour monde\n",
        "de": "Hallo Welt\n",
        "gr": "γειά σου κόσμος\n",
        "it": "Ciao mondo\n",
        "jp": "こんにちは世界\n",
        "kr": "여보세요 세계\n",
        "pt": "Olá mundo\n",
        "ru": "Здравствуй, мир\n",
        "sp": "Hola mundo\n"
}

app = Flask(__name__)
# Add the API
app.register_blueprint(SITE_API)

#from __init__ import db

@app.route('/hello_world')
def hello_world():
    app.logger.debug('Hello world')
    resp=make_response('Hello world\n')
    #Set extra reponse headers
    resp.headers['X-Less']='Is More'
    resp.headers['Content-Type']='text/plain;charset=utf-8'
    #If accept language is send by the client
    if ('Accept-Language') in request.headers:
        if request.headers['Accept-language'][:2] in HELLO_STRINGS:
            resp.headers.add('Content-language',request.headers['Accept-language'])
            resp.data = HELLO_STRINGS.get(request.headers['Accept-language'][:2])
    return resp

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('Presentation.html')

@app.route('/flask')
def flaskintro():
    app.logger.debug('serving root URL /')
    return render_template('flask.html')


@app.route('/index')
def indexapi():
    return render_template('index.html')


@app.route('/about')
def about():
    from datetime import datetime
    today = datetime.today()
    app.logger.debug('about')
    return render_template('about.html', date=today,page_title='Je suis le nouveau titre')

@app.route('/Etudiants')
def Etudiants():
    return render_template('Etudiants.html')

@app.route('/Entreprises')
def Entreprises():
    return render_template('Entreprises.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/Presentation')
def Presentation():
    return render_template('Presentation.html')

@app.route('/Login')
def Login():
    return render_template('Login.html')

with open('data.json') as js:
    DATA = json.load(js)
    USERS = DATA.get('USERS')
    FIELDS = DATA.get('FIELDS')

@app.route('/users',methods=['POST', 'GET'])
@app.route('/users/<username>/')
def users(username=None):
    names = []
    if request.method == 'POST':
        dico = {}
        dico["name"]= request.form['name']
        dico["gender"]= request.form['gender']
        dico["birth"]= request.form['birth']
        dico["id"]= len(USERS)
        USERS.append(dico)
    for user in USERS :
        names.append(user["name"])
    if not username:
        return render_template('users.html',names=names)
    for i in range(0,len(names)):
        if (names[i]==username) :
            return render_template('member.html',info=USERS[i],name=username)
       


@app.route('/search/', methods=['GET'])
def search():
    search = request.args.get('pattern','')
    personnes=[]
    for user in USERS : 
        if search in user["name"] :
            personnes.append(user["name"])
    return render_template('users.html',names=personnes)
    users(username=personnes)



# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)

# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
