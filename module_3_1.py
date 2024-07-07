calls = 0
def count_calls():
    global calls  # вызов глобальной переменной
    calls += 1  # добавляем единицу
def string_info(string):
    count_calls()  # вызов функции подсчета вызовов
    string_par = (len(string), string.upper(), string.lower())  # вводим переменную, в которую кладем длину, верхний
# и нижний регистр
    return string_par  # возвращаем переменную
def is_contains(string, list_to_search):  # функция по проверке элементов содержащихся в списке
    count_calls()  # вызов функции подсчета вызовов
    contains_marker = False  # базовый маркер
    for i in list_to_search:  # перебор элементов и проверка их по условию
        if string.lower() == i.lower():  # если string в нижнем регистре равен i
            contains_marker = True  # тогда переключаем маркер и прерываем цикл
            break
    return contains_marker  # возвращаем маркер
print(string_info('Armageddon'))
print(string_info('Tequila'))
print(calls)
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
