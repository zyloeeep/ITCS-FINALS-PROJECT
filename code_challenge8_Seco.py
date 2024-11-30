prelim = eval(input("Enter your Prelim grade: "))
midterm = eval(input("Enter your Midterm grade: "))
semifinal = eval(input("Enter your Semi-final grade: "))
finalq = eval(input("Enter your Final Quiz grade: "))
quiz = eval(input("Enter your Quiz grade: "))
projgr = eval(input("Enter your Project Grade: "))


average = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (finalq * 0.15) + (quiz * 0.25) + (projgr * 0.15)

print(f"\nYour final average is {average}")

if average > 100 or average < 50:
    print("\n Invalid grade")
elif average >= 75:
    print("\nCongratulations, You passed the course!")
else:
    print("\nSorry, you failed!!!")
