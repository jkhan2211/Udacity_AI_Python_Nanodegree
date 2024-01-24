# Scripting with Raw Inputs

name = input("Enter your name: ")
print("Hello there, {}".format(name.title()))

num = int(input("Enter a intger: "))
print("hello" * num)

# We can also use eval, this function evaluates a string as a line of python
result = eval(input("Enter an expression: "))
print(result)