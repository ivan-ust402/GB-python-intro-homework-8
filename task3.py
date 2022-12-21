"""
Задание 3.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class OwnError(Exception):
    """Собственный класс для обработки ошибок"""
    def __init__(self, txt):
        self.txt = txt


first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
    if second_number == 0:
        raise OwnError("Второе число равно нулю, а на ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f'Результат деления чисел: {first_number / second_number}')
