import re

words_1 = []
words_2 = set()
with open('slovnik.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split()
        for word in line:
            if not word.islower() and len(word) > 2:
                words_1.append(word)

pattern = r'[^а-яА-ЯёЁ]'
for word in words_1:
    if '-' in word:
        for element in word.split('-'):
            words_2.add(element)
    else:
        word = re.sub(pattern, "", word)
        words_2.add(word)

print(list(words_2))
