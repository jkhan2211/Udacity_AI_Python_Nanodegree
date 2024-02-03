import random

word_file = "./words.txt"
word_list = []


with open(word_file, 'r') as words:
    for line in words:
        word = line.strip().lower()
        if 3 < len(word) < 8:
            word_list.append(word)

def generate_password():
    global word_list
    select_word = random.sample(word_list, 3)
    return ''.join(select_word)
password = generate_password()

print(password)