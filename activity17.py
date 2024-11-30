
column = int(input("Enter a number of Column: "))

for r in range (1,11):
    for c in range (1, column +1):
        print(f"{r} x {c} = {r * c}", end = "\t")
    print()