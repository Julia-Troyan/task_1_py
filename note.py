import json
import datetime

def create_note():
    note_id = input("Enter note ID: ")
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def main():
        while True:
            print("1. Создать новую заметку")
            print("2. Читать все заметки")
            print("3. Редактирование заметки")
            print("4. Удаление заметки")
            print("5. Выход из приложения 'Заметки'")