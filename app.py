from flask import Flask,render_template,request,redirect, session
from pymongo import Connection
import utils

app=Flask(__name__)

def SessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

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
            error= "Did not match our records. Please try again or create a new account"
            return render_template("login.html",error=error)
        elif valid_user is True:
            SessionCounter()
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
            SessionCounter()
            session['name'] = uname
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

@app.route("/welcome/p1")
def p1():
    
    try:
        session['name']
        session['counter'] = session['counter'] + 1
        return render_template("p1.html")
    except:
        return redirect("/")
    
    
@app.route("/welcome/p2")
def p2():
    try:
        session['counter'] = session['counter'] + 1
        session['name']
        return render_template("p2.html")
    except:
        return redirect("/")


if __name__=="__main__":
    app.secret_key="GetBetterGeButter"
    app.debug=True
    app.run();
    
     
