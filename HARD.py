
# Задача 1 HARD по желанию Напишите программу, 
# которая принимает на вход целое или дробное число
#  и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4


def console_input():
    N= float((input("Введите число: ")))
    return N


def count_nums(N):
    if N < 1:
        N+=1
    N = N * 1_000_000

    while N % 10 == 0:
        N = N / 10
    count = 0
    while N != 0:
        N = N // 10
        count += 1
    print(N)

    return count

print(count_nums(console_input()))