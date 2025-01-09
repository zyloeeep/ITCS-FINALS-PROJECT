import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_python(name):
    while True:
        clear_screen()
        print("\n────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
        print(f"\n\t\t   Hi, {name}. Welcome to Print Statement!")
        print("\n────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
        print("\nPRINT")
        print("\tThe Python print () function takes in python data such as ")
        print("\tints and strings, and prints those values to standard out.")
        print("\tTo say that standard out is 'text' here means a series of lines,")
        print("\twhere each line is a series of chars with a 'n' newline char ")
        print("\tmarking the end of each line.")

        print("\nMENU IN PRINT STATEMENT IN PYTHON: ")
        print("\n1. SIMPLE PRINTING")
        print("\n2. PYTHON STRING CONCATENATION")
        print("\n3. BACK TO MAIN MENU")
        print("\n--------------------------------------------------------------------------")

        chooseP = input("\nChoose a number from 1-3: ")

        if chooseP == "1":
            clear_screen()
            print("\n\t\t-- SIMPLE PRINTING --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nINPUT:")
            print("""\tprint("Hello, World!")""")
            print("\nOUTPUT:")
            print("\tHello, World!")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Print Statement Menu...")
        elif chooseP == "2":
            clear_screen()
            print("\n\t-- PYTHON STRING CONCATENATION --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nINPUT:")
            print("""\tone= "Hello,"
\ttwo = "User!"
\tonetwo = one + " " + two
\tprint(onetwo)""")
            print("\nOUTPUT:")
            print("\tHello, User!")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the menu...")
        elif chooseP == "3":
            clear_screen()
            input("\nPress Enter to return to the Print Statement Menu...")
            return
        else:
            print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
            print("\nInvalid input. Please select from options 1-3.")
            input("\nPress Enter to try again...")

def variables_python(name):
    while True:
        clear_screen()
        print("\n────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
        print(f"\n\t\t   Hi, {name}. Welcome to Variables in Python!")
        print("\n────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
        print("\nVARIABLES")
        print("\n\tVariables are containers for storing data values.")

        print("\nMENU IN VARIABLES IN PYTHON: ")
        print("\n1. EXAMPLE VARIABLE")
        print("\n2. BACK TO MAIN MENU")
        print("\n--------------------------------------------------------------------------")

        chooseV = input("\nChoose a number from 1-2: ")

        if chooseV == "1":
            clear_screen()
            print("\n\t\t-- EXAMPLE VARIABLE --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nINPUT:")
            print("""\tx = 5
    \ty = \"Cielo\"
    \tprint(x)
    \tprint(y)""")
            print("\nOUTPUT: ")
            print("\t5 \n\tCielo")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Python Variables Menu...")
        elif chooseV == "2":
            clear_screen()
            print("\nReturning to the Main Menu...")
            return
        else:
            print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
            print("\nInvalid input. Please select from options 1-2.")
            input("\nPress Enter to try again...")

def operators_python(name):
    while True:
        clear_screen()
        print("\n────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
        print(f"\n\t\t   Hi, {name}. Welcome to Operators in Python!")
        print("\n────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────────୨ৎ────")
        print("\nPYTHON OPERATORS")
        print("\n\tOperators are used to perform operations on variables and values.")
        

        print("\nMENU IN PYTHON OPERATORS: ")
        print("\n\n1. ARITHMETIC OPERATORS")
        print("\n2. ASSIGNMENT OPERATORS")
        print("\n3. COMPARISON OPERATORS")
        print("\n4. LOGICAL OPERATORS")
        print("\n5. BACK TO MAIN MENU")
        print("\n--------------------------------------------------------------------------")

        chooseO = input("\nChoose a number from 1-5: ")

        if chooseO == "1":
            clear_screen()
            print("\n\t-- ARITHMETIC OPERATORS --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\n\tAddition: x + y \n\tSubtraction: x - y \n\tMultiplication: x * y \n\tDivision: x / y \n\tExponentiation: x ** y \n\tModulus: x % y \n\tFloor Division: x // y")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Operators Menu...")
        elif chooseO == "2":
            clear_screen()
            print("\n\t-- ASSIGNMENT OPERATORS --") 
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\n\tx = 5 \n\tx += 3 \n\tx -= 3 \n\tx *= 3 \n\tx /= 3 \n\tx %= 3 \n\tx //= 3 \n\tx**= 3")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Operator Menu...")
        elif chooseO == "3":
            clear_screen()
            print("\n\t-- COMPARISON OPERATORS --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("\nCOMPARISON OPERATORS")
            print("""\n\tare used to compare values inside a Conditional Statements.
\n\t== EQUAL
\t!= - NOT EQUAL
\t> GREATER THAN
\t< LESS THAN
\t>= GREATER THAN or EQUAL
\t<= LESS THAN or EQUAL
""")
            print("EXAMPLE: ")
            print("""\tEnter the first number: 12
\tEnter the second number: 15

\tChecking if 12 == 15: False
\tChecking if 12 != 15: True
\tChecking if 12 > 15: False
\tChecking if 12 < 15: True
\tChecking if 12 >= 15: False
\tChecking if 12 <= 15: True""")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            input("\nPress Enter to return to the Operators Menu...")
        
        elif chooseO == "4":
            clear_screen()
            print("\n\t\t\t\t\t\t-- LOGICAL OPERATORS --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ")
            print("\nLOGICAL OPERATORS")
            print("\n\tand -->\tReturns True if both statements are true\t\t--> x = 7 || x < 5 and  x < 10")
            print("\tor  -->\tReturns True if one of the statements is true\t\t--> x = 3 || x < 5 or x < 4")
            print("\tnot -->\tReverse the result, returns False if the result is true\t--> x = 7 || not(x < 5 and x < 10)")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Operators Menu...")

        elif chooseO == "5":
            clear_screen()
            print("\nReturning to the Main Menu...")
            return
        else:
            print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
            print("Invalid input. Please select from options 1-5.")
            input("\nPress Enter to try again...")


def condition_python(name):
    while True:
        clear_screen()
        print(f"Hi, {name}. Welcome to Conditions in Python!")
        print("\nCONDITIONS")
        print("\n\tA Statement that makes the program smarter, it makes the program decide on what to do in certain condition")

        print("\nMENU IN CONDITIONS IN PYTHON: ")
        print("\n1. CONDITIONAL STATEMENT")
        print("\n2. BACK TO MAIN MENU")
        print("\n--------------------------------------------------------------------------")

        chooseC = input("\nChoose a number from 1-2: ")

        if chooseC == "1":
            clear_screen()
            print("\n\t\t\t-- CONDTIONAL STATEMENT --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ")
            print("\nCONDTIONAL STATEMENT")
            print("""\n\tIF Statement (1 Condition)
\tIF-ELSE Statement (2 Conditions)
\tIF-ELIF-ELSE Statement (3 or More Conditions)
\tNESTED Conditional Statements (Condition after a Condition)
""")
            print("\nINPUT:")
            print("""\n\tnumber = int(input("Enter a number: "))

\tif number > 0:
    \tprint(f"{ number } is a positive number.")
\telif number == 0:
    \tprint("You entered zero.")
\telse:
    \tprint(f"{ number } is a negative number.")
""")
            print("\nOUTPUT:")
            print("""\tEnter a number: -2
\t-2 is negative number""")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Conditions in Python Menu...")
            
        elif chooseC =="2":
            clear_screen()
            print("\nReturning to the Main Menu...")
            return
        else:
            print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
            print("Invalid input. Please select from options 1-3.")
            input("\nPress Enter to try again...")

def loop_python(name):
    while True:
        clear_screen()
        print(f"\nHi, {name}. Welcome to Loops in Python!")
        print("\nLOOPS")
        print("\tA loop in Python is a sequence of statements that repeats a task multiple times.")

        print("\nMENU IN LOOP: ")
        print("\n1. FOR LOOP")
        print("\n2. WHILE LOOP")
        print("\n3. NESTED LOOP")
        print("\n4. BACK TO MAIN MENU")
        print("\n--------------------------------------------------------------------------")

        chooseL = input("\nChoose a number from 1-4: ")

        if chooseL == "1":
            clear_screen()
            print("\n\t\t-- FOR LOOP --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nFOR LOOP")
            print("\tA statement that is commonly used to iterate through a collection or to execute a block of code a certain number of times")
            print("\nINPUT:")
            print("""\nfor x in range(1, 6):
    \tfor y in range(6, x, -1):
        \tprint(" ", end=" ")
    \tfor z in range(x, 1, -1):
        \tprint(z, end=" ")
    \tfor a in range(1, x + 1):
        \tprint(a, end=" ")
    \tprint()

for i in range(4, 0, -1):
    \tfor j in range(6 - i):
        \tprint("  ", end="")
    \tfor k in range(i, 0, -1):
        \tprint(k, end=" ")
    \tfor o in range(2, i + 1):
        \tprint(o, end=" ")
    \tprint()""")
            print("\nOUTPUT:")
            print("""          1 
        2 1 2 
      3 2 1 2 3 
    4 3 2 1 2 3 4 
  5 4 3 2 1 2 3 4 5 
    4 3 2 1 2 3 4 
      3 2 1 2 3 
        2 1 2 
          1 """)
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Python Loops Menu...")
        elif chooseL == "2":
            clear_screen()
            print("\n\t\t-- WHILE LOOP --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nWHILE LOOP")
            print("\n\tA statement that will repeat a block of code as long as its condition is fulfilled")
            print("\nINPUT:")
            print("""\nbzz = True
no = 0

while bzz:
    ask = input("Do you wish to create a new triangle (Y/N): ")

    if ask.lower() == "n":
        print("\n- loop terminated -")
        break
    elif ask.lower() == "y":
        os.system("cls")
        no += 1

        for x in range(1, 6):
            for r in range(1, no + 1):
                for y in range(1, x + 1):
                    print("*", end=" ")
                for z in range(6, x, -1):
                    print(" ", end=" ")
            print()
        continue

    else:
        os.system("cls")
        print("Invalid answer, please only answer 'y' or 'n'.")
        continue
""")
            print("\nOUTPUT:")
            print("""
*
* *
* * *       
* * * *     
* * * * *   
Do you wish to create a new triangle (Y/N):""")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Python Loops Menu...")
        elif chooseL == "3":
            clear_screen()
            print("\n\t\t-- NESTED LOOP --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nNESTED LOOP")
            print("\n\tA Nested Loop is a loop inside another loop.")
            print("\nINPUT:")
            print("""\n\tx = [1, 2]
\ty = [4, 5]
\tfor i in x:
    \t   for j in y:
        \tprint(i, j)""")
            print("\nOUTPUT:")
            print("""
\t1 4
\t1 5
\t2 4
\t2 5
""")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Python Loops Menu...")
        elif chooseL == "4":
            clear_screen()
            print("\nReturning to the Main Menu...")
            return
        else:
            print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
            print("Invalid input. Please select from options 1-4.")
            input("\nPress Enter to try again...")

def list_python(name):
    while True:
        clear_screen()
        print(f"\nHi, {name}. Welcome to List in Python!")
        print("\nLIST")
        print("\tList is a READ and WRITE collection of variables that may be used to sort certain data")
        print("\nMENU IN LOOP: ")
        print("\n1. TYPES OF LIST")
        print("\n2. BACK TO MAIN MENU")
        print("\n--------------------------------------------------------------------------")

        chooseList = input("\nChoose a number from 1-2: ")

        if chooseList == "1":
            clear_screen()
            print("\n\t\t\t\t-- TYPES OF LIST --")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nTypes of List: ")
            print("1. List add items by APPEND() \n\t- append() adds an item at the END of THE LIST")
            print("2. List add items by INSERT() \n\t- insert() an item at the SPECIFIED INDEX")
            print("3. Sort list items \n\t- sort() by alphabet or value depending on the datatype")
            print("4. Remove list items by REMOVE() \n\t- remove() deletes a SPECIFIC ITEM from the list")
            print("5. Clear all list items by CLEAR() \n\t- clear() empties the entire list")
            print("6. Copy a list by COPY() \n\t- copy() creates a DUPLICATE of the list")

            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("\nINPUT:")
            print("""\n\tcielo_list = []

    \tcielo_list.append('HTML')
    \tcielo_list.append('JAVA')
    \tcielo_list.insert(1, 'C#')
                  
    \tprint('Original List:', cielo_list)


    \tcielo_list.sort()
    \tprint('Sorted List:', cielo_list)


    \tcielo_list.remove('JAVA')
    \tprint('After Remove:', cielo_list)


    \tcopy_list = cielo_list.copy()
    \tprint('Copy of List:', copy_list)""")

            print("\nOUTPUT:")
            print("""\n\tOriginal List: ['HTML', 'C#', 'JAVA']
    \tSorted List: ['HTML', 'JAVA', 'C#']
    \tAfter Remove: ['HTML', 'C#']
    \tCopy of List: ['HTML', 'C#']""")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            input("\nPress Enter to return to the Python List Menu...")

        elif chooseList == "2":
            clear_screen()
            print("\nReturning to the Main Menu...")
            return
        else:
            print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
            print("Invalid input. Please select from options 1-2.")
            input("\nPress Enter to try again...")

def function_python(name):
    clear_screen()
    print(f"\nHi, {name}. Welcome to Function in Python!")
    print("\nFUNCTION")
    print("\n\tfunction are used to organize and divide specific tasks in a program that will only run when it is called.")

    print("\nMENU IN FUNCTION: ")
    print("\n1. EXAMPLE OF FUNCTION")
    print("\n2. BACK TO MAIN MENU")
    print("\n--------------------------------------------------------------------------")

    chooseF = input("\nChoose a number from 1-2: ")

    if chooseF == "1":
        clear_screen()
        print("\n\t\t\t\t-- EXAMPLE OF FUNCTION --")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("\nINPUT: ")
        print("""\tdef my_function():
    \t  print("Hello, user!")

\tmy_function()""")
        print("\nOUTPUT: ")
        print("\tHello, user!")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        input("\nPress Enter to return to the Python Function Menu...")


    elif chooseF == "2":
        clear_screen()
        print("\nReturning to the Main Menu...")
        return
    else:
        print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
        print("Invalid input. Please select from options 1-2.")
        input("\nPress Enter to try again...")

def exit_python(name):
    print(f"\nThank you, {name}, for using the program. Goodbye!")
    exit()

def main_menu(): 
    clear_screen()
    print("\n⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚")
    print("\nHello, Welcome to Python Discussion!")
    name = input("\nEnter your name: ")
    print(f"\nHi, {name}.")
    start = input("\nDo you want to start the program (yes/no)? ")
    while True:
        if start.lower() == "yes":
            print("\n⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆")
            print("\n\t\t\t<<Main Menu>>")
            print("\n\t\t1. PRINT STATEMENT IN PYTHON \n\t\t2. VARIABLES IN PYTHON \n\t\t3. PYTHON OPERATORS \n\t\t4. CONDITIONS IN PYTHON \n\t\t5. LOOPS IN PYTHON \n\t\t6. LIST IN PYTHON \n\t\t7. FUNCTIONS IN PYTHON \n\t\t8. EXIT")
            print("\n⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆꙳•❅*°⋆❆.ೃ࿔*:･*❆ ₊⋆")
            choice = input("\nChoose a number from 1-8: ")

            if choice == "1":
                print_python(name)
            elif choice == "2":
                variables_python(name)
            elif choice == "3":
                operators_python(name)
            elif choice == "4":
                condition_python(name)
            elif choice == "5":
                loop_python(name)
            elif choice == "6":
                list_python(name)
            elif choice == "7":
                function_python(name)
            elif choice == "8":
                exit_python(name)
            else:
                print("\nInvalid choice. Please select from options 1-8.")
        else:
            print("\nOkay, have a good day!")
            print("\n⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚₊⋆꙳•̩̩͙❅*̩̩͙‧͙ ‧͙*̩̩͙❆ ͙͛ ˚")
            print()
            break

main_menu()
