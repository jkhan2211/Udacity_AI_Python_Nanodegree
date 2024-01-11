# Control Flow

## IF Statement

```
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
```

## IF, Elif, Else Statement

```
if season == 'spring':
    print('Plant the garden')
elif season == 'summer':
    print('Water the garden')
elif season == 'fall':
    print('harvest the garden')
elif season == 'winter':
    print('Stay indoors')
else:
    print('unrecognized season')    
```

## For Loops 

- Python has two kinds of loops - for loops and while loops. A for loop is used to "iterate", or do something repeatedly, over an iterable.

-  such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.

```
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")
```
Output: 
```
new york city
mountain view
chicago
los angeles
Done!
```

### Using the range() Function with for Loops

```
for i in range(3):
    print("Hello!")
```

Output:
```
Hello!
Hello!
Hello!
```

```
range(start=0, stop, step=1)
```
- The range() function takes three integer arguments, the first and third of which are optional:

The 'start' argument is the first number of the sequence. If unspecified, 'start' defaults to 0.
The 'stop' argument is 1 more than the last number of the sequence. This argument must be specified.
The 'step' argument is the difference between each number in the sequence. If unspecified, 'step' defaults to 1.


#### Creating and Modifying Lists
```
## Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
```

Modifying the list - a bit more involved, and requires the use of the range() function.

```
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
```


## Quiz_for_loop

### Quiz Solution: Create Usernames
```
names = ["Joey Tribianni", "Monica Geller", "Chandler Bing", "Pheobe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)
```

### Quiz Solution: Modify Usernames with range
```
usernames =  ["Joey Tribianni", "Monica Geller", "Chandler Bing", "Pheobe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")
print(usernames)
```

### Quiz Solution: Tag Counter

```
tokens = ['<greeting>', 'Hello World!', </greeting>]
count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count +=1
print(count)
```

### Quiz Solution: Create an HTML List

```
items = ['first string', 'second string']
html_str = "<ul>\n"

for item in items:
    html_str += "<li>{}</li>\n.format(item)"
html_str += "</ul>"
print(html_str)
```


## Building Dictionaries

#### Method 1: Using a for loop to create a set of counters
Let's start with a list containing the words in a series of book titles

```
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
```

Step1: Create a Dictionary 
```
word_counter = {}
```

Step2:  Iterate through each element in the list. If an element is already included in the dictionary, add 1 to its value. If not, add the element to the dictionary and set its value to 1. 
```
for word in book_title: 
    if word not in word_counter: 
        word_counter[word] = 1 
    else: 
        word_counter[word] += 1
```

Output:
```
{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}
```

##### Method 2: Using the get method

```
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
```

Step 1: Create an empty dictionary.

```
word_counter = {}
```

Step 2. Iterate through each element, get() its value in the dictionary, and add 1.

```
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
```

Step3: 
Printing word_counter shows us we get the same result as we did in method 1. 
```
{'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}
```

#### Iterating Through Dictionaries with For Loops

```
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key in cast:
    print(key)
```

Output:
```
Jerry Seinfeld
Julia Louis-Dreyfus
Jason Alexander
Michael Richards
```

```
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
```

This outputs:

```
Actor: Jerry Seinfeld    Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus    Role: Elaine Benes
Actor: Jason Alexander    Role: George Costanza
Actor: Michael Richards    Role: Cosmo Kramer
```

#### Solution: Factorials with While Loops
```
## number to find the factorial of
number = 6
## start with our product equal to one
product = 1
## track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


## print the factorial of number
print(product)
```

#### Solution: Factorials with For Loops

```
## number we'll find the factorial of
number = 6
## start with our product equal to one
product = 1

## calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

## print the factorial of number
print(product)
```
