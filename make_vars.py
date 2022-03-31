import constants
'''
variants = []

for word in words.gerund:
    dic_word = {
        word: 'correct'
    }
    for i in range(len(word)):
        if word[i].islower() and word[i] in ['а', 'о', 'у', 'ы', 'э', 'я', 'ю', 'и', 'е']:
            new_word = word[:i].lower() + word[i].upper() + word[i+1:].lower()
            dic_word[new_word] = 'incorrect'
    variants.append(dic_word)

print(variants)

'''
res = {}
for pair in words.adverbs_vars:
    word = list(pair.keys())[0]
    res[word] = [0, 0]

print(res)

