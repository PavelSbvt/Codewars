from utils.output_rich import Rich


Rich.simple_log("Решение задачи")

Rich.debug_log("Условие: получаем массив n*n элементов, который нужно вернуть в виде"
               " 'развёрнутой улитки', возвращайте элементы массива,\n"
               "        расположенные от самых внешних элементов, в средний элемент,"
               " путешествуя по часовой стрелке.")

input_massive = [
                 [1, 2, 3, 4   ],
                 [12, 13 ,14, 5],
                 [11, 16 ,15, 6],
                 [10, 9 ,8 , 7 ]
                ]

def output_mas(input_mas: list) -> None:
    """
    Функция для развёртывания многомерного массива
    :param input_mas: принимаемый массив n*n элементов
    :return: Str - развёрнутый массив в виде одномерного массива
    """

    working_mas = []

    elements = len(input_mas)

    for elements in input_mas:
        # верхняя строка
        working_mas += input_mas.pop(0)

        # правый столбец
        if input_mas and input_mas[0]:
            for row in input_mas:
                working_mas.append(row.pop())

        # нижняя строка
        if input_mas:
            working_mas += input_mas.pop()[::-1]

        # левый столбец
        if input_mas and input_mas[0]:
            for row in reversed(input_mas):
                working_mas.append(row.pop(0))

    Rich.debug_log(working_mas)

    input_mas = working_mas

    Rich.success_log("Массив обработан :)")

output_mas(input_massive)
