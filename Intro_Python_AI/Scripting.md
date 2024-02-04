# Scripting

```
python first_script.py
```


## Scripting with Raw Input

```
# Scripting with Raw Inputs

name = input("Enter your name: ")
print("Hello there, {}".format(name.title()))
```

Prompts user, to enter

```
num = int(input("Enter a integer: "))
print("hello" * num)
```

Using Eval:

```
# We can also use eval, this function evaluates a string as a line of python
result = eval(input("Enter an expression: "))
print(result)
```


### Errors and Exceptions

Syntax errors occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

Exceptions occur when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.

## Try Statement
We can use try statements to handle exceptions. There are four clauses you can use (one more in addition to those shown in the video).

```try```: This is the only mandatory clause in a try statement. The code in this block is the first thing that Python runs in a try statement.
```except```: If Python runs into an exception while running the try block, it will jump to the except block that handles that exception.
else: If Python runs into no exceptions while running the try block, it will run the code in this block after running the try block.
finally: Before Python leaves this try statement, it will run the code in this finally block under any conditions, even if it's ending the program. E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.
Why do we need the finally clause in Python?

## Specifying Expectations
```
try:
    # some code
except ValueError:
    # some code
```

```
try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code
```

```
try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
```

## Accessing Error Messages

```
try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
```

This would print something like this:
```
ZeroDivisionError occurred: integer division or modulo by zero
```

```
try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
```


### With

```
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
```


## Solution: Practice Debugging 

```
user_list = []
list_sum = 0

for i in range(10):
	userInput = input("Enter any 2-digit number")
	
	
	try:
		user_list.append(new_user_input)
		if userInput % 2 == 0:
			list_sum += new_user_input
	
	except ValueError:
		print("Incorrect value. ")
		
print("user_list: {}".format(user_list))
print("The sum is {}".format(list_sum)) 
```



## Quiz Solution: Compute an Exponent
We found the math module function exp in the documentation to do this for us.

So here's our solution:
```
## calculate e to the power of 3 using the math module
import math

result = math.exp(3)
```

## Quiz Solution: Password Generator
At the top we used import random.

Then here is one possible version of a generate_password function, using random.choice:
```
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
```
Alternatively, you could use the random.sample function and .join method for strings:

```
def generate_password():
    return ''.join(random.sample(word_list, 3))
```