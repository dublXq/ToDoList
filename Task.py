
"""Импорт дочернего класса TaskManager"""
import TaskManager

class Task:

    if __name__ == '__main__':

        task_manager = TaskManager.TaskManager()

        with open("notions.txt", "r", encoding="utf-8") as file:
            COUNT_TIME = 1
            COUNT_TASKS = 1
            for line in file:
                line = line.strip()
                line = line.strip(str(COUNT_TIME) + ".")
                if "Срок задачи:" in line:
                    line = line.replace("⟫. Срок задачи:", "").strip()
                    task_manager.dictionary_time[COUNT_TIME] = line
                    COUNT_TIME += 1
                elif "Описание задачи:" in line:
                    line = line.replace("Описание задачи:", "").strip()
                    task_manager.dictionary_tasks[COUNT_TASKS] = line
                    COUNT_TASKS += 1

        while True:
            print("\nДобро пожаловать в твой ToDoList :>.\n\n Приступим к работе?)\n\nВыбери действие\n\n"
                  "1. Добавить новую задачу\n"
                  "2. Просмотреть все задачи\n"
                  "3. Редактировать задачу\n"
                  "4. Удалить задачу\n"
                  "5. Выйти")

            a = input("Ввод: ")

            try:
                if int(a) > 5:
                    print("Нужно выбрать от 1 до 5")
            except ValueError:
                print("Введи пожалуйста число, а не строку")

            match int(a):
                case 1:
                    value = input("Введи описание задачи: ")
                    value_2 = input("Введи срок выполнения: ")
                    if task_manager.add_tasks(value) is True:
                        formatted_date = task_manager.time_tasks(value_2)
                        if formatted_date is not False:
                            i = len(task_manager.dictionary_tasks) + 1
                            task_manager.dictionary_tasks[i] = value
                            task_manager.dictionary_time[i] = formatted_date
                            print("Задача успешно добавлена")
                    else:
                        print("Ошибка: Сбой в системе. Задача не была добавлена")
                case 2:
                    task_manager.read_tasks()
                case 3:
                    task_manager.redaction_tasks()
                case 4:
                    task_manager.del_tasks()
                case 5:
                    if len(task_manager.copy_file_set) == 0 and len(task_manager.dictionary_tasks) == 0:
                        task_manager.sync_file_with_dict()
                        print(f"Отчет:\nВсего задач в файле: {len(task_manager.dictionary_tasks)}.\nДо свидания :)")
                        break
                    elif len(task_manager.copy_file_set) <= len(task_manager.dictionary_tasks):
                        task_manager.sync_file_with_dict()
                        print(f"Отчет:\nВсего задач в файле: {len(task_manager.dictionary_tasks)}."
                              f"\nВсе задачи были успешно сохранены.\nДо встречи :)")
                        break
                    else:
                        print("Жаль что не было новых задач. До новых встреч :)")
                        break