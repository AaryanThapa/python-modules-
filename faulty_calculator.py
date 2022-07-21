# input1 = int(input("Enter the first number:"))
# input2 = int(input("Enter the second number:"))

# if input1 == 45 and input2 == 3:
#     print("45 * 3 = 555")
#     print("Hence it is faulty result")
# else:
#     print(input1 * input2)
#     print(input1/input2)
#     print(input1 + input2)
#     print(input1 - input2)
operator =(input("Select the operator:"))
num1 = int(input("Select the first number:"))
num2 = int(input("Select the second number:"))


if num1 == 45 and num2 == 3 and operator == "*":
    print("Faulty result of this calculation is 555")
elif num1 == 56 and num2 == 9 and operator == "+":
    print("Faulty result of this calculation is 77")
elif num1 == 56 and num2 == 7 and operator == "/":
    print("Faulty result of this calculation is 4")
elif operator == "+" :
    sum = num1 + num2
    print("sum of two numbers is",sum)

elif operator == "-":
    subtract = num1 - num2
    print("Difference of two numbers is",subtract)
elif operator == "*":
    multiply = num1 * num2
    print("Multiplication of two number is",multiply)
elif operator == "/":
    divide = num1/num2
    print("division of two number is",divide)
