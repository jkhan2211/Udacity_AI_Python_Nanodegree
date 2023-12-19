# Data Structures in Python

## Data Structures 

Data structures are containers or collections of data that organize and group data types together in different ways.

Specifically, you'll learn about:

- Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
- Operators: Membership, Identity
- Built-In Functions and Methods


### Lists
```
list_of_random_things = [1, 3.4, 'a string', True]

>>> list_of_random_things[0]
1

>>> list_of_random_things[len(list_of_random_things)] 
IndexError: list index out of range
```

However, you can retrieve the last element by reducing the index by 1. Therefore, you can do the following:
```
>>> list_of_random_things[len(list_of_random_things) - 1] 
True
```

Alternatively, you can index from the end of a list by using negative values, where -1 is the last element, -2 is the second to last element and so on.
```
>>> list_of_random_things[-1] 
True
>>> list_of_random_things[-2] 
a string
```


### Slice and Dice with Lists
When using slicing, it is important to remember that the lower index is inclusive and the upper index is exclusive.
```
>>> list_of_random_things = [1, 3.4, 'a string', True]
>>> list_of_random_things[1:2]
[3.4]
```
```
>>> list_of_random_things[:2]
[1, 3.4]
```

```
>>> list_of_random_things[1:]
[3.4, 'a string', True]
```

### Are you in or not in? 
```
>>> 'this' in 'this is a string'
True
>>> 'in' in 'this is a string'
True
>>> 'isa' in 'this is a string'
False
>>> 5 not in [1, 2, 3, 4, 6]
True
>>> 5 in [1, 2, 3, 4, 6]
False
```