word = input()

new_word = ""

for i in range(len(word)):
    if i % 2 == 0:
        new_word += word[i]

print(new_word)
