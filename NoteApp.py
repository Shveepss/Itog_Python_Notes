import json
from datetime import datetime


# Определение структуры заметки
class Note:
    def __init__(self, id, title, text, date):
        self.id = id
        self.title = title
        self.text = text
        self.date = date


def create_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    note = Note(generate_id(), title, text, date)
    save_note(note)
    print("Заметка успешно создана.")


def read_notes():
    start_date = input("Введите дату в формате ДД.ММ.ГГГГ (оставьте пустым для отображения всех заметок): ")
    notes = load_notes()
    filtered_notes = [note for note in notes if start_date == "" or note['date'] >= start_date]
    for note in filtered_notes:
        print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nДата создания: {note['date']}")
        print(f"Текст заметки: {note['text']}")
        print("-" * 20)


def update_note():
    note_id = input("Введите ID заметки для изменения: ")
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            text = input("Введите новый текст заметки: ")
            note['text'] = text
            note['date'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            save_notes(notes)
            print("Заметка успешно изменена.")
            return
    print("Заметка с указанным ID не найдена.")


def delete_note():
    note_id = input("Введите ID заметки для удаления: ")
    notes = load_notes()
    filtered_notes = [note for note in notes if note['id'] != note_id]
    save_notes(filtered_notes)
    print("Заметка успешно удалена.")


def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4, default=vars)


def generate_id():
    notes = load_notes()
    if not notes:
        return "1"
    return str(int(notes[-1]['id']) + 1)


def save_note(note):
    notes = load_notes()
    notes.append(vars(note))
    save_notes(notes)


def main():
    while True:
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Изменить заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
