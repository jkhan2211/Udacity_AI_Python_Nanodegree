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