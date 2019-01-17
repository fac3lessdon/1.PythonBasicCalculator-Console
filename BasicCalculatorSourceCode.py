# created by fac3lessdon
# https://github.com/fac3lessdon
# https://twitter.com/fac3lessdon

num1 = float(input("Enter a number: \n"))

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide\n")

action = int(input("Please select a action: \n"))

num2 = float(input("\nEnter a another number: \n"))

if action == 1:
    result = num1 + num2
elif action == 2:
    result = num1 - num2
elif action == 3:
    result = num1 * num2
elif action == 4:
    result = num1 / num2

print("\nResult")

result = round(result*100)/100.0
print(result)

input("\nPress Enter to exit...\n")
