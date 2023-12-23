string = input('Введите строку: ')

#Создаём масивы куда будем помещать повторяющиеся слова
repeat_words = []
fin_repeat_words = []

#Циклами проходимся по всем символам в строке. И если срез строки находится в строке больше 2 раз - добавляем в repeat_words
for j in range(0, len(string)):
    for i in range(j+2, len(string)):
        if string.count(string[j:i]) >= 2:
            repeat_words.append([string[j:i], string.count(string[j:i])])
    repeat_count = 0

#проверка на повторение слов
for i in repeat_words:
    if i not in fin_repeat_words:
        fin_repeat_words.append(i)
    else:
        continue

#выводим результат
print(f'В строке {string}:')

for i in fin_repeat_words:
    print(f'{i[0]} кол-во повторений: {i[1]}')
