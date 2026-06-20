import datetime
print ("Wlcome to Basic chat Box")
while True: 
    user=input("User:")
    if user.lower()=="hi":
        print("Bot : HEllo")
    elif user.lower()=="hello":
        print("Bot : Hiiii")
    elif user.lower()=="how are you":
        print("Bot : Im Great,what about you")
    elif user.lower()=="fine" or user.lower()== "great" or user.lower()=="good":
        print("Bot : That Awsome")
    elif user.lower()=="what is your name":
        print("Bot : My name is MINIBOT")
    elif user.lower()== "time":
        currenttime=datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot : ",currenttime)
    elif user.lower()=="date":
        currentdate=datetime.datetime.now().strftime("%d/%m/%Y")
        print("Bot : ",currentdate)
    elif user.lower()=="what is your fav language":
        print("Bot :Ofourse its Python")
    elif user.lower()=="thank you":
        print("Bot : Welcom")
    elif user.lower()=="who created you":
        print("Bot : I was created using Python")
    elif user.lower() == "help":
        print("Bot: Try these commands:")
        print("hello")
        print("time")
        print("date")
        print("what is your name")
        print("bye")
        
    elif user.lower()=="bye":
        print("Bot : GoodBye")  
        break
    else:
        print("Bot : Did'nt undertood!!!!")