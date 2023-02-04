print("Welcome to my amazing program!")
input("Please enter your favorite hobby")

x = y2
z = x + y
y = x2 / z


print("Welcome to my amazing program!")
# The program will lose anything the user input because it is not stored
input("Please enter your favorite hobby")

# When reading input it's best to store it in a variable. Personally, I also
# like to add a colon ':' to the end of a prompt to help signal the user that
# the program is waiting on their input.
name = input("Please enter your name:")
print(name)

# the following line reads and prints input, but is not useful because 
# the input isn't stored and can't be used anywhere else in the program.
print(input("Please enter your name:"))

# Print an arithmetic expression
print(3 * 8 - 4 / 2)

num = input("Please enter a number:")
# the following line will cause a TypeError.
print(num + 10)