

import os

isContinue = True
nt = 0

while isContinue == True:
    ask = input("Do you like to create more triangle (yes/no): ")
    if ask.lower() == "no":
        print("Program is Terminated")
        break
        isContinue = False
        
    elif ask.lower() == "yes":
        os.system('cls')
        nt += 1
        for j in range(1, 5):
            for h in range(1, nt + 1):
                for o in range(1, j + 1):
                    print("*", end = " ")
                for n in range(5, j, -1):
                    print(" ", end = " ")
                print(end=" ")
            print()
        continue
    else:
        print("Invalid answer, please only answer in 'yes' or 'no'")
        continue