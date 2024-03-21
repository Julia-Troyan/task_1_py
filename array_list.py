import menu
import note
import array_list
from functionality import num


def write_file(array, mode):
    try:
        with open("list.csv", mode=mode, encoding='utf-8') as file:
            for list in array:
                file.write(note.Note.to_string(list))
                file.write('\n')
    except IOError:
        print('Ошибка при записи в файл')

def read_file():
    try:
        array = []
        with open("list.csv", "r", encoding='utf-8') as file:
            notes = file.read().strip().split("\n")
            for n in notes:
                split_n = n.split(';')
                note_obj = note.Note(
                    id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
                array.append(note_obj)
    except Exception:
        print('Нет сохраненных заметок...')
        return []
    return array

def add():
    new_note = menu.create_note(num)
    array = array_list.read_file()
    for existing_note in array:
        if note.Note.get_id(new_note) == note.Note.get_id(existing_note):
            note.Note.set_id(new_note)
    array.append(new_note)
    array_list.write_file(array, 'a')
    print('Данная заметка добавлена...')