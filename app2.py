from flask import Flask,render_template,request,redirect, session
from pymongo import Connection
import utils
import urllib
import requests
import os
import json
import time
import sys
import base64


app=Flask(__name__)

CLIENT_ID="6d6dc214017b46be974deaa6db911002"
CLIENT_SECRET="01b6d36cb27a40b09dac489336299692"
REDIRECT_URI="http://127.0.0.1:5000/welcome"
scope = "playlist-read-private"

OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

UserToken = None

class SpotifyOauthError(Exception):
    pass


@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("hello.html")
    else:
        return redirect(get_authorize_url())


def get_authorize_url():
    """ Gets the URL to use to authorize this app"""
    payload = {'client_id': CLIENT_ID,
                'response_type': 'code',
                'redirect_uri': REDIRECT_URI}
    payload['scope'] = scope
    payload['state'] = "34fFs29kd09"
    urlparams = urllib.urlencode(payload)

    return "%s?%s" % (OAUTH_AUTHORIZE_URL, urlparams)


def get_token(AuthCode):
    payload = {'redirect_uri': REDIRECT_URI,
                'code': AuthCode,
                'grant_type': 'authorization_code'}
    payload['scope'] = scope
    payload['state'] = "34fFs29kd09"
    auth_header = base64.b64encode(CLIENT_ID + ':' + CLIENT_SECRET)
    headers = {'Authorization': 'Basic %s' % auth_header}

    
    response = requests.post(OAUTH_TOKEN_URL,data = payload, headers=headers, verify=True)
    if response.status_code is not 200:
        raise SpotifyOauthError(response.reason)
    return response.json()


@app.route("/welcome")
def welcome():
    url = request.url
    url = url.split("code=",1)
    code = url[1]
    url = code.split("&",1)
    code = url[0]
    print "\n"
    print  code
    print '\n\n\n'
    UserToken = get_token(code)
    return render_template("welcome.html", UserToken = UserToken)
  

if __name__=="__main__":
    app.secret_key="GetBetterGetButter"
    app.debug=True
    app.run();
    



