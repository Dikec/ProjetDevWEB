#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, Blueprint, request, flash
# ./img/photo2.jpg"
from flask import abort, request, make_response
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from data import USERS

import json 

from __init__ import create_app, db, app, Admin

db.create_all(app=create_app())

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/')
def index():
    app.logger.debug('serving root URL /')
    return render_template('Presentation.html')


@app.route('/Etudiants', methods=['GET', 'POST'])
def Etudiants():
    result = request.args
    n = result['name']
    p = result['prénom']
    g = result['group']
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

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Admin.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or password != user.password:
        flash("L'identifiant ou le mot de passe n'est pas reconnu")
        return redirect(url_for('login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user,remember=remember)
    return render_template('Presentation.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

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
