from note import Note
from task import Task
from finance import FinanceRecorrd
from calculator import Calculator
from contact import Contact

def main():
    exit = False
    while not exit:
        print('''Добро пожаловать в Персональный помощник!
                Выберите действие:
                1. Управление заметками
                2. Управление задачами
                3. Управление контактами
                4. Управление финансовыми записями
                5. Калькулятор
                6. Выход''')
        choice = input('Введите номер действия: ')
        if choice == '1':
            exit_notes = False
            while not exit_notes:
                print('''Добро пожаловать в Управление Заметками!
                                Выберите действие:
                                1. Добавить новую заметку
                                2. Просмотр списка заметок
                                3. Просмотр контента заметки
                                4. Изменение заметки
                                5. Удаление заметки
                                6. Экспорт в CSV
                                7. Импорт в CSV
                                8. Выход''')
                choice = input('Введите номер действия: ')
                if choice == '1':
                    title = input('Введите название: ')
                    content = input('Введите содержание: ')
                    timestamp = input('Введите дату создания в формате ДД-ММ-ГГГГ ЧЧ:ММ:СС : ')
                    note = Note(title,content,timestamp)
                    print(note.create_note())
                if choice == '2':
                    note = Note(None,None,None)
                    note.check_notes()
                if choice == '3':
                    note = Note(None,None,None)
                    id = int(input('Введите id заметки: '))
                    print(note.desc_note(id))
                if choice == '4':
                    note = Note(None,None,None)
                    id = int(input('Введите id заметки: '))
                    data = {}
                    print('Хотите поменять название?')
                    if input('Да/Нет ') == 'Да':
                        data['title'] = input('Введите новое название: ')
                    print('Хотите поменять содержание?')
                    if input('Да/Нет ') == 'Да':
                        data['content'] = input('Введите новое содержание: ')
                    data['timestamp'] = input('Введите дату изменения в формате ДД-ММ-ГГГГ ЧЧ:ММ:СС : ')
                    print(note.rewrite_note(id,data))
                if choice == '5':
                    id = int(input('Введите id заметки: '))
                    note = Note(None, None, None)
                    note.delete_note(id)
                if choice == '6':
                    note = Note(None,None,None)
                    print(note.export_notes('export_note.csv'))
                if choice == '7':
                    note = Note(None,None,None)
                    filename = input('Введите имя файла: ')
                    print(note.import_notes(filename))
                if choice == '8':
                    exit_notes = True
        if choice == '2':
            exit_tasks = False
            while not exit_tasks:
                print('''Добро пожаловать в Управление Задачами!
                                Выберите действие:
                                1. Добавить новую задачу
                                2. Просмотр списка задач
                                3. Отметить задачу выполненной
                                4. Изменение заметки
                                5. Удаление заметки
                                6. Экспорт в CSV
                                7. Импорт в CSV
                                8. Выход''')
                choice = input('Введите номер действия: ')
                if choice == '1':
                    title = input('Введите название: ')
                    description = input('Введите описание: ')
                    done = False
                    priority = input('Введите приоритет: ')
                    due_date = input('Введите дату в формате ДД-ММ-ГГГГ : ')
                    task = Task(title,description,done,priority,due_date)
                    print(task.create_task())
                if choice == '2':
                    task = Task(None,None,None,None,None)
                    task.check_tasks()
                if choice == '3':
                    task = Task(None,None,None,None,None)
                    id = int(input('Введите id задачи: '))
                    print(task.done_task(id))
                if choice == '4':
                    task = Task(None,None,None,None,None)
                    id = int(input('Введите id задачи: '))
                    data = {}
                    print('Хотите поменять название?')
                    if input('Да/Нет ') == 'Да':
                        data['title'] = input('Введите новое название: ')
                    print('Хотите поменять описание?')
                    if input('Да/Нет ') == 'Да':
                        data['description'] = input('Введите новое описание: ')
                    if input('Да/Нет ') == 'Да':
                        data['due_date'] = input('Введите дату в формате ДД-ММ-ГГГГ : ')
                    if input('Да/Нет ') == 'Да':
                        data['priority'] = input('Введите новый приоритет : ')
                    print(task.rewrite_task(id,data))
                if choice == '5':
                    task = Task(None, None, None, None, None)
                    id = int(input('Введите id задачи: '))
                    return task.delete_task(id)
                if choice == '6':
                    task = Task(None, None, None, None, None)
                    print(task.export_tasks('export_note.csv'))
                if choice == '7':
                    task = Task(None, None, None, None, None)
                    filename = input('Введите имя файла: ')
                    print(task.import_tasks(filename))
                if choice == '8':
                    exit_tasks = True
        if choice == '3':
            exit_contact = False
            while not exit_contact:
                print('''Добро пожаловать в Управление Контактами!
                                Выберите действие:
                                1. Добавить новый контакт
                                2. Поиск контакта
                                3. Редактирование контакта
                                4. Удаление контакта
                                5. Экспорт в CSV
                                6. Импорт в CSV
                                7. Выход''')
                choice = input('Введите номер действия: ')
                if choice == '1':
                    name = input('Введите имя: ')
                    phone = input('Введите номер: ')
                    email = input('Введите почту: ')
                    contact = Contact(name, phone, email)
                    print(contact.create_contact())
                if choice == '2':
                    contact = Contact(None, None, None)
                    if input('Поиск по имени или номеру телефону( 1 и 2 соответсвено): ') == 1:
                        filter = {'name' : input('Введите имя пользователя: ')}
                    else:
                        filter = {'phone': input('Введите номер пользователя: ')}
                    print(contact.filter_contact(filter))
                if choice == '3':
                    contact = Contact(None, None, None)
                    id = int(input('Введите id пользователя: '))
                    data = {}
                    print('Хотите поменять имя?')
                    if input('Да/Нет ') == 'Да':
                        data['name'] = input('Введите новое имя: ')
                    print('Хотите поменять номер?')
                    if input('Да/Нет ') == 'Да':
                        data['phone'] = input('Введите новый номер: ')
                    print('Хотите поменять почту?')
                    if input('Да/Нет ') == 'Да':
                        data['email'] = input('Введите новую почту : ')
                    print(contact.rewrite_contact(id, data))
                if choice == '4':
                    id = int(input('Введите id задачи: '))
                    contact = Contact(None, None, None)
                    contact.delete_contact(id)
                if choice == '5':
                    contact = Contact(None, None, None)
                    print(contact.export_contact())
                if choice == '6':
                    contact = Contact(None, None, None)
                    filename = input('Введите имя файла: ')
                    print(contact.import_contact(filename))
                if choice == '7':
                    exit_contact = True
        if choice == '4':
            exit_finance = False
            while not exit_finance:
                print('''Добро пожаловать в Управление Финансами!
                                Выберите действие:
                                1. Добавить новую запись
                                2. Просмотр записей по дате/категории
                                3. Получить отчет за год/месяц
                                4. Экспорт в CSV
                                5. Импорт в CSV
                                6. Выход''')
                choice = input('Введите номер действия: ')
                if choice == '1':
                    amount = float(input('Введите сумму операции: '))
                    category = input('Введите категорию: ')
                    date = input('Введите дату в формате ДД-ММ-ГГГГ: ')
                    description = input('Введите описание: ')
                    finance = FinanceRecorrd(amount,category,date,description)
                    print(finance.create_operation())
                if choice == '2':
                    finance = FinanceRecorrd(None, None, None, None)
                    if input('Фильтрация по дате и категории( 1 и 2 соответсвено): ') == 1:
                        filter = {'date' : input('Введите дату: ')}
                    else:
                        filter = {'category': input('Введите категорию: ')}
                    print(finance.filter_operation(filter))
                if choice == '3':
                    finance = FinanceRecorrd(None,None,None,None)
                    year = input('Введите год( формат YYYY )')
                    if input('Учитывать месяц?: (Да/Нет) ') == 'Да':
                        month =  input('Введите год( формат YYYY )')
                        date = [month,year]
                    else:
                        date = [year]
                    print(finance.feedback(date))
                if choice == '4':
                    finance = FinanceRecorrd(None,None,None,None)
                    print(finance.export_finance())
                if choice == '5':
                    finance = FinanceRecorrd(None,None,None,None)
                    filename = input('Введите имя файла: ')
                    print(finance.import_finance(filename))
                if choice == '6':
                    exit_finance = True
        if choice == '5':
            exit_calc = False
            while not exit_calc:
                print('''Добро пожаловать в Калькулятор!
                                    Выберите действие:
                                    "+" Сложение
                                    "-" Разность
                                    "*" Умножение
                                    ":" Деление
                                    "0" Выход''')
                choice = input('Введите номер действия: ')
                calc =Calculator()
                if choice == '+':
                    res = calc.summary([int(input('Введите первое число: ')),int(input('Введите второе число: '))])
                    print(res)
                if choice == '-':
                    res = calc.minus([int(input('Введите первое число: ')),int(input('Введите второе число: '))])
                    print(res)
                if choice == '*':
                    res = calc.multiply([int(input('Введите первое число: ')),int(input('Введите второе число: '))])
                    print(res)
                if choice == ':':
                    res = calc.division([int(input('Введите первое число: ')),int(input('Введите второе число: '))])
                    print(res)
                if choice == '0':
                    exit_calc = True
        if choice == '6':
            exit = True



if __name__ == '__main__':
    main()