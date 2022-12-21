"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""
from copy import deepcopy


class Matrix:
    """
    Класс для матриц
    """
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        view_matrix = ''
        for i in self.matrix_list:
            for j in i:
                view_matrix += f'{j} '
            view_matrix += '\n'
        return view_matrix

    def __add__(self, other):
        first_length = len(self.matrix_list)
        second_length = len(other.matrix_list)
        result = deepcopy(self.matrix_list)
        for i in range(first_length):
            for j in range(second_length):
                result[i][j] += other.matrix_list[i][j]
        return Matrix(result)


my_matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Первая матрица:")
print(my_matrix_1)
my_matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Вторая матрица:")
print(my_matrix_2)
print("Результирующая матрица:")
print(my_matrix_1 + my_matrix_2)
