def hamada():
    print("Hello world!")
    print("This is other string")

hamada()

# ---------------------------------------

# for i in list:
#     print(i)
#     print("still inside for loop")

# ---------------------------------------

def sum_two_numbers(num1, num2):
    # num1 = number1
    # num2 = number2
    print("inside sum_two_numbers")
    # if num1 < 0 or num2 < 0:
    #     print(num1)
    #     print(num2)
    #     return 0
    return num1 + num2

number1 = 20
number2 = 30

sum = sum_two_numbers(number1, number2) # 50
print(sum)

number1 = 33
number2 = 44

sum = sum_two_numbers(number1, number2) # 77
print(sum)

number1 = -3
number2 = 44

sum = sum_two_numbers(number1, number2) # 0
print(sum)

number1 = "Hello from the other world!"
number2 = "ay 7aga"

sum = sum_two_numbers(number1, number2) # Error! >>> 1
print(sum)

# ---------------------------------------

x = input("enter x: ")
print(x)

print = ""

print("hello " + "Hamza!")

# ---------------------------------------

age = input("Enter your age:")

if age > 16 and age < 18:
    print("can vote with conditions...")
elif age < 16:
    print("can't vote...")
else:
    print("can vote...")
