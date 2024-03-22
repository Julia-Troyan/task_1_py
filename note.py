import json
import datetime

def create_note():
    note_id = input("Enter note ID: ")
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_date": created_date
    }

    return note

    def save_note(note):
        with open('notes.json', 'a') as file:
            json.dump(note, file)
            file.write('\n')

    def read_notes():
        with open('notes.json') as file:
            for line in file:
                note = json.loads(line)
                print("ID: ", note["id"])
                print("Title: ", note["title"])
                print("Body: ", note["body"])
                print("Created on: ", note["created_date"])
                print()




    def main():
        while True:
            print("1. Создать заметку")
            print("2. Просмотреть все заметки")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Выход из приложения 'Заметки'")

            choice = input("Введите свой выбор: ")

            if choice == "1":
                note = create_note()
                save_note(note)
            elif choice == "2":
                read_notes()
            elif choice == "3":
                note_id = input("Введите ID заметки для редактирования: ")
                edit_note(note_id)
            elif choice == "4":
                note_id = input("Введите ID заметки для редактирования: ")
                delete_note(note_id)
            elif choice == "5":
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте еще раз...")

    if __name__ == "__main__":
        main()