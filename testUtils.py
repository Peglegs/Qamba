# method for testing purposes     

def authenticate(uname, pword):
    if len(uname)==0 or len(pword) == 0:
        return False
    else:
        return True

def newUser(uname,pword):
    name = ['Mark', 'Sue', 'Sally', 'Sam']
    if uname in name or  len(pword) == 0:
        return False
    else: 
        return True
