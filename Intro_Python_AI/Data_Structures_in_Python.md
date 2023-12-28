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

### Mutability and Order

Mutability refers to whether or not we can change an object once it has been created. If an object can be changed, it is called mutable. However, if an object cannot be changed after it has been created, then the object is considered immutable.

```
>>> my_lst = [1, 2, 3, 4, 5]
>>> my_lst[0] = 'one'
>>> print(my_lst)
['one', 2, 3, 4, 5]
```

Order is about whether the position of an element in the object can be used to access the element. Both strings and lists are ordered. We can use the order to access parts of a list and string.

### Quiz
#### Quiz: List indexing
```
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# TODO: replace None with appropriate code
# Use list indexing to determine the number of days in `month`
num_days = days_in_month[len(days_in_month) -1]
num_days_alternative = days_in_month[month - 1]
print(num_days)
```

#### Quiz: Dicing
```
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']          
                 
# TODO: Replace None with appropriate code
# Modify this code so it prints the last three elements of the list
last_three_dates = eclipse_dates[7:]
last_three_dates_alternative = eclipse_dates[-3:]
print(last_three_dates)
```

### List Method

Useful Functions for List 1
- len()
- max() dependes what type of object 
- min()
- sorted()

Useful Functions for List 2
- join method
```
new_str = "/n".join(["fore", "aft", "starboard", "port"])
print(new_str)

>>> fore
>>> aft
>>> starboard
>>> port

name = "-".join(["Garcia", "O'Kelly", "Davis"])
print(name)

>>> Garcia-O'Kelly-Davis
```

append method
```
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

>>> ['a', 'b', 'c', 'd']
```

List: Quiz

Quiz1: Which of the following statements about data types and data structures are true? Select all that applies
- Data structures are containers that can include different type of data
- A list is an example of a data structure
- All generic data structures are data types 

Quiz2: Which of the following are properties of lists?
- Mutable
- Ordered

### Tuples
- data types that are immutable ordered sequence of elements

```
location = (13.4321, 103.44452)
print("latitude:", location[0])
print("longitude:", location[1])
```

```
dimensions = 20, 32, 12
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

length = 52, 30, 100
print("The dimensions are {} x {} x {}".format(length, width, height))

```

Quiz1- Tuple
Tuples - ordered, immutable 
Lists - ordered, mutable


### Sets 

- set is a data type for mutable unordered collection of unique elements. One application is a set is to quickly remove duplicates from list

```
fruits = {"apple", "bannana", "orange"}
```

Quiz Question
```
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))
```

List a has 10 elements, set b(created from list a) has 4 elements 
10 - 4 = 6

Ques 2
```
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
```
Maybe


### Dictionary and Identity Operators 

Dictionaries 
- A dictionary is a mutable data type that stores maps of unique keys to values

```
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
```

Identity Operators 
is - evaluates if both side have the same identity
is not - evaluates if both sides have different identities 



Data Structure- Quiz 
