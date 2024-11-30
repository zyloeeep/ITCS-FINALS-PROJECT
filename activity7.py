gold = 0
miner = input("Hi, what is your name: ")

isGold = input("is the mineral gold? ")

if isGold == "yes":
	gold +=1
	print(f"Hi,{miner}, Your total gold is", gold)
else: 
	print("Your total gold is" ,gold )