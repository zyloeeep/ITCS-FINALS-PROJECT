name = input("Enter your name: ")
stud = input("Are you a current student of DLL? [Y/N]:")

if stud.lower() == "y":
    yrlev = input("What year are you currently enrolled? \nF - Freshmen \nS - Sophomore \nJ - Junior \nR - Senior")

    if yrlev.lower() == "f":
        print(f"Hi {name}, Freshmen, Welcome to DLL!")
    elif yrlev.lower() == "s":
        print(f"Hi {name}, Sophomore, Welcome to DLL!")
    elif yrlev.lower() == "j":
        print(f"Hi {name}, Junior, Welcome to DLL!")
    elif yrlev.lower() == "j":
        print(f"Hi {name}, Senior, Welcome to DLL!")

else:
    print(f"Hi {name}, Welcome to DLL!")