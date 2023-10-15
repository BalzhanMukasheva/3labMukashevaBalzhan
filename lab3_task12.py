#подсчет простых чисел
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    N = int(input("Введите число: "))
    if N <= 0:
        print("Введите положительное число: ")
    else:
        print(f"Простые числа в промежутке 1 to {N}:")
        num = 2
        while num <= N:
            if is_prime(num):
                print(num, end=" ")
            num += 1
except ValueError:
    print("Ввод неверный")