# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
# import collections
# text = 'Hello'
# data = collections.Counter(text)
# print(data)

text = input('Ведите текст ')
dict_letters = dict.fromkeys(text,0)
for i in text:
      dict_letters[i] =dict_letters[i]+ 1
print(dict_letters)





