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
## Quiz: Count By
Suppose you want to count from some number `start_num` by another number `count_by` until you hit a final number `end_num`. Use `break_num` as the variable that you'll change each time through the loop.  For simplicity, assume that `end_num` is always larger than `start_num` and `count_by` is always positive. 

Before the loop, what do you want to set `break_num` equal to? How do you want to change `break_num` each time through the loop? What condition will you use to see when it's time to stop looping?

After the loop is done, what's the value of `break_num`? It is the case that `break_num` should be a number that is the first number larger than `end_num`.

```
start_num = 5 #provide some start number, replace 5 with a number you choose
end_num = 100#provide some end number that you stop when you hit, replace 100 with a number you choose
count_by = 2 #provide some number to count by, replace 2 with a number you choose 

# write a while loop that uses break_num as the ongoing number to 
# check against end_num

break_num = start_num 
while break_num < end_num:
    print("Current break_num:", break_num)
    break_num += count_by
    
print("The value of break_num after the loop is:", break_num)
```

## Quiz: Count By Check

```
start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)
```

### Solution: Nearest Square

```
limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
```


### For Loops vs While Loops

`for` loops are ideal when the number of iterations is known or finite

Examples:
- When you have iterable collection(list, string, set, tuple, dictionary)
- When you want to iterate through a loop for a definite number of times, using range()

`while` loops are ideal when the iterations need to continue until a condition is met
Examples:
- When you want to use comparasion operators
- When you want to loop based on recieving specefic user input

## Quiz: 
Question: You need to write a loop that takes the numbers in a given ```
list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
```

Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.


Our solution:
We would write a while loop to write this code for the following reasons:

We don't need a break statement that a for loop will require. Without a break statement, a for loop will iterate through the whole list, which is not efficient.
We don't want to iterate over the entire list, but only over the required number of elements in the list that meets our condition.
It is easier to understand because you explicitly control the exit conditions for the loop.
Here's the code we wrote:

```
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))



## Quiz:
Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, which can be used in both for and while loops.

break terminates a loop
continue skips one iteration of a loo