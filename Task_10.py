# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import getrandbits

def console_input():
    coll = 0
    while coll == 0:
        try:
            coll=int(input("Сколько монеток было подбросить?: "))
            return coll
        except:
            print("Пожалуйста введите положительное целое число \n")
            

def flipping_coins():
    n = console_input()
    i=1
    count_of_head = 0
    count_of_tail = 0
    while i <=n:
        coin = getrandbits(1)
        print(coin)
        if coin == 0:
            count_of_head += 1
        else:
            count_of_tail += 1
        i += 1
    if count_of_tail > count_of_head:
        return count_of_head
    else:
        return count_of_tail

print(f"Нужно перевернуть минимум {flipping_coins()} монет")