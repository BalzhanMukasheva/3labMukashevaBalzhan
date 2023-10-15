#программа которая пропускает четные числа и выводит сумму всех нечетных
sum_odd = 0
num = int(input("Введите число: "))
if num % 2 == 0:
    'continue'
else:
    sum_odd += num
    print("Сумма нечетных",sum_odd)