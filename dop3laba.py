string = input('Введите строку: ')

repeat_words = []
fin_repeat_words = []

for j in range(0, len(string)):
    for i in range(j+2, len(string)):
        if string.count(string[j:i]) >= 2:
            repeat_words.append([string[j:i], string.count(string[j:i])])
    repeat_count = 0


for i in repeat_words:
    if i not in fin_repeat_words:
        fin_repeat_words.append(i)
    else:
        continue

print(f'В строке {string}:')

for i in fin_repeat_words:
    print(f'{i[0]} кол-во повторений: {i[1]}')
