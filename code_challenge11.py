
for a in range (0,3):
    for b in range (a, 4):
        print(" ", end = " ")
    for c in range (a+1):
        print("*", end = " ")
    for d in range (1, a+1):
        print("*", end = " ")
    print()

for w in range (1,5):
    for x in range (1,w+1):
        print(" ", end = " ")
    for y in range (5,w,-1):
        print ("*", end = " ")
    for z in range (4,w,-1):
        print ("*", end = " ")
    print()