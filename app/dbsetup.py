import sqlite3
import dbmanager
#API STUFF START
import http.client
import json
import urllib.parse
import requests
#API STUFF END

DB_FILE = "./app/db.db"

db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

def createTables():

    command = "DROP TABLE IF EXISTS users;"

    command += "DROP TABLE IF EXISTS favorited;"

    command += "DROP TABLE IF EXISTS listn;"
    
    command += "CREATE TABLE users(username TEXT, password TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT);"

    command += "CREATE TABLE favorited(userid INTEGER, listid TEXT, itemid INTEGER, id INTEGER PRIMARY KEY AUTOINCREMENT);"

    command += "CREATE TABLE lists(title TEXT, picture TEXT, descriptions TEXT, flairs TEXT, listid TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT);"

    c.executescript(command)
    db.commit()

for x in range (0,5):#get an image <number> amount of times
    conn = http.client.HTTPSConnection("dog.ceo")
    conn.request('GET', '/api/breeds/image/random')
    response = conn.getresponse()
    dict = json.loads(response.read())
    picture=dict['message']#get image source

    
    "https://images.dog.ceo/breeds/collie-border/n02106166_4450.jpg"
    
    title = picture[30:]
    index = title.rindex("/")
    title = title[:index]
    title = title.replace("-", " ")

    # print(title)
    # print(picture)
    
    if dbmanager.getItemInfoByPicture(picture) == None:
        dbmanager.addItem(title, picture, "description", "flair", "dogs")

dbmanager.showLists()

if __name__ == "__main__":
    createTables()