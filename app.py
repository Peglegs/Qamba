

from flask import Flask,request,url_for,redirect,render_template,session,flash
from pymongo import Connection
from utils import *
from uploadmanager import *
import json 

app=Flask(__name__, static_url_path='',static_folder='')



data = [
    {
    'playlist':{
        1:{
        'src': 'songs/Mark/Mark2.mp3', 
        'type': 'audio/mp3', 
        'config': {'poster': '', 'title': 'I Bet That You'}
            },
    }
    }   
]
with open("songs.json", "w") as outfile:
    json.dump(data[0], outfile, indent=4)

@app.route("/genres", methods=["GET","POST"])
def play():
    if 'name' not in session:
        return redirect("/")
    else:   
        try:
            url = request.url
            url = url.split("/genres?")
            genre = url[1]
            print genre
            songs = get_by_genre(genre)
            return render_template("play.html", genre=genre, songs=songs)
        except:
            return render_template('play.html')
        


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
            return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


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
            return redirect("/")
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
 
@app.route("/profile")
def profile():
    if 'name' not in session:
        return redirect("/")
    else:
        user = session['name']
        links = find_links(user)
        artist = is_artist(user)
        likes = get_likes(user)
        return render_template("profile.html", user=user, links=links, artist=artist, likes = likes)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect("/")



@app.route("/upload", methods=["GET","POST"])
def upload():
    if 'name' not in session:
        return redirect("/")
    else:
        if request.method == "GET":
            return render_template("upload.html")
        else:
            author = session["name"]
            title = request.form['title']
            song_file = request.files['file']
            genre = request.form['genre']
            link = generate_link(title, author)
            store_song(link, song_file)
            upload_song(title, author, link, genre)
            return render_template("upload_success.html")
            #except:
            #    return render_template("upload_failure.html")
            try:
                author = session["name"]
                title = request.form['title']
                song_file = request.files['file']
                link = generate_link(title, author)
                store_song(link, song_file)
                upload_song(title, author, link)
                sessio
                return render_template("upload_success.html")
            except:
                return render_template("upload_failure.html")


if __name__=="__main__":
    app.secret_key="GetBetterGetButter"
    app.debug=True
    app.run();
