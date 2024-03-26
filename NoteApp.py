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
    note_id = input("Введите ID заметки для обновления: ")
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            text = input("Введите новый текст заметки: ")
            note['title'] = title
            note['text'] = text
            note['date'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            save_notes(notes)
            print("Заметка успешно обновлена.")
            return
    print("Заметка с указанным ID не найдена.")


def delete_note():
    pass


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
    pass


def save_note(note):
    pass


def main():
    while True:
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Просмотреть заметки")
        print("3. Обновить заметку")
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
