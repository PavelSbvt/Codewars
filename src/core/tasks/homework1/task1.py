from utils.output_rich import Rich


# Реализуйте функцию, которая определяет,
# является ли строка, состоящая только из букв, изограммой.
# Считайте, что пустая строка — это изограмма. Регистр букв не учитывается.

Rich.simple_log("Проверка: является ли строка изограммой.")

input_string: str = Rich.input_data("Введите строку")

def check_is_isogram(input_str: str) -> bool:
    """
    Функция, которая проверяет, является ли строка изограммой.

    :param input_str: str - принимает текст строки, которую нужно проверить

    :return: bool - истина, если изограмма выявлена, иначе ложь
    """

    if input_str == "":
        return True

    input_str = input_str.lower()

    if input_str.isalpha():
        Rich.debug_log(set(input_str))

        return len(input_str) == len(set(input_str))

    else:
        Rich.log_error("В строке есть не только буквы")
        return False


if check_is_isogram(input_string):
    Rich.success_log(f"слово '{input_string}' - изограмма")
else:
    Rich.warning_log(f"слово '{input_string}' содержит повторяющиеся символы "
        f"и не является изограммой")
