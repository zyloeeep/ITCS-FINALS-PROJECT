

def zyp():
    print("Hi, IT 1A ")

def activities():
    num1 = eval(input("Please input number: "))
    num2 = eval(input("Please input another number: "))
    print(num1, "Floor divided to, ", num2, " = ", num1 // num2)

isContinue = True

while isContinue:
    print("\nSELECT FROM THE FOLLOWING CODE \nFIRST \nSECOND \nTHIRD \nEXIT ")

    ask = input("Which program would you like to run, select from the options above: ")

    if ask== "1":
        zyp()
        continue

    if ask == "2":
        activities()
        continue

    if ask== "3":
        print("TRES")
        break

    else:
        print("HI, IMYSM!!!!!!!")
        continue

