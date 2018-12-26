authenticated={ "John":1234,"Lily":2349, "Rose":2018}
def authentication(func):
    print("Enter username and password")
    def login(username,password,*args,**kwargs):
        if (username in authenticated and authenticated[username]==password):
            func(*args,**kwargs)
        else:
            print("Not authenticated")
    return login

@authentication
def add(a,b):
    print(a+b)
add("Rose",2018,1700,5)


