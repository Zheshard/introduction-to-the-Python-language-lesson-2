# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Скоолько монет лежит на столе: '))

head = 0
tail = 0

for i in range(n):
    sideCoin = int(input('Введите 0, если "решка" и 1, если "орел": '))
    
    if sideCoin == 0:
        tail += 1
    else:
        head += 1

if tail > head:
    print(head)
else:
    print(tail)