prelim = float(input("Enter your Prelim grade: "))
midterm = float(input("Enter your Midterm grade: "))
semifinal = float(input("Enter your Semi-final grade: "))
finalq = float(input("Enter your Final Quiz grade: "))
quiz = float(input("Enter your Quiz grade: "))
projgr = float(input("Enter your Project Grade: "))


average = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (finalq * 0.15) + (quiz * 0.25) + (projgr * 0.15)

print(f"\nYour final average is {average}")

if (prelim >= 65 and prelim <=100) and (midterm >= 65 and midterm <=100) and (semifinal >= 65 and semifinal <=100) and (finalq >= 65 and finalq <=100) and (quiz >= 65 and quiz <=100) and (projgr >= 65 and projgr <=100):
	if average >=75:
		print("\nCongratulations, You passed the course! :D ")
	else:
		print("\nSorry, you failed! :( ")


else: 
    print("\nInvalid grades!!! :/ ")
