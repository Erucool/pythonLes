# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [2, 5, 10, 5, 2, 4, 16, 33]
b = []

for x in a:
    if x % 2 == 0:
        b.append(x / 4)
    else:
        b.append(x*2)

print(b)