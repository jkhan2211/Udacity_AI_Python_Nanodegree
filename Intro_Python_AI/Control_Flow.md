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