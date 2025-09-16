def add_task(tasks, task_name):
    # Ошибка №1: Отсутствует проверка на пустую строку.
    # Пустая задача добавляется в список, что не соответствует ТЗ.
    tasks.append({"task": task_name, "completed": False})
    print("Задача добавлена")

def complete_task(tasks, task_index):
    # Ошибка №2: Проверка на некорректный индекс не учитывает отрицательные значения.
    # Ввод отрицательного индекса вызывает ошибку IndexError.
    if task_index > len(tasks):
        print("Ошибка: Неверный номер задачи")
        return
    tasks[task_index - 1]["completed"] = True
    print("Задача отмечена как выполненная")

def delete_task(tasks, task_index):
    # Ошибка №3: Аналогичная ошибка с индексом, как в complete_task.
    # Отрицательный индекс не проверяется, что приводит к IndexError.
    if task_index > len(tasks):
        print("Ошибка: Неверный номер задачи")
        return
    tasks.pop(task_index - 1)
    print("Задача удалена")

def show_tasks(tasks):
    # Ошибка №4: При пустом списке задач выводится некорректное сообщение.
    # Вместо "Список задач пуст" выводится "Нет задач", что может запутать.
    if not tasks:
        print("Нет задач")
        return
    for i, task in enumerate(tasks, 1):
        # Ошибка №5: Статус задачи всегда выводится как "не выполнена".
        # Логика проверки completed игнорируется.
        status = "не выполнена"
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
            # Ошибка №6: Нет обработки нечислового ввода.
            # Ввод букв (например, "abc") вызывает ValueError.
            task_index = int(input("Введите номер задачи: "))
            complete_task(tasks, task_index)
        elif choice == "3":
            show_tasks(tasks)
            # Ошибка №6 (повторяется): Аналогичная проблема с нечисловым вводом.
            task_index = int(input("Введите номер задачи: "))
            delete_task(tasks, task_index)
        elif choice == "4":
            show_tasks(tasks)
        elif choice == "5":
            print("Программа завершена")
            break
        else:
            # Ошибка №7: Некорректное сообщение об ошибке.
            # Сообщение "Неверный выбор" выводится даже для ввода букв, что неинформативно.
            print("Неверный выбор")

if name == "main":
    main()