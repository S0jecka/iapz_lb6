tasks = []

def show_menu():
    print("\n===== Менеджер задач =====")
    print("1. Додати задачу")
    print("2. Показати задачі")
    print("3. Відзначити задачу як виконану")
    print("4. Видалити задачу")
    print("5. Вийти")
    print("==========================")

def add_task():
    task = input("Введи задачу: ")
    tasks.append({"text": task, "done": False})
    print("Задачу додано!")

def show_tasks():
    if not tasks:
        print("Список задач порожній.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} {task['text']}")

def mark_done():
    show_tasks()
    try:
        index = int(input("Введи номер задачі для відзначення як виконаної: ")) - 1
        tasks[index]["done"] = True
        print("Готово!")
    except (IndexError, ValueError):
        print("Неправильний номер.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Введи номер задачі для видалення: ")) - 1
        deleted = tasks.pop(index)
        print(f"Задачу '{deleted['text']}' видалено.")
    except (IndexError, ValueError):
        print("Неправильний номер.")

def main():
    while True:
        show_menu()
        choice = input("Обери опцію (1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("До зустрічі 👋")
            break
        else:
            print("Невірна опція, спробуй ще раз.")

if __name__ == "__main__":
    main()
