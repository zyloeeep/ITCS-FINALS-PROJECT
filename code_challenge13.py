
for x in range(1, 6):
    for y in range(6,x,-1):
        print(" ", end=" ")
    for z in range(x,1, -1):
        print(z, end=" ")
    for a in range(1, x+1):
        print(a, end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(6 - i):
        print("  ", end="")
    for k in range(i, 0, -1):
        print(k, end=" ")
    for o in range(2, i + 1):
        print(o, end=" ")
    print()  

