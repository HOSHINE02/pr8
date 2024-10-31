summa = 0.0

print("Введите числа для суммирования. Введите 'stop' или 'end' для завершения.")

while True:
    input_ch = input("Введите число: ").strip().lower()
    
    if input_ch == "stop" or input_ch == "end":
        break
    
    try:
        number = float(input_ch)
        summa += number
    except ValueError:
        print("Ошибка: введите корректное число или 'stop'/'end' для завершения.")

print("Сумма введённых чисел:", summa)
