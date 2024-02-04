import json

word_file = "./flower_names.txt"
word_dict = {}

with open(word_file, 'r') as words:
    for line in words:
        parts = line.split(":")
        key = parts[0].strip()
        value = parts[1].strip()

        word_dict[key] = value

def user_name():
    global word_dict
    user_name = input("Enter your First[space] Last name only: ")
    first_name, last_name = user_name.split()
    initial = first_name[0].upper()
    flower_name = word_dict.get(initial, "does not match")
    print(f"Unique flower name with the first letter: {flower_name}")


user_name()

