# Функция для ввода числа с проверкой на корректность
def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное целое число.")

# Запрос чисел у пользователя
a = input_number("Введите первое число (a): ")
b = input_number("Введите второе число (b): ")

# Определение диапазона для вывода чисел между a и b
if a < b:
    for i in range(a + 1, b):
        print(i)
elif a > b:
    for i in range(a - 1, b, -1):
        print(i)
else:
    print("Между числами нет целых чисел, так как они равны.")

# Запрос чисел у пользователя
a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))

# Определение диапазона для вывода чисел между a и b
if a < b:
    for i in range(a + 1, b):
        print(i)
elif a > b:
    for i in range(a - 1, b, -1):
        print(i)
else:
    print("Между числами нет целых чисел, так как они равны.")
