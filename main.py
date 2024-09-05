class Main:

    dict_tasks = []

    # Инициализация
    def __init__(self):
        self.tasks = None

    # Функция добавление задачи в список dict_tasks
    def add_tasks(self, tasks):
        self.tasks = tasks
        self.dict_tasks.append(tasks)
        print("Задача успешно добавлена")

    # Метод класса, который выполняет дополнительную функцию, к функции add_tasks
    @classmethod
    def time_tasks(cls, time):
        cls.time = time
        cls.dict_tasks.append(time)

    # Функция чтения задач из списка dict_tasks
    def read_tasks(self):
        return self.dict_tasks

    # Функция удаления задач из списка dict_tasks
    def del_tasks(self, del_value):
        self.dict_tasks.remove(del_value)


if __name__ == '__main__':

    main = Main()

    print("\nДобро пожаловать в твой ToDoList :>.\n\n Приступим к работе?)\n\nВыбери действие\n\n"
          "1. Добавить новую задачу\n"
          "2. Просмотреть все задачи\n"
          "3. Редактировать задачу\n"
          "4. Удалить задачу\n"
          "5. Выйти")

    a = input("Ввод: ")

    match a:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
