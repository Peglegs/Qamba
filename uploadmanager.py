#Databases: uploads, popular
#Both have tables in the order of: (date text, title text, author text, link text, genre text, views integer, likes integer, dislikes integer)

import sqlite3
import csv
import os
import utils
from time import strftime, gmtime, localtime, time

genres = ["Rap", "Rock", "EDM", "Country", "Alternative", "Pop", "Classical", "Metal"]
def get_all():
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM uploads")
    out = c.fetchall()
    conn.close()
    return out
def upload_song(title,author,link,genre):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    insertion = (time(), title, author, link, genre, 0, 0, 0)
    c.execute("INSERT INTO uploads VALUES (?,?,?,?,?,?,?,?)", insertion)
    conn.commit()
    conn.close()

def special_upload(title,author,link,genre):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    insertion = (time(), title, author, link, genre, 0, 0, 0)
    c.execute("INSERT INTO popular VALUES (?,?,?,?,?,?,?,?)", insertion)
    conn.commit()
    conn.close()
def generate_link(title, author):
    os.chdir("./genres")
    os.chdir("./songs")
    if not os.path.exists(author):
        os.makedirs(author)
    os.chdir("..")
    os.chdir("..")
    return "./genres/songs/" + author + "/" + title + ".mp3"


def store_song(link, song_file):
    song_file.save(link)


def wipe_tables():
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    c.execute("DELETE FROM uploads")
    c.execute("DELETE FROM popular")
    conn.commit()
    conn.close()
    print "Done"
# Returns a dictionary with two keys
# uploads: a list of all songs in the genre in the uploads database
# popular: a list of all songs in the genre in the popular database

def get_by_genre(genre):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    ret = {}
    find =(genre,)
    ret['uploads'] = c.execute("SELECT * FROM uploads WHERE genre=?", find).fetchall()
    ret['popular'] = c.execute("SELECT * FROM popular WHERE genre=?", find).fetchall()
    conn.close()
    return ret
def get_by_artist(artist):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    ret = {}
    find =(artist,)
    ret['uploads'] = c.execute("SELECT * FROM uploads WHERE author=?", find).fetchall()
    ret['popular'] = c.execute("SELECT * FROM popular WHERE author=?", find).fetchall()
    conn.close()
    return ret

def increment_views(title, author):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    values = (title, author)
    changed = False
    try:
        c.execute("SELECT views from uploads WHERE title=? AND author=?", values)
        num =  c.fetchone()[0] + 1
        change = (num,title, author)
        c.execute("UPDATE uploads SET views = ? WHERE title=? AND author=?", change)
        changed = True
    except:
        pass
    try:
        c.execute("SELECT views from popular WHERE title=? AND author=?", values)
        num = c.fetchone()[0] + 1
        change = (num, title, author)
        c.execute("UPDATE popular SET views = ? WHERE title=? AND author=?", change)
        changed = True
    except:
        pass
    conn.commit()
    conn.close()

def increment_likes(title, author):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    values = (title, author)
    try:
        c.execute("SELECT likes from uploads WHERE title=? AND author=?", values)
        num =  c.fetchone()[0] + 1
        change = (num,title, author)
        c.execute("UPDATE uploads SET likes = ? WHERE title=? AND author=?", change)
        changed = True
    except:
        pass
    try:
        c.execute("SELECT likes from popular WHERE title=? AND author=?", values)
        num = c.fetchone()[0] + 1
        change = (num, title, author)
        c.execute("UPDATE popular SET likes = ? WHERE title=? AND author=?", change)
        changed = True
    except:
        pass
    conn.commit()
    conn.close()

def assess_uploads():
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    adding = []
    global genres
    for genre in genres:
        insertion = (genre,)
        to_add = (-1,-1,-1,-1,-1,-1,-1,-1)
        for row in c.execute("SELECT * FROM uploads WHERE genre=?", insertion):
            if to_add[6] < row[6]:
                to_add = row
            elif to_add[6] == row[6] and to_add[5] < row [5]:
                to_add = row
        if to_add[5] != -1:
            adding.append(to_add)
    c.executemany("INSERT into popular VALUES (?,?,?,?,?,?,?,?)", adding)
    c.execute("DELETE FROM uploads")
    for thing in adding:
        make_artist(thing[2])
    conn.commit()
    conn.close()
#print get_all()
#print get_by_genre("Classical")
