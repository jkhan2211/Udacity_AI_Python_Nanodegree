# Functions

## Defining a Function

```
def cylinder_volume(height, radius):
    pi = 3.14159
    return height  *pi*  radius ** 2
```

Function calling:

```
cylinder_volume(10, 3)
```

## Default Arguments

We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

```
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height  *pi*  radius ** 2
```

### Ways of Arguments

```
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name
```

## Quiz Function

```
# write your function here
def population_density(population, land_area):
    return population/land_area

print(population_density(42449768,977372))
```

## Quiz: Readable Timetable

```
# write your function here
def readable_timedelta(days):
    weeks = days // 7
    rem_days = days % 7
    
    return "{} week(s) and {} day(s).".format(weeks, rem_days)

print(readable_timedelta(1))
print(readable_timedelta(30))
print(readable_timedelta(70))
```

### Variable Scope

```
## This will result in an error
def some_function():
    word = "hello"
 
print(word)
```


```
## This works fine
def some_function():
    word = "hello"
 
def another_function():
    word = "goodbye"
```


```
## This works fine
word = "hello"

def some_function():
    print(word)

some_function()```
Notice that we can still access the value of the global variable `word` within this function. However, the value of a global variable can not be __modified__ inside the function. If you want to modify that variable's value inside this function, it should be passed in as an argument. You'll see more on this in the next quiz.

Scope is essential to understanding how information is passed throughout programs in Python and really any programming language.
```


Quiz Solution: Variable Scope
The code snippet on the previous page is repeated here:

```
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
```

A better way to write this:

```
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
```

### Lambda Functions

With a lambda expression, this function:

```
def multiply(x, y):
    return x * y
```

can be reduced to:

```
multiply = lambda x, y: x * y
```