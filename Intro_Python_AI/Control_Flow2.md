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