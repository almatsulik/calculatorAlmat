import math

# initialize last_result to 0
last_result = 0

while True:
    print("Доступные операции: ")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Синус")
    print("7. Косинус")
    print("8. Тангенс")
    print("9. Использовать предыдущий результат")
    print("10. Выход")
    # Запрос пользовательского ввода
    choice = input("Выберите операцию (1-10): ")

    # Проверка ввода на корректность
    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print("Неверный ввод")
    elif choice == '10':
        break
    elif choice == '9' and last_result == 0:
        print("Предыдущий результат отсутствует")
    elif choice == '9':
        operation = input("Введите операцию.  +, -, *, /, **, s, c, t: ")
        if operation == 's':
            result = math.sin(last_result)
            print("sin(", last_result, ") =", result)
        elif operation == 'c':
            result = math.cos(last_result)
            print("cos(", last_result, ") =", result)
        elif operation == "t":
            result = math.tan(last_result)
            print("tan(", last_result, ") =", result)
        else:
            num2 = float(input("Введите второе число: "))
            if operation == '+':
                result = last_result + num2
            elif operation == '-':
                result = last_result - num2
            elif operation == '*':
                result = last_result * num2
            elif operation == '/':
                if num2 == 0:
                    print("Деление на ноль невозможно")
                else:
                    result = last_result / num2
            elif operation == '**':
                result = last_result ** num2
            else:
                print("Неверный ввод операции")
                continue
            print(last_result, operation, num2, "=", result)
        last_result = result
    else:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        # Выполнение выбранной операции
        if choice == '1':
            result = num1 + num2
            print(num1, "+", num2, "=", result)
        elif choice == '2':
            result = num1 - num2
            print(num1, "-", num2, "=", result)
        elif choice == '3':
            result = num1 * num2
            print(num1, "*", num2, "=", result)
        elif choice == '4':
            if num2 == 0:
                print("Деление на ноль невозможно")
            else:
                result = num1 / num2
                print(num1, "/", num2, "=", result)
        elif choice == '5':
            result = num1 ** num2
            print(num1, "**", num2, "=", result)
        elif choice == '6':
            result = math.sin(num1)
            print("sin(", num1, ") =", result)
        elif choice == '7':
            result = math.cos(num1)
            print("cos(", num1, ") =", result)
        elif choice == '8':
            result = math.tan(num1)
            print("tan(", num1, ") =", result)

        last_result = result
