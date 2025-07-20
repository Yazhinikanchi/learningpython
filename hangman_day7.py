import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length= len("chosen_word")

for postion in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

display = ""
for letters in chosen_word:
    if letters == guess:
        display += letters
    else:
        display += "_"

print(display)


