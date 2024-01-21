## Break, Continue
Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, which can be used in both for and while loops.

break terminates a loop
continue skips one iteration of a loop


Example: 

```
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# Breaks the loop if weight is greater than or equal to the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))
```


Output:

```
METHOD 1
current weight: 0
  adding bananas (15)
current weight: 15
  adding mattresses (24)
current weight: 39
  adding dog kennels (42)
current weight: 81
  adding machine (120)
current weight: 201
  breaking loop now!

Final Weight: 201
Final Items: ['bananas', 'mattresses', 'dog kennels', 'machine']

METHOD 2
current weight: 0
  adding bananas (15)
current weight: 15
  adding mattresses (24)
current weight: 39
  adding dog kennels (42)
current weight: 81
  skipping machine (120)
current weight: 81
  adding cheeses (5)

Final Weight: 86
Final Items: ['bananas', 'mattresses', 'dog kennels', 'cheeses']
```


## Break Quiz

```
# List of headlines
headlines = ["Headline1", "Headline2", "Headline3", "Headline4", "Headline5"]

# Initialize the new ticker string
new_tick = ""

# Loop through the headlines
for headline in headlines:
    # Check if adding the next headline exceeds the length limit
    if len(new_tick) + len(headline) + 1 > 140:
        # Calculate the remaining space and truncate the headline if needed
        remaining_space = 140 - len(new_tick) - 1  # -1 for the space
        new_tick += " " + headline[:remaining_space]
        break
    else:
        # Add the headline with a space (except for the first headline)
        if new_tick:
            new_tick += " "
        new_tick += headline

# Print the result
print("Ticker:", new_tick)
print("Length of ticker:", len(new_tick))

```

### Alternative Solution

```
# List of headlines
headlines = ["Headline1", "Headline2", "Headline3", "Headline4", "Headline5"]

news_ticker = ""

for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
```

### Coding Quiz

Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

For instance, 6 has four factors: 1, 2, 3, 6.

1 X 6 = 6

2 X 3 = 6

So we know 6 is not a prime number.

This practice is not graded. Using the workspace on the Coding Space page, write code to check if the numbers provided in the list check_prime are prime numbers.

If the numbers are prime, the code should print "[number] is a prime number."
If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".
Example output: 7 IS a prime number 26 is NOT a prime number, because 2 is a factor of 26

If you get stuck, check out the solution on the next page.

```
check_prime = [2, 26, 39, 51, 53, 57, 79, 85]


for num in check_prime:
    
    if num == 2:
        print("{} is a prime number".format(num))
        continue
    
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is not a prime number".format(num))
            break
        
        if i == num -1:
            print("{} is a prime number".format(num))
```

## Zip and Enumerate

### Zip
zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)].

Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

You could unpack each tuple in a for loop like this.

```
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
```

Output:

```
a: 1
b: 2
c: 3
```

#### Enumerate
enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.

```
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
```

Output:

```
0 a
1 b
2 c
3 d
4 e
```

