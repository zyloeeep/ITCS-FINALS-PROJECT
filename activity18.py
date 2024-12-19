
nt = eval(input("Enter a number of triangle(s):  "))

for r in range (1,5):
    for rr in range (1, nt+1):
        for c in range(1, r+1):
            print("*", end = " ")
        for cc in range (5, r, -1):
            print(" ",end = " ")
        print(end = " ")
    print()
