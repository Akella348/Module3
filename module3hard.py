data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    total_sum = 0
    total_len = 0
    def structure_checker(item):
        nonlocal total_sum, total_len  # обращаемся к введенным в головной функции переменным
        if isinstance(item, (list, tuple, set)):  # вводим проверку класса на список кортеж или множество
            for object in item:  # и каждый объект из взятого элемента
                structure_checker(object)  # рекурсивно обращаемся по функции
        elif isinstance(item, dict):  # вводим проверку класса на словарь
            for key, value in item.items():  # и каждый объект из взятого элемента
                structure_checker(key)  # рекурсивно обращаемся по функции для ключа
                structure_checker(value)  # рекурсивно обращаемся по функции для значения
        elif isinstance(item, int):  # вводим проверку класса на целое число
            total_sum += item  # добавляем его в переменную
        elif isinstance(item, float):  # вводим проверку класса на число с плавающей точкой
            total_sum += int(item)  # добавляем его в переменную
        elif isinstance(item, str):  # вводим проверку класса на строку
            total_len += len(item)  # добавляем его в переменную
    structure_checker(data_structure)  # обращаемся к функции с вводом исходника
    return total_sum + total_len  # суммируем

result = calculate_structure_sum(data_structure)
print(result)