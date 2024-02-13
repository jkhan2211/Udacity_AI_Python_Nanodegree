# Introduction to Object Oriented Programming

### Object-Oriented Programming (OOP) Vocabulary
class - a blueprint consisting of methods and attributes

object - an instance of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog, a blue shirt, etc. However, as you'll see later in the lesson, objects can be more abstract.

attribute - a descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, 3 inches, large, etc.

method - an action that a class or object could take

OOP - a commonly used abbreviation for object-oriented programming

encapsulation - one of the fundamental ideas behind object-oriented programming is called encapsulation: you can combine functions and data all into a single entity. In object-oriented programming, this single entity is called a class. Encapsulation allows you to hide implementation details much like how the scikit-learn package hides the implementation of machine learning algorithms.
In English, you might hear an attribute described as a property, description, feature, quality, trait, or characteristic. All of these are saying the same thing.

Here is a reminder of how a class, object, attributes and methods relate to each other.


### Example: 

Object: Stephen Hawking, Angela Merkel, Bradd Pitt

Class: scientist, chancellor, actor

Attribute: color, size, shape

Method: to ring, to rain, to open

Value: gray, large, round


#### Quiz Question

###### Consider the code from above
```
class Shirt:
  def __init__(self, shirt_color, shirt_size, shirt_size, shirt_price):
      self-color = shirt_color
      self.size = shirt_size
      self-style = shirt_style
      self.price = shirt_price
```


#### Quiz Question

###### Consider the code from above
```
class Shirt:
  def __init__(self, shirt_color, shirt_size, shirt_size, shirt_price):
      self-color = shirt_color
      self.size = shirt_size
      self-style = shirt_style
      self.price = shirt_price
```

Ans: 

```
self_color = "orange"
```


Consider the code from above
```
class Shirt:

def __init__(self, shirt_color, shirt_size, shirt_size, shirt_price):
 self-color=  shirt_color
 self.size =  shirt_size
 self-style = shirt_style
 self.price = shirt_price
What changes would you have to make to the above code add a new attribute called "material"? Note that there is more than one way to accomplish this.

Your reflection
class Shirt: def __init__(self, shirt_color, shirt_size, shirt_size, shirt_price, shirt_material): self-color= shirt_color self.size = shirt_size self-style = shirt_style self.price = shirt_price self.material = shirt_material

Things to think about
There are multiple approaches that you could take. This is one approach. You will need to add a new parameter in the header

def __init__(self, shirt_color, shirt_size, shirt_size, shirt_price, shirt_material):

and also set your variable = to the value of the parameter self.material = shirt_material

It should look like this when you are done,


class Shirt:


def init(self, shirt_color, shirt_size, shirt_size, shirt_price, shirt_material):
    self-color= shirt_color
    self.size = shirt_size
    self-style = shirt_style
    self.price = shirt_price
    self.material = shirt_material
```


Quiz Question

Imagine we added a new variable to the Short class called "material." Which of the following would be a get method for that attribute.

```
def get_material(self):
return self.material
```

Quiz Question

Which of the following would be a set method for an attribute called "material" in the Shirt class

```
def change_material(self, new_material):
self.material = new.material
```



## Inheritance
### Clothing class

```
class Clothing:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

class Shirt(Clothing):
    def __init__(self, color, size, style, price, long_or_short):
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2*self.price

class Pants(Clothing):
    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)
```