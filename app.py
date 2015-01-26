from flask import Flask,render_template,request,redirect, session, jsonify
from pymongo import Connection
from utils import *
from uploadmanager import *

app=Flask(__name__)

@app.route("/")
def home():
    if "name" in session:
        return redirect("/profile")
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if "name" in session:
        return redirect("/profile")
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

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/newUser", methods=["GET", "POST"])
def newUser():
    if "name" in session:
        return redirect("/profile")
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
            return redirect("/profile")
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

@app.route("/discover")
def discover():
    if 'name' not in session:
        return redirect("/")
    return render_template("play.html")

 
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


@app.route("/test")
def test():
    views = "2"
    return render_template("test.html", views=views)
@app.route('/echo/', methods=['GET'])
def increment():
    link = "" + request.args.get("title") + request.args.get("author")
    if get_likes(session["name"]) == None or link not in get_likes(session["name"]):
        increment_likes(request.args.get("title"), request.args.get("author")) 
        ret_data = {"value":  str(int( request.args.get('views')) + 1)}
        add_like(session["name"], link)
    else:
        ret_data = {"value":  request.args.get('views')}
    print get_all()
    return jsonify(ret_data)

@app.route("/upload", methods=["GET","POST"])
def upload():
    if 'name' not in session:
        return redirect("/")
    else:
        if request.method == "GET":
            return render_template("upload.html")
        else:
            try:
                author = session["name"]
                title = request.form['title']
                song_file = request.files['file']
                link = generate_link(title, author)
                genre = request.form['genre']
                if get_space(author) > 0:
                    store_song(link, song_file)
                    
                    special_upload(title, author, link, genre)
                else:
                    store_song(link, song_file)
                    upload_song(title, author, link,genre)
                return render_template("upload_success.html")
            except:
                return render_template("upload_failure.html")

@app.route("/genres/<genre>")
def genre(genre = None):
    global genres
    if "name" not in session:
        return redirect("/")
    if genre != None and genre in genres:
        print genre
        songs = get_by_genre(genre)
        j = 1
        for song in songs["uploads"]:
            song =list(song)
            song[7]=  j
            j = j + 1
        return render_template("genres.html", genre=genre, songs=songs["uploads"])
    else:
        genre = "Genre Not Found"
        return render_template("play.html") 

@app.route("/artists")
def artists():
    if "name" not in session:
        return redirect("/")
    artistsUser = get_artists()
    artists = []
    for artist in artistsUser:
        artists.append(artist['user'])
    return render_template("artists.html", artists=artists)
    
@app.route("/artistpage")
def ArtistPage():
    if "name" not in session:
        return redirect("/")
    url = request.url
    url = url.split("?")
    artist = url[1]
    music = find_links(artist)
    if music == None:
        error = "Artist not found"
        return render_template("ArtistPage.html", error = error)
    return render_template("ArtistPage.html", artist = artist, music=music)



if __name__=="__main__":
    app.secret_key="GetBetterGetButter"
    app.debug=True
    app.run();
