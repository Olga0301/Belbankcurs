a = int(input('Введите число a = '))
b = int(input('Введите число b = '))
c = int(input('Введите число c = '))
count_pol = f'{a > 0}, {b > 0}, {c > 0}'
print('Количество положительных чисел ', count_pol.count('True'), 'Количество отрицательных чисел ', count_pol.count('False'))
