name = 'Alex'
age = 32
city = 'Minsk'
text1 = f'Hello. My name is {name}. I am {age} years old. I am from {city}.'
print(text1)
text2 = 'Hello. My name is {}. I am {} years old. I am from {}.'.format(name, age, city)
print(text2)
text3 = "Hello. My name is %s. I am %d years old. I am from %s." % (name, age, city)
print(text3)
print("Hello. My name is %(name)s. I am %(age)d years old. I am from %(city)s." % {"name": name, "age": age, "city": city})
