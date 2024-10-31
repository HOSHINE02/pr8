while True:
    try:
        chislo1 = int(input("Введите число: "))
        chislo2 = int(input("Введите число: "))
        result = chislo1 + chislo2
        print(f"Сумма: {result}")
    except ValueError:
        print("Пожалуйста, введите целое число.")
