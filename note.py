import datetime
import json
import os

NOTES_FILE = 'notes.json'

def create_note():
    try:
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
    except Exception as e:
        print("An error occurred while creating the note:", e)
        return None

    return note

def save_notes(notes):
    try:
        with open(NOTES_FILE, 'w') as file:
            json.dump(notes, file, indent=4)
    except Exception as e:
        print("An error occurred while saving notes:", e)

def read_notes():
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE) as file:
            notes = json.load(file)
            for note in notes:
                print("ID: ", note["id"])
                print("Title: ", note["title"])
                print("Body: ", note["body"])
                print("Created on: ", note["created_date"])
                print()
    except Exception as e:
        print("An error occurred while reading notes:", e)

def filter_notes_by_date(start_date, end_date):
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return []

        with open(NOTES_FILE) as file:
            notes = json.load(file)
            filtered_notes = [note for note in notes if start_date <= note["created_date"] <= end_date]
            return filtered_notes
    except Exception as e:
        print("An error occurred while filtering notes by date:", e)
        return []

def print_selected_note(note_id):
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE) as file:
            notes = json.load(file)
            for note in notes:
                if note["id"] == note_id:
                    print("ID: ", note["id"])
                    print("Title: ", note["title"])
                    print("Body: ", note["body"])
                    print("Created on: ", note["created_date"])
                    print()
                    return

            print("Note with ID {} not found.".format(note_id))
    except Exception as e:
        print("An error occurred while printing selected note:", e)

def edit_note(note_id):
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)

        for note in notes:
            if note["id"] == note_id:
                title = input("Enter new title: ")
                body = input("Enter new body: ")
                note["title"] = title
                note["body"] = body
                note["created_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break

        save_notes(notes)
    except Exception as e:
        print("An error occurred while editing note:", e)

def delete_note(note_id):
    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)

        notes = [note for note in notes if note["id"] != note_id]
        save_notes(notes)
    except Exception as e:
        print("An error occurred while deleting note:", e)