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