from flask import Flask,render_template,request,redirect, session
from pymongo import Connection
import utils
import urllib
import requests
import json
from spotUtil import *

app=Flask(__name__)

CLIENT_ID="6d6dc214017b46be974deaa6db911002"
CLIENT_SECRET="01b6d36cb27a40b09dac489336299692"
REDIRECT_URI="http://127.0.0.1:5000/welcome"
scope = "playlist-read-private playlist-modify-private user-read-email"

OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

UserToken = None


@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("hello.html")
    else:
        return redirect(get_authorize_url())


@app.route("/welcome")
def welcome():
    global UserToken
    if UserToken == None:
        url = request.url
        url = url.split("code=",1)
        code = url[1]
        url = code.split("&",1)
        code = url[0]
        UserToken = get_token(code)
    sec = UserToken['expires_in']
    return render_template("welcome.html", UserToken = UserToken)




if __name__=="__main__":
    app.secret_key="GetBetterGetButter"
    app.debug=True
    app.run();
    



