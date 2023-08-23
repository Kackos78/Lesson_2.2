#  Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.

def console_input():
    N = None
    while N == None:
        try:
            N= int(input("Введите число: "))
            return N
        except:
            print("Введите целое, положительное число!")

def mult_two(N):
    mul = 1
    i = 1
    dic = {}
    while mul < N:
        mul = mul * 2
        dic[i] = {mul}
        i += 1
    return dic

N = console_input()
dic = mult_two(N)
print(dic)