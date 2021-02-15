
kaji=""
started=False
while kaji.lower()!="quit":
    kaji=input("enter the command ").lower()
    if kaji=="start":
        if started:
            print("your car is already started")
        else:
            started=True
        print("your car is started.....ready to go")
    elif kaji=="stop":
        if not started:
            print("your car is alreaddy stopped")
        else:
         started=False
        print("your car is stopped")
    elif kaji=="help":
        print(""" 
        start=press to start your car
        stop=press to stop your car
        quit=press to quit""")
    elif kaji=="quit":
        exit(kaji)
    else:
        print("i don't understand")