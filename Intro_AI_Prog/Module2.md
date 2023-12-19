# Module 2: Intro to Python

Lessons
(Why Python Programming, Data Types and Operators, Control Flow ,Functions and Scripting)

Project_1 (using an Image classifier)


## Table of Contents

- [Arthimetic Operators](#arthimetic-operators)
- [Variables I](#var-1)
- [Variables 2](#var-2)
- [Assignment Operators](#assignment-operators)
- [Strings](#strings)

## Arthimetic Operators

- (+) Addition
- (-) Subtraction
- (*) Multiplication
- (/) Division
- (%) Mod (the remainder after dividing)
- (**) Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
- (//) Divides and rounds down to the nearest integer

The usual order of mathematical operations holds in Python, often referred to as 
PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

If needed, you can review the order of mathematical operations in this Wikipedia article Order of Operations.

Bitwise operators are special operators in Python that you can learn more about here if you'd like.

### Quiz Question
```
print((17 - 6))
```
Which of these lines of Python code are well formatted? How would you improve the readability of the codes that don't use good formatting? (Choose all that apply)


## Variables I
```
mv_population = 747728
```
## Variables II
```
x = 3
y = 4
z = 5
```
and 
```
x, y, z = 3, 4, 5
```
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Correct way of Variables
```
my_height = 58
my_lat = 40
my_long = 105
```
### Incorrect way of Variables
```
my Height = 58
MYLONG = 40
My_Lat = 105
```

## Assignment Operators
| Symbol | Example | Equivalent |
| --------------- | --------------- | --------------- |
| = | x = 2 | x = 2 |
| += | x += 2 | x = x + 2 |
| -= | x -= 2 | x = x - 2 |

## Strings
```
>>> my_string = 'this is a string!'
>>> my_string2 = "this is also a string!!!"
```

You can also include a \ in your string to be able to include one of these quotes:

```
>>> this_string = 'Simon\'s skateboard is in the garage.'
>>> print(this_string)
```

### Concateting String and len()
```
>>> first_word = 'Hello'
>>> second_word = 'There'
>>> print(first_word + second_word)

HelloThere

>>> print(first_word + ' ' + second_word)

Hello There

>>> print(first_word * 5)

HelloHelloHelloHelloHello

>>> print(len(first_word))

5
```
Pick a character from string
```
>>> first_word[0]

H

>>> first_word[1]

e
```

### len() function
```
print(len("ababa") / len("ab"))
2.5
```

### Quiz Questions
```
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
# Todo: calculate how long this name is
name_length = len(given_name + " " + middle_names + " " + family_name)


# Now we check to make sure that the name fits within the driving license character limit
# Uncomment the code below. You don't need to make changes to the code.

driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
```