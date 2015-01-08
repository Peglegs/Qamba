'''Databases: uploads, popular
Both have tables in the order of: (date text, title text, author text, link text, views integer, likes integer, dislikes integer)
'''
import sqlite3
import csv
from time import strftime, gmtime, localtime, time
def upload(title,author,link):
     conn = sqlite3.connect("database.db")
    c = conn.cursor()
    insertion = (time(), title, author, link, 0, 0, 0)
    c.execute("INSERT INTO uploads VALUES (?,?,?,?,?,?,?)", insertion)
    conn.commit()
    conn.close()
    
