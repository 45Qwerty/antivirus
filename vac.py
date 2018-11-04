#определение софта
#кик при софте
num = int (input("Нажмите 1: "))
if num == 1:
    login = int (input("Введите номер своего акк: "))
    paswd = int (input("Введите пароль: "))
    if login == paswd:
        print ("Пароль не может совпадать с акк.")
        exit(0)
    sign = login
    if login == sign:
        sse = int (input("Если у вас нет sse нажмите 1. Если есть нажмите 2: "))
        if sse == 1:
            name = int (input("Введите свой номер (10 цифр): "))
            sse_1 = int (input("Введите желаемый sse:"))
            rel = sse_1
            if sse_1 == rel:
                print ("Проверка завершена. Запомните ваш sse ")
        if sse == 2:
            sse_2 = int (input("Введите sse: "))
            passwd = sse_2
            if sse_2 == passwd:
                print ("Вошли")
