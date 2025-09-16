def add_task(tasks, task_name):
    if not task_name.strip():
        print("Ошибка: Название задачи не может быть пустым")
        return
    tasks.append({"task": task_name, "completed": False})
    print("Задача добавлена")

def complete_task(tasks, task_index):
    if task_index <= 0 or task_index > len(tasks):
        print("Ошибка: Неверный номер задачи")
        return
    tasks[task_index - 1]["completed"] = True
    print("Задача отмечена как выполненная")

def delete_task(tasks, task_index):
    if task_index <= 0 or task_index > len(tasks):
        print("Ошибка: Неверный номер задачи")
        return
    tasks.pop(task_index - 1)
    print("Задача удалена")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст")
        return
    for i, task in enumerate(tasks, 1):
        status = "выполнена" if task["completed"] else "не выполнена"
        print(f"{i}. {task['task']} ({status})")

def main():
    tasks = []
    while True:
        print("\n1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Удалить задачу")
        print("4. Показать список задач")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ")
        
        if choice == "1":
            task_name = input("Введите название задачи: ")
            add_task(tasks, task_name)
        elif choice == "2":
            show_tasks(tasks)
            try:
                task_index = int(input("Введите номер задачи: "))
                complete_task(tasks, task_index)
            except ValueError:
                print("Ошибка: Введите корректный номер задачи")
        elif choice == "3":
            show_tasks(tasks)
            try:
                task_index = int(input("Введите номер задачи: "))
                delete_task(tasks, task_index)
            except ValueError:
                print("Ошибка: Введите корректный номер задачи")
        elif choice == "4":
            show_tasks(tasks)
        elif choice == "5":
            print("Программа завершена")
            break
        else:
            print("Ошибка: Неверный выбор. Введите число от 1 до 5")

if __name__ == "__main__":
    main()