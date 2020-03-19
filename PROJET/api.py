# coding: utf-8

from flask import request, abort, current_app
from flask import Blueprint, jsonify

from data import USERS

SITE_API = Blueprint('api', __name__,)


@SITE_API.route('/api')
@SITE_API.route('/api/users/<string:node0>', methods=['GET', 'POST'])
#Remplacer username par node0
def api(node0=None):
    names=[]
    for user in USERS :
         names.append(user["name"])
    if not node0:
            return jsonify(names)
    for i in range(0,len(names)):
        if (names[i]==node0) :
            return jsonify(USERS[i])

    current_app.logger.debug('Looking at "{}" resource'.format(node0))
    abort(501)
# VIM MODLINE
# vim: ai ts=4 sw=4 sts=4 expandtab fileencoding=utf8
