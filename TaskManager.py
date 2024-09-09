
"""Импорт datetime, для реализации форматирования вывода чтения задач"""
import datetime
import re

class TaskManager:
    """Главный Backend класс, который имеет в себе методы проекта"""

    path = "notions.txt"

    # Инициализация
    def __init__(self):
        self.tasks = None
        self.bools = False
        self.dictionary_tasks = {}
        self.dictionary_time = {}
        self.time = None
        self.copy_file_set = list()
        self.copy_task_set = list()
        self.pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"

    # Функция добавление задачи в словарь dictionary_tasks
    def add_tasks(self, tasks):
        self.tasks = tasks
        if isinstance(tasks, str):
            self.bools = True
            return True
        else:
            print("Попробуй еще раз. Ты что-то ввел не так")
            self.bools = False
            return False

    # Метод, который выполняет дополнительную функцию, к методу dictionary_tasks
    def time_tasks(self, time):
        self.time = time

        if time[2] == " " and time[5] == " ":
            self.time = time.replace(" ", ".")  # Убираем пробелы из строки
            self.bools = True
            return self.time
        elif time[2] == "-" and time[5] == "-":
            self.time = time.replace("-", ".")  # Убираем тире из строки
            self.bools = True
            return self.time
        elif time[2] == "." and time[5] == ".":  # Верная запись
            self.bools = True
            return self.time
        elif time[2] == "," and time[5] == ",":
            self.time = time.replace(",", ".")  # Убираем запятую из строки
            self.bools = True
            return self.time
        elif time[2] == "+" and time[5] == "+":
            self.time = time.replace("+", ".")  # Убираем плюсы из строки
            self.bools = True
            return self.time
        else:
            print("Не верный формат даты")
            self.bools = False
            return False

    # Функция чтения задач из словаря dictionary_tasks
    def read_tasks(self) -> None:

        count = 1

        if len(self.dictionary_tasks) > 0 and len(self.dictionary_time) > 0:
            for element_task in self.dictionary_tasks.values():
                print(f"{count}.\nОписание задачи: " + element_task)
                for element_time in self.dictionary_time.values():
                    if len(element_time.split('.')) == 3:
                        try:
                            datetime.datetime.strptime(element_time, '%d.%m.%Y')
                            print("Срок задачи: " + self.dictionary_time[count])
                            count += 1
                            break
                        except ValueError:
                            print(
                                f'ВНИМАНИЕ: НЕ ВЕРНЫЙ ФОРМАТ. Задача выше ⬆️⬆️⬆️ по Дате ==> "{element_time}", была удалена из-за не логичности.'
                                f'\nПожалуйста, исправьте это')
                            self.dictionary_tasks.pop(element_time)
                            self.dictionary_time.pop(element_time)
        else:
            print("У вас пока что нет, ни одной задачи")

    # Функция удаления задач из словаря dictionary_tasks
    def del_tasks(self):
        if len(self.dictionary_tasks) >= 1:
            print("\nВыберите задачу для удаления\n")
            self.read_tasks()
            key_value = int(input("Ввод: "))
            if int(key_value) <= len(self.dictionary_tasks):
                # Удаление элемента
                self.dictionary_tasks.pop(key_value)
                self.dictionary_time.pop(key_value)

                # Создание новых словарей с обновленными ключами
                new_tasks = {}
                new_time = {}
                new_key = 1

                for old_key in sorted(self.dictionary_tasks.keys()):
                    new_tasks[new_key] = self.dictionary_tasks[old_key]
                    new_time[new_key] = self.dictionary_time[old_key]
                    new_key += 1

                # Перезапись словарей
                self.dictionary_tasks = new_tasks
                self.dictionary_time = new_time

                print("Задача была успешно удалена")
        else:
            print("У вас пока что нет, ни одной задачи")

    def redaction_tasks(self):

        if len(self.dictionary_tasks) >= 1:
            print("\nВыбери задачу для редактирования\n")
            self.read_tasks()
            key_value = int(input("Ввод: "))
            print("Мы вошли в задачу. Можешь редактировать")
            new_tasks = input("Ввод текста: ")
            self.dictionary_tasks[key_value] = new_tasks
            print("Задача была успешно отредактирована :)")
        else:
            print("Ошибка: На данный момент, у вас нет задач. Добавьте свою первую задачу, нажав на 1, в модуле выбора :)")

    def sync_file_with_dict(self):
        # ------------------------------------------------------------------------------

        # Блок кода который берет из файла все элементы, и записывает в список

        # ------------------------------------------------------------------------------
        count = 1
        with open(self.path, "r", encoding="utf-8") as read_file_item:
            copy_file_line = read_file_item.readlines()
            for item in copy_file_line:
                item = item.strip("\n")
                if "Описание задачи" in item:
                    item = item.replace(str(count) + ". " + "Описание задачи: ", '')
                    self.copy_file_set.append(item)
                    count += 1
                elif "Срок задачи" in item:
                    item = item.replace("⟫. " + "Срок задачи: ", '')
                    self.copy_file_set.append(item)

        # ------------------------------------------------------------------------------

        # Блок кода который проверяет наличие элемента из списка, в словаре
        # И записывает элемент в новый список, если есть и нет его нет в файле

        # ------------------------------------------------------------------------------
        for item in self.dictionary_tasks.values():
            time_count_index = 0  # 3-й проверки (2-й if)
            if item in self.copy_file_set:
                self.copy_task_set.append(item)
                time_count_task_index = self.copy_file_set.index(item) + 1
                self.copy_task_set.append(self.copy_file_set[time_count_task_index])

            elif item not in self.copy_file_set:
                self.copy_task_set.append(item)
                for key, value in self.dictionary_tasks.items():
                    if item == value:
                        time_count_index = key
                self.copy_task_set.append(self.dictionary_time[time_count_index])
            else:
                print("Элемент есть в файле, но нет в словаре")
        # ------------------------------------------------------------------------------
        with open(self.path, "w", encoding="utf-8") as write_file_item:
            for item in self.copy_task_set:
                if re.match(self.pattern, item):
                    write_file_item.write("⟫. Срок задачи: " + item + "\n")
                else:
                    write_file_item.write("Описание задачи: " + item + "\n")