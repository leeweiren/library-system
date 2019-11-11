import datetime

def getDate():
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    now=datetime.datetime.now
    return str(now().time())

    
