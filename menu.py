import note


def create_note(num):
    title = check_len_text_input(
        input('Введите название заметки: '), num)
    body = check_len_text_input(
        input('Введите содержание заметки: '), num)
    return note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Выполняет следующие функции:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Введите не менее {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def world():
    print("Миру - мир!")