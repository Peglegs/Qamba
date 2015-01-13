from flask import Flask,render_template,request,redirect, session
from pymongo import Connection
import utils

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        # post
        button = request.form["b"]
        uname  = request.form["uname"]
        pword  = request.form['pword']
        valid_user = utils.authenticate(uname,pword)
        error=None
        if button=="clear":
            return render_template("login.html")
        if button=="newUser":
            return redirect('/newUser')
        elif valid_user is False:
            error= "Invalid Username or Password. Please try again or create a new account"
            return render_template("login.html",error=error)
        elif valid_user is True:
            session['name'] = uname
            return redirect("/welcome")




@app.route("/newUser", methods=["GET", "POST"])
def newUser():
    if request.method=="GET":
        return render_template("newUser.html")
    else:
        button = request.form["create"]
        uname  = request.form["username"]
        pword  = request.form['password']
        create = utils.newUser(uname,pword)
        error=None
        if create is True:
            session['name'] = uname
            session['artist'] = False
            return render_template("welcome.html", error=error)
        else:
            error = "Sorry, the username you have selected already exists or you didn't enter a password."
            return render_template("newUser.html", error=error)

        
@app.route("/welcome")
def welcome():
    try:
        session['name']
        return render_template("welcome.html")
    except:
        return redirect("/")
 

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")


@app.route("/ArtistPage")
def ArtistPage():
    url = request.url
    url = url.split("artist=")
    artist = url[1]
    music = find_artist(artist)
    if music == None:
        error = "Artist not found"
        return render_template("ArtistPage.html", error = error)
    return render_template("ArtistPage.html", music=music)





if __name__=="__main__":
    app.secret_key="GetBetterGetButter"
    app.debug=True
    app.run();
    
     
