


print("Enter a number you want to add, and if you are done, type 'stop'.")
print()
bzz = True
num = 0
while bzz == True:
    numberz = input("Enter a number: ")

    if numberz.lower() == "stop":
        print("\n- loop has terminated - ")
        print(f"\nThe sum of all the numbers given is {num}")
        break
    else:
        num +=int(numberz)
        continue



