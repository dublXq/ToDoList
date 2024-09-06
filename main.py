"""Импорт datetime, для реализации форматирования вывода чтения задач"""
import datetime


class Main:
    dict_tasks = []

    # Инициализация
    def __init__(self):
        self.value_tasks = None
        self.tasks = None
        self.bools = None

    # Функция добавление задачи в список dict_tasks
    def add_tasks(self, tasks):
        self.tasks = tasks
        if isinstance(tasks, str):
            self.bools = True
            return True
        else:
            print("Попробуй еще раз. Ты что-то ввел не так")
            self.bools = False
            return False

    # Метод класса, который выполняет дополнительную функцию, к функции add_tasks
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

    # Функция чтения задач из списка dict_tasks
    def read_tasks(self):
        count = 1
        if len(self.dict_tasks) > 0:
            for i in self.dict_tasks:
                if len(i.split('.')) == 3:
                    try:
                        datetime.datetime.strptime(i, '%d.%m.%Y')
                        print("Срок задачи: " + i)
                    except ValueError:
                        print(
                            f'ВНИМАНИЕ: НЕ ВЕРНЫЙ ФОРМАТ. Задача выше ⬆️⬆️⬆️ по Дате ==> "{i}", была удалена из-за не логичности.'
                            f'\nПожалуйста, исправьте это')
                        self.dict_tasks.remove(i)
                        self.dict_tasks.pop()
                else:
                    print(f"{count}. Описание задачи: " + i)
                    count = count + 1

        else:
            print("У вас пока что нет, ни одной задачи")

    # Функция удаления задач из списка dict_tasks
    def del_tasks(self, del_value):
        self.dict_tasks.remove(del_value)

    # Функция редактирования задач из списка dict_tasks
    def redaction_tasks(self):

        if len(self.dict_tasks) > 1:
            print("\nВыбери задачу для редактирования\n")
            self.read_tasks()
            key_value = int(input("Ввод: "))
            print("Мы вошли в задачу. Можешь редактировать")
            key_value += -1
            new_tasks = input("Ввод текста: ")
            self.dict_tasks[key_value] = new_tasks
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
                        main.dict_tasks.append(value)
                        main.dict_tasks.append(formatted_date)
                        print("Задача успешно добавлена")
                else:
                    print("Ошибка: Сбой в системе. Задача не была добавлена")
            case 2:
                main.read_tasks()
            case 3:
                main.redaction_tasks()
            case 4:
                value = input("Введи номер задачи, которую хочешь удалить: ")
                main.del_tasks(value)
            case 5:
                break