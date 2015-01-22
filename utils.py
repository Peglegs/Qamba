import pymongo
from pymongo import Connection
#new authenticate in progress below:

def floop(x,u,p):
    res=x
    for r in res:
        if r['user']==(u):
            if r['pw']==(p):
                return True
    return False

def mfloop(x,u):
    res=x
    for r in res:
        if r['user']==(u):
            return True
    return False

def newAuth(uname,pword):
    if len(uname) == 0 or len(pword) ==0:
            return False
    conn=Connection()
    db=conn["mydb"]
    #floop(db.testbase.find())
    #db.testbase.drop()
    #db.testbase.insert({'user':'moo', 'pw':'oink'})
    
    return floop(db.testbase.find(),uname,pword)
    

#lazy copy and paste solutions for the win!
def authenticate(uname,pword):
    return newAuth(uname,pword)

# method for testing purposes     
def newUser(uname):
    name = ['Mark', 'Sue', 'Sally', 'Sam']
    if uname in name:
        return False
    else: 
        return True

def newUser(uname,pword):
	if len(uname) == 0 or len(pword) ==0:
		return False
	conn=Connection()
	db=conn["mydb"]
	if mfloop(db.testbase.find(),uname):
		return False
	#floop(db.testbase.find())
	#db.testbase.drop()
	db.testbase.insert({'user':uname, 'pw':pword, 'artist':False, 'links':[], 'likes':[]})
	return True

def add_link(artist,link):
    conn=Connection()
    db=conn["mydb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
            r['links'].append(link)
            return True
    return False
                
def is_artist(artist):
    conn=Connection()
    db=conn["mydb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
            return r['artist']


def add_like(user, link):
    conn=Connection()
    db=conn["mydb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == user:
            r['likes'].append(link)


def get_likes(user):
    conn=Connection()
    db=conn["mydb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == user:
            return r['likes']
    return None

def find_links(artist):
    conn=Connection()
    db=conn["mydb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
            return r['links']
    return None


#print newUser("moo","oinker")
#print authenticate("moo","oinker")


