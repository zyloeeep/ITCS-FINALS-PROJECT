name = input("Enter your name: ")
ask = input("Will you buy a grocery? [Yes/No]: ")

if ask.lower() == "yes":
	item = input("\nName of the item: ")
	price = float(input("\nPrice of the item: ₱"))
	age = int(input("\nHow old are you? "))
	amgiv = float(input("\nAmount Given: ₱"))

	sdisc = round(price * 0.052, 2)
	addedtax = round(price * 0.123, 2)
	discprice = round(price - sdisc, 2)
	taxPri = round(price + addedtax, 2)

	if age < 60:
		totalamm = taxPri
		amchange = float(amgiv - totalamm)

		print("\n\n==================================================================================================")
		print(f"\n\nHi {name}, you purchased {item}, with a price of ₱{price} plus 12.3% tax (₱{addedtax}) to your total purchase.")
		print(f"\nTotal: ₱{totalamm}")
		print(f"Amount Given: ₱{amgiv}")
		print(f"Change: ₱{amchange}")
		print("\nThank you for purchasing, See you again!")

	elif age >= 60:
		totalamm = discprice
		amchange = float(amgiv - totalamm)
		
		print("\n\n==================================================================================================")
		print(f"\n\nHi {name}, you purchased {item}, with a price of ₱{price} and received a 5.2% senior discount (₱{sdisc}).")
		print(f"\nTotal: ₱{totalamm}")
		print(f"Amount Given: ₱{amgiv}")
		print(f"Change: ₱{amchange}")
		print("\nThank you for purchasing, See you again!")

else:
	print("\n\n===========================================================================")
	print("\nThank you for dropping by!")
