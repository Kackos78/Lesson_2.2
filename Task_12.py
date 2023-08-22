# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


# Петя загадывает числа
def Console_input():
    num1, num2 = None, None
    while num1 == None:
        try: num1 = int(input("Какое первое число?: "))            
        except: print("Пожалуйста введите целые натуральные числа \n")
    while num2 == None:
        try: num2 = int(input("Какое второе число?: "))
        except: print("Пожалуйста введите целые натуральные числа \n")
    return num1, num2

def Do_sum_and_mul(num1, num2):
    mul = num1 * num2
    sum = num1 + num2
    return  sum, mul

# Находим делители
def Find_dividers(mul):
    div=[]
    i=1
    while i < mul:
        if mul % i == 0:
            div.append(i)
        i+=1
    return div

# Перебираем найденные делители
def Find_term(sum, div):
    check = True
    for i in range(len(div)):
        for j in range(len(div)):
            if div[i] + div[j] == sum:
                check = False
                return div[i], div[j]
    if check:
        return "Неверные значения"
            
num1, num2 = Console_input()
sum, mul = Do_sum_and_mul(num1, num2)
print(f"Петя загадал числа {num1} и {num2}")
print(f"Их сумма их равна {sum}, а произведение {mul}")

print(f"Катя угадывает эти числа и это {Find_term(sum, Find_dividers(mul))}")

