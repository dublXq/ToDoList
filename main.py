"""Импорт datetime, для реализации форматирования вывода чтения задач"""
import datetime


class Main:
    dictionary_tasks = {}
    dictionary_time = {}

    # Инициализация
    def __init__(self):
        self.value_tasks = None
        self.tasks = None
        self.bools = None

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

    # Метод класса, который выполняет дополнительную функцию, к методу dictionary_tasks
    @classmethod
    def time_tasks(cls, time):
        cls.time = time

        if time[2] == " " and time[5] == " ":
            cls.time = time.replace(" ", ".")  # Убираем пробелы из строки
            cls.bools = True
            return cls.time
        elif time[2] == "-" and time[5] == "-":
            cls.time = time.replace("-", ".")  # Убираем тире из строки
            cls.bools = True
            return cls.time
        elif time[2] == "." and time[5] == ".":
            cls.bools = True
            return cls.time
        else:
            print("Не верный формат даты")
            cls.bools = False
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
                            print(f'ВНИМАНИЕ: НЕ ВЕРНЫЙ ФОРМАТ. Задача выше ⬆️⬆️⬆️ по Дате ==> "{element_time}", была удалена из-за не логичности.'
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
            if int(key_value) <= len(main.dictionary_tasks):
                self.dictionary_tasks.pop(key_value)
                self.dictionary_time.pop(key_value)
        else:
            print("У вас пока что нет, ни одной задачи")

    # Функция редактирования задач из словаря dictionary_tasks
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


if __name__ == '__main__':

    main = Main()

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
                if main.add_tasks(value) is True:
                    formatted_date = main.time_tasks(value_2)
                    if formatted_date is not False:
                        i = len(main.dictionary_tasks) + 1
                        main.dictionary_tasks[i] = value
                        main.dictionary_time[i] = formatted_date
                        print("Задача успешно добавлена")
                else:
                    print("Ошибка: Сбой в системе. Задача не была добавлена")
            case 2:
                main.read_tasks()
            case 3:
                main.redaction_tasks()
            case 4:
                main.del_tasks()
            case 5:
                break
