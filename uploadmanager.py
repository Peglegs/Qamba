'''Databases: uploads, popular
Both have tables in the order of: (date text, title text, author text, link text, views integer, likes integer, dislikes integer)
'''
import sqlite3
import csv
import os
from time import strftime, gmtime, localtime, time
def upload_song(title,author,link):
    conn = sqlite3.connect("songs.db")
    c = conn.cursor()
    insertion = (time(), title, author, link, 0, 0, 0)
    c.execute("INSERT INTO uploads VALUES (?,?,?,?,?,?,?)", insertion)
    conn.commit()
    conn.close()
    
def generate_link(title, author):
    os.chdir("./songs")
    if not os.path.exists(author):
        os.makedirs(author)
    os.chdir("..")
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
    
