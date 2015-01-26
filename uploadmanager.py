#Databases: uploads, popular
#Both have tables in the order of: (date text, title text, author text, link text, genre text, views integer, likes integer, dislikes integer)

import sqlite3
import csv
import os
import utils
from time import strftime, gmtime, localtime, time
def upload_song(title,author,link,genre):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    insertion = (time(), title, author, link, genre, 0, 0, 0)
    c.execute("INSERT INTO uploads VALUES (?,?,?,?,?,?,?,?)", insertion)
def upload_song(title,author,link):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    insertion = (time(), title, author, link, 0, 0, 0)
    utils.add_link(author, link)
    c.execute("INSERT INTO uploads VALUES (?,?,?,?,?,?,?)", insertion)
    conn.commit()
    conn.close()
    
def generate_link(title, author):
    os.chdir("./songs")
    if not os.path.exists(author):
        os.makedirs(author)
    os.chdir("..")

    return "./songs/" + author + "/" + title
def store_song(link, song_file):
    song_file.save(link)

    return author + "/" + title

def store_song(link, song_file):
    song_file.save("./songs/" + link)

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
    ret['uploads'] = c.execute("SELECT * FROM uploads WHERE genre=?", genre)
    ret['popular'] = c.execute("SELECT * FROM popular WHERE genre=?", genre)
    return ret
