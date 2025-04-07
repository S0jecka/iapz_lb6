# task_manager.py
tasks = []

def add_task(text):
    task = {"text": text, "done": False}
    tasks.append(task)
    return task
    
def list_tasks():
    return tasks

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False

def delete_task(index):
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    return None

# нижче — тільки консольний інтерфейс, який не треба тестити
def show_menu():
    print("\n===== Менеджер задач =====")
    print("1. Додати задачу")
    print("2. Показати задачі")
    print("3. Відзначити задачу як виконану")
    print("4. Видалити задачу")
    print("5. Вийти")
    print("==========================")

def show_tasks():
    if not tasks:
        print("Список задач порожній.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} {task['text']}")

def main():
    while True:
        show_menu()
        choice = input("Обери опцію (1-5): ")
        if choice == "1":
            text = input("Введи задачу: ")
            add_task(text)
            print("Задачу додано!")
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_tasks()
            try:
                index = int(input("Номер задачі: ")) - 1
                if mark_done(index):
                    print("Задачу відзначено як виконану ✅")
                else:
                    print("Невірний номер")
            except ValueError:
                print("Це не число.")
        elif choice == "4":
            show_tasks()
            try:
                index = int(input("Номер задачі: ")) - 1
                deleted = delete_task(index)
                if deleted:
                    print(f"Задачу '{deleted['text']}' видалено.")
                else:
                    print("Невірний номер.")
            except ValueError:
                print("Це не число.")
        elif choice == "5":
            print("До зустрічі 👋")
            break
        else:
            print("Невірна опція, спробуй ще раз.")

if __name__ == "__main__":
    main()
