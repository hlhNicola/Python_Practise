# simple one

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)

# advanced one

num1 = input("Enter first number")
op = input("Enter operator: ")
num2 = input("Enter another number: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invald calculation")
