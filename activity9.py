name = input("enter your name: ")
age = eval(input("Enter your age: "))

if age >=1 and age <=7:
	print("Toddler")
elif age >=8 and age <=13:
	print("Pre teen")
elif age >=14 and age <=18:
	print("Teenager")
elif age >=19 and age <=31:
	print("Early Adulthood")
elif age >=32 and age <=45:
	print("Mid Adulthood")
elif age >=46 and age <=59:
	print("Post Adulthood")
elif age >=60:
	print("Senior")
else:
	print(f"{name}, your age is invalid")
