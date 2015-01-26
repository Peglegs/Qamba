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
    db=conn["userdb"]
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
	db=conn["userdb"]
	if mfloop(db.testbase.find(),uname):
		return False
	#floop(db.testbase.find())
	#db.testbase.drop()
	db.testbase.insert({'user':uname, 'pw':pword, 'artist':False, 'links':[], 'likes':[], 'space':0})
	return True


def decrement_space(artist):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
                r['space'] = r['space'] - 1
    return r['space']
                
def set_space(artist,num):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
            r['space'] = num
    return r['space']
            
def get_space(artist):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
          return r['space']
                
def add_link(artist,link):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
            r['links'].append(link)
            
            return True
    return False

def make_artist(user):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == user:
            r['artist'] = True


def get_artists():
    answer = []
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['artist'] == True:
                answer.append(r)
    return answer

def is_artist(artist):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
            return r['artist']


def add_like(user, link):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == user:
            if r['likes'] == None:
                newlikes = []
            else:
                newlikes = r['likes']
            newlikes.append(link)
            #print newlikes
            db.testbase.update({"user": user}, { "$set": {"likes" : newlikes} })
            


def get_likes(user):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == user:
            #print r['likes']
            return r['likes']
    return None

def find_links(artist):
    conn=Connection()
    db=conn["userdb"]
    res = db.testbase.find()
    for r in res:
        if r['user'] == artist:
            return r['links']
    return None


#print newUser("moo","oinker")
#print authenticate("moo","oinker")


