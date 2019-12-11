# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


#  Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count("а"))


# # Вывести количество гласных букв в слове
word = 'Архангельск'
print(word.count("а"))


# # Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
word=sentence.split()
print(len(word))


# # Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
letters="".join(item[0] for item in sentence.split())
print(letters)

# # Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
avr_len = sum(len(word) for word in sentence.split())/len(sentence.split())
print(avr_len)