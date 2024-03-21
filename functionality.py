import array_list
import note
import menu

num = 6
def add():
    note = menu.create_note(num)
    array = array_list.read_file()
    for list in array:
        if note.Note.get_id(note) == note.Note.get_id(list):
            note.Note.set_id(note)
    array.append(note)
    array_list.write_file(array, 'a')
    print('Данная заметка добавлена... ')


def show(text):
    logic = True
    array = array_list.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for list in array:
        if text == 'all':
            logic = False
            print(note.Note.map_note(list))
        if text == 'id':
            logic = False
            print('ID: ' + note.Note.get_id(list))
        if text == 'date':
            logic = False
            if date in note.Note.get_date(list):
                print(note.Note.map_note(list))
    if logic:
        print('Заметок нет ...')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = array_list.read_file()
    logic = True
    for list_note in array:
        if id == note.Note.get_id(list_note):
            logic = False
            if text == 'edit':
                note_obj = menu.create_note(6)
                note.Note.set_title(list_note, note_obj.get_title())
                note.Note.set_body(list_note, note_obj.get_body())
                note.Note.set_date(list_note)
                print('Изменения в заметку внесены ...')
            if text == 'del':
                array.remove(list_note)
                print('Заметка удалена ...')
                array_list.write_file(array, 'w')  # Сохранение изменений в файл
            if text == 'show':
                print(note.Note.map_note(list_note))
    if logic:
        print('Данная заметка отсутствует, может быть, введен неверный id ')