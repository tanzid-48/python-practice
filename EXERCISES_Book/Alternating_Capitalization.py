word = input('Enter a word: ')
result = ''
for i in range(len(word)):
    if i % 2 == 0:
        result = result + word[i].lower()
    else:
        result = result + word[i].upper()
print(result)