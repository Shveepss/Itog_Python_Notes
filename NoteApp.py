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
    created_at = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    note = Note(generate_id(), title, text, created_at)
    save_note(note)
    print("Заметка успешно создана.")


def read_notes():
    pass


def update_note():
    pass


def delete_note():
    pass


def load_notes():
    pass


def save_notes(notes):
    pass


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
