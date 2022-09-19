def email_validate():
    email_add=input("enter ur email address: ")
    while "@" not in email_add:
        email_add=input("your email must have '@' in it\nenter ur email address again:")
        if len(email_add)<=6:
           email_add=input("your email address is too short\nenter ur email address again:")    
        if "." not in email_add:
            email_add=input("your email must have '.' in it\nenter ur email address again:")
           
    while "." not in email_add:
        email_add=input("your email must have '.' in it\nenter ur email address again:")
        if len(email_add)<=6:
           email_add=input("your email address is too short\nenter ur email address again:")    
        if "@" not in email_add:
            email_add=input("your email must have '@' in it\nenter ur email address again:")
        else:
            print("email_add looks fine: ")
    return email_add

import re
def pwd_validate():
    while True:
        pwd=input("enter a pwd: ")
        if len(pwd)<5 or len(pwd)>16:
            print("make sure ur password must have atleast 8 letters ")
        elif re.search('[0-9]',pwd) is None:
            print("make sure ur pwd has a number: ")
        elif re.search('[A-Z]',pwd) is None:
            print("make sure ur pwd has a capital letter in it : ")
        else:
            print("ur password looks fine ")
            return pwd
        break

#import bcrypt
#def welcome():
#    print("welcome to dashboard: ")  
def gainAccess(Username=None, Password=None):
    Username=email_validate()    
    Password=pwd_validate()
    if not len(Username or Password)<=1:
        if True:
            db=open("database.txt","r")
            d=[]
            f=[]

            for i in db:
                a,b=i.split(",")
                b=b.strip()
                c=a,b
                d.append(a)
                f.append(b)
                data=dict(zip(d, f))
            try:
                if Username in data:
                    hashed=data[Username].split(',')
                    if hashed[-1]==Password:
                        print(Username)
                        print("login success ")
                        print("Hi",Username)
#                        welcome()
                    else:
                        print("user name does not exist ")
            except:
                print("password or user name does not exist ")
        else:
            print("error logging into system ")
    else:
         print("login again ")
         gainAccess()
 
         
def register(Username=None, Password1=None,Password2=None):
    Username=email_validate()    
    Password1=pwd_validate()
    Password2=input("confirm password ")
    db=open("database.txt","r")
    d=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        c=a,b
        d.append(a)
    if not len(Password1)<=8:
        db=open("database.txt","r")
        if not Username==None:
            if len(Username)<1:
                print("please provide username ")
                register()
            elif Username in d:
                print("user exists ")
            else:
                if Password1==Password2:
                    db=open("database.txt","a")
                    db.write(Username+" ,"+str(Password1)+"\n")
                    print("user created successfully ")
                    print("login to proceed ")
                else:
                    print("password doesnot match ")
                    register()
    else:
        print("password too short ")

def home(option=None):
    print("welcome !")
    option=input("Login | Register :")
    if option=="Login":
        gainAccess()
    elif option=="Register":
        register()
    else:
        print("please enter valid parameter, this is case sensiive ")
home()        
        
                
                    
    















































































































































