#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, Blueprint, request, flash
# ./img/photo2.jpg"
from flask import abort, request, make_response
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from data import USERS,COMPANY, STUDENT

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
    if request.method=='POST':
        result = request.form
        print(result)
        dico = {}
        dico['id'] = len(STUDENT)
        dico["name"] = result['name']
        dico["prenom"] = result['prenom']
        dico["group"] = result['group'] # 3BIM ou 3BB ou ...
        dico['entretien'] = result['entretien'] # entretien : oui ou non

        with open('donnees.json', 'r') as json_file: 
            DATA = json.load(json_file)
            DATA['STUDENT'].append(dico) # python object to be appended.
        with open('donnees.json', 'w') as js:
            json.dump(DATA, js, indent=2)
        return 'Merci, votre inscription a bien été prise en compte.'
    else :
        return render_template('Etudiants.html')

@app.route('/Entreprises', methods=['GET', 'POST'])
def Entreprises():
    if request.method=='POST':
        result = request.form
        print(result)
        dico = {}
        dico['id'] = len(COMPANY)
        dico['name'] = result['name']
        dico['secteur'] = result['secteur']
        dico['effectif'] = result['effectif'] # inf250 ou sup250
        dico['entretien'] = result['entretien'] # entretien : oui ou non
        dico['forum'] = result['forum'] # forum : oui ou non
        dico['responsable'] = result['responsable'] # name of resp
        dico['mail'] = result['mail'] # adresse mail format

        with open('donnees.json', 'r') as json_file: 
            DATA = json.load(json_file)
            DATA['COMPANY'].append(dico) # python object to be appended.
        with open('donnees.json', 'w') as js:
            json.dump(DATA, js, indent=2)
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
    return redirect(url_for('profile'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

with open('donnees.json') as js:
    DATA = json.load(js)
    STUDENT = DATA.get('STUDENT')
    COMPANY = DATA.get('COMPANY')

@app.route('/admin',methods=['GET'])
@app.route('/admin/<lien>/')
@login_required
def admin(lien=None):
    etudiant=[]
    entreprise=[]
    for student in STUDENT:
        nom=student["name"]
        prenom=student["prenom"]
        nom_complet=nom+" "+prenom
        etudiant.append(nom_complet)
    for company in COMPANY:
        entreprise.append(company["name"])
    if not lien:
        return render_template('admin.html',etudiants=etudiant,entreprises=entreprise)
    for i in range(0,len(etudiant)):
        if (etudiant[i]==lien) :
            return render_template('membre.html',info=STUDENT[i],name=lien)
    for i in range(0,len(company)):
        if (entreprise[i]==lien) :
            return render_template('membre.html',info=COMPANY[i],name=lien)


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
