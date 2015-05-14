talk = input("Hello there! Would you like to talk with me about cookies? y/n")
if talk == "y" or talk == "Y":
    awesome = input("Awesome! Do you like chocolate chip cookies? y/n")
    if awesome == "y" or awesome == "Y":
        pb = input ("Me too! What about peanut butter cookies? y/n")
        if pb == "y" or pb == "Y":
            sugar = input("Yay! How about sugar cookies? y/n")
            if sugar == "y" or sugar =="Y":
                input ("Cool! What about Snickerdoodles? y/n")
            elif sugar == "n" or sugar == "N":
                snicker = input("Bummer. What about Snickerdoodles? y/n")
                if snicker == "y" or snicker == "Y":
                    input ("Nice! It was nice talking to you! :)")
                elif snicker == "n" or snicker == "N":
                      input ("Okay. It was nice talking to you! :)")  
        elif pb == "n" or pb == "N":
            input ("Ok, what about sugar cookies?")   
    elif awesome == "n" or awesome == "N":
        input ("Aw...bummer. What about peanut butter cookies? y/n")
elif talk == "n" or talk == "N":
    okay = input("Oh, okay then...are you sure? y/n")
    if okay == "y" or okay == "Y":
        cakes = input ("Okay. Do you want to talk about cakes? y/n")
    elif okay == "n" or okay == "N":
        sure1 = input ("Are you sure? y/n")
        if sure1 == "y" or sure1 == "Y":
            input ("Fine. Be that way.")
        elif sure1 == "n" or sure1 == "N":
            input ("Oh, well I'm sorry. Were out of time.")
        if cakes == "y" or "Y":
            cc = input ("Ok! Do you like chocolate cake? y/n")
            if cc == "y" or cc == "Y":
                vanilla = input ("Nice! What about vanilla cakes? y/n")
                if vanilla == "Y" or vanilla == "y":
                    input ("Cool! Well, it was nice talking to you!")
                elif vanilla == "n" or vanilla == "N":
                    input ("Aw...well, it was nice talking to you!")
            elif cc == "n" or cc == "N":
                input ("Man...what about vanilla cakes? y/n")
        elif cakes == "n" or cakes == "N":
            sure = input ("Are you sure? y/n")
            if sure == "Y" or sure == "y":
                print ("Fine. Be that way.")
    elif okay == "n" or okay == "N":
        input("Oh! Well we can if you want to! Do you want to change your mind? y/n")
        
else:
    print("I'm sorry. I didn't hear you.")
