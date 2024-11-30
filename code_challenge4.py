numOne = eval(input("Enter a number: "))
numTwo = eval(input("Enter a number: "))

sum = numOne + numTwo
diff = numOne - numTwo
prod = numOne * numTwo
quot = numOne / numTwo
expo = numOne ** numTwo
rem = numOne % numTwo
fDiv = numOne // numTwo

print()
print("The sum of ", numOne, "and", numTwo, "is", sum)
print("The difference of ", numOne, "and", numTwo, "is", diff)
print("The product of ", numOne, "and", numTwo, "is", prod)
print("The quotient of ", numOne, "and", numTwo, "is", quot)
print(numOne, "exponent by ", numTwo, "is", expo)
print("The remainder of ", numOne, "and", numTwo, "is", rem)
print("The floor division of ", numOne, "and", numTwo, "is", fDiv)
print()