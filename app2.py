from flask import Flask,render_template,request,redirect, session
from pymongo import Connection
import utils
import spotipy
import sys
import spotipy.util as util


app=Flask(__name__)

SPOTIPY_CLIENT_ID='6d6dc214017b46be974deaa6db911002'
SPOTIPY_CLIENT_SECRET='01b6d36cb27a40b09dac489336299692'
SPOTIPY_REDIRECT_URI='http://127.0.0.1:5000/welcome'
scope = 'user-library-read'

@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("hello.html")
    else:
        user = request.form["username"]
        token = util.prompt_for_user_token(user, scope)
        sp = spotipy.Spotify(auth=token)
        return render_template("hello.html")




if __name__=="__main__":
    app.secret_key="GetBetterGeButter"
    app.debug=True
    app.run();
