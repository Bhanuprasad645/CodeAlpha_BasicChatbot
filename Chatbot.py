import datetime

print("Welcome to Basic Chat Bot")

while True:
    user = input("User: ")

    if user.lower() == "hi":
        print("Bot : Hello")

    elif user.lower() == "hello":
        print("Bot : Hiiii")

    elif user.lower() == "how are you":
        print("Bot : I'm Great, what about you?")

    elif user.lower() == "fine" or user.lower() == "great" or user.lower() == "good":
        print("Bot : That's Awesome!")

    elif user.lower() == "what is your name":
        print("Bot : My name is MINIBOT")

    elif user.lower() == "time":
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot :", currenttime)

    elif user.lower() == "date":
        currentdate = datetime.datetime.now().strftime("%d/%m/%Y")
        print("Bot :", currentdate)

    elif user.lower() == "what is your fav language":
        print("Bot : Of course, it's Python!")

    elif user.lower() == "thank you":
        print("Bot : You're Welcome!")

    elif user.lower() == "who created you":
        print("Bot : I was created using Python.")

    elif user.lower() == "joke":
        print("Bot : Why do programmers prefer dark mode? Because light attracts bugs!")

    elif user.lower() == "help":
        print("Bot : Try these commands:")
        print("hello")
        print("time")
        print("date")
        print("what is your name")
        print("who created you")
        print("joke")
        print("bye")

    elif user.lower() == "bye":
        print("Bot : Goodbye!")
        break

    else:
        print("Bot : Didn't understand!!!!")