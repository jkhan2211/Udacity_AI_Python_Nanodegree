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