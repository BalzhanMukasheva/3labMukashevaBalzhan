#факториал это произведение всех натуральных чисел до него включительно
try:
    num = int(input('Введите число : '))
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
        print(fact)
except ValueError:
    print("Ввод данных неверный")