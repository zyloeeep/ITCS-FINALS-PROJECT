

import os

isContinue = True
nt = 0

while isContinue == True:
    ask = input("Do you like to create more triangle (yes/no): ")
    if ask.lower() == "no":
        print("Program terminated")
        break
        isContinue = False

    elif ask.lower() == "yes":
        os.system('cls')
        nt  +=1
        for x in range (1,5):
            for r in range (1, nt+1):
                for y in range (1, x+1):
                    print("*", end = " ")
                for z in range (5, x, -1):
                    print(" ", end = " ")
                print(end = " ")
            print()
        continue
    else:
        print("Invalid answer, please only answer in 'yes' or 'no'.")
        continue