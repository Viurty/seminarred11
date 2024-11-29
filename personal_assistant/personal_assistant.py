import csv
import json


class Note():

    def __init__(self,title,content,timestamp):
        self.title = title
        self.content = content
        self.timestamp = timestamp
        with open('notes.json', 'r') as f:
            try:
                self.id = json.load(f)[-1]['id'] + 1
            except:
                self.id = 1 # Если все заметки были удалены, то присваивается айди = 1

    def create_note(self):
        time = self.timestamp
        try:
            if not(int(time[:2])<=31 and int(time[3:5])<=12 and int(time[6:10])<=2100 and int(time[11:13])<=23 and time[13]==':' and int(time[14:16])<=59 and time[16]==':' and int(time[17:19])<=59 and time[2]=='-' and time[5]=='-' and time[10]==' '):
                return 'Неверный формат даты'
        except:
            return 'Неверный формат даты'
        new_note = {'id' : self.id, 'title' : self.title, 'content' : self.content, 'timestamp' : self.timestamp}
        json_a = json_func()
        json_a.upload('notes.json',new_note)
        return (f"Заметка с id {self.id} загружена")

    def check_notes(self):
        json_a = json_func()
        res = json_a.check('notes.json',['id','title'])
        print(f"Список всех заметок: {res}")

    def desc_note(self,id):
        json_a = json_func()
        res = json_a.search('notes.json',id)
        return res

    def rewrite_note(self,id,new_data):
        file = self.desc_note(id)
        time = new_data['timestamp']
        json_a = json_func()
        try:
            if (not (int(time[:2]) <= 31 and int(time[3:5]) <= 12 and int(time[6:10]) <= 2100 and int(
                    time[11:13]) <= 23 and time[13] == ':' and int(time[14:16]) <= 59 and time[16] == ':' and int(
                    time[17:19]) <= 59 and time[2] == '-' and time[5] == '-' and time[10] == ' ')):
                json_a.upload('notes.json', file)
                return 'Неверный формат даты'
        except:
            json_a.upload('notes.json', file)
            return 'Неверный формат даты'
        self.delete_note(id)
        keys = new_data.keys()
        if 'title' in keys:
            file['title'] = new_data['title']
        if 'content' in keys:
            file['content'] = new_data['content']
        file['timestamp'] = new_data['timestamp']
        json_a.upload('notes.json',file)
        return 'Заметка изменена'

    def delete_note(self,id):
        json_a = json_func()
        json_a.delete('notes.json',id)

    def export_notes(self,filename):
        csv_a = csv_func()
        json_a = json_func()
        data = json_a.check('notes.json',['id','title','content','timestamp'])
        return csv_a.export_csv(filename,data)

    def import_notes(self,filename):
        csv_a = csv_func()
        json_a = json_func()
        try:
            data = csv_a.import_csv(filename)
        except:
            return 'Неверное название файла'
        return json_a.new_file('notes.json',data)

class Task():

    def __init__(self,title,description,done,priority,due_date):
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date
        with open('tasks.json', 'r') as f:
            try:
                self.id = json.load(f)[-1]['id'] + 1
            except:
                self.id = 1 # Если все заметки были удалены, то присваивается айди = 1

    def create_task(self):
        time = self.due_date
        new_task = {'id' : self.id, 'title' : self.title, 'description' : self.description, 'done' : self.done,'priority' : self.priority, 'due_date' : self.due_date}
        json_a = json_func()
        try:
            if not (int(time[:2]) <= 31 and int(time[3:5]) <= 12 and int(time[6:10]) <= 2100 and time[2] == '-' and time[5] == '-'):
                return 'Неверный формат даты'
        except:
            return 'Неверный формат даты'
        json_a.upload('tasks.json', new_task)
        return (f"Заметка с id {self.id} загружена")

    def check_tasks(self):
        json_a = json_func()
        res = json_a.check('tasks.json', ['id', 'title','done','priority','due_date'])
        print(f"Список всех задач: {res}")

    def done_task(self, id):
        json_a = json_func()
        res = json_a.search('tasks.json', id)
        try:
            res['done'] = True
        except:
            return 'Неверный id'
        json_a.delete('tasks.json',id)
        json_a.upload('tasks.json',res)
        return 'Задание выполнено!'

    def rewrite_task(self, id, new_data):
        json_a = json_func()
        file = json_a.search('tasks.json',id)
        try:
            s = file['id']
        except:
            return 'Неверный id'
        json_a.delete('tasks.json',id)
        keys = new_data.keys()
        if 'due_date' in keys:
            time = new_data['due_date']
            try:
                if not (int(time[:2]) <= 31 and int(time[3:5]) <= 12 and int(time[6:10]) <= 2100 and time[2] == '-' and time[5] == '-'):
                    json_a.upload('tasks.json', file)
                    return 'Неверный формат даты'
            except:
                json_a.upload('tasks.json', file)
                return 'Неверный формат даты'
            file['due_date'] = new_data['due_date']
        if 'title' in keys:
            file['title'] = new_data['title']
        if 'description' in keys:
            file['description'] = new_data['description']
        if 'priority' in keys:
            file['priority'] = new_data['priority']
        json_a.upload('tasks.json', file)
        return 'Задача изменена'

    def delete_task(self, id):
        json_a = json_func()
        json_a.delete('tasks.json', id)

    def export_tasks(self, filename):
        csv_a = csv_func()
        json_a = json_func()
        data = json_a.check('tasks.json', ['id', 'title', 'description', 'priority','done','due_date'])
        return csv_a.export_csv(filename, data)

    def import_tasks(self, filename):
        csv_a = csv_func()
        json_a = json_func()
        data = csv_a.import_csv(filename)
        return json_a.new_file('tasks.json', data)

class Contact():

    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        with open('contacts.json', 'r') as f:
            try:
                self.id = json.load(f)[-1]['id'] + 1
            except:
                self.id = 1 # Если все заметки были удалены, то присваивается айди = 1

    def create_contact(self):
        new_contact = {'id' : self.id, 'name' : self.name, 'phone' : self.phone, 'email' : self.email}
        json_a = json_func()
        json_a.upload('contacts.json',new_contact)
        return (f"Контакт с id {self.id} загружена")

    def rewrite_contact(self,id,new_data):
        json_a = json_func()
        file = json_a.search('contacts.json',id)
        json_a.delete('contacts.json', id)
        keys = new_data.keys()
        if 'name' in keys:
            file['name'] = new_data['name']
        if 'phone' in keys:
            file['phone'] = new_data['phone']
        if 'email' in keys:
            file['email'] = new_data['email']
        json_a.upload('contacts.json',file)
        return 'Контакт изменен'

    def filter_contact(self,filter):
        json_a = json_func()
        return json_a.filter('contacts.json',filter)

    def delete_contact(self,id):
        json_a = json_func()
        return json_a.delete('contacts.json',id)

    def export_contact(self):
        csv_a = csv_func()
        json_a = json_func()
        data = json_a.check('contacts.json', ['id', 'name', 'phone', 'email'])
        return csv_a.export_csv('export_contact.csv', data)

    def import_contact(self,filename):
        csv_a = csv_func()
        json_a = json_func()
        data = csv_a.import_csv(filename)
        return json_a.new_file('contacts.json', data)

class FinanceRecorrd():

    def __init__(self,amount,category,date,description):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date
        with open('finance.json', 'r') as f:
            try:
                self.id = json.load(f)[-1]['id'] + 1
            except:
                self.id = 1 # Если все заметки были удалены, то присваивается айди = 1

    def create_operation(self):
        time = self.date
        try:
            if not (int(time[:2]) <= 31 and int(time[3:5]) <= 12 and int(time[6:10]) <= 2100 and time[2] == '-' and time[5] == '-'):
                return 'Неверный формат даты'
        except:
            return 'Неверный формат даты'
        new_operation = {'id' : self.id, 'amount' : self.amount, 'category' : self.category, 'date' : self.date, 'description' : self.description}
        json_a = json_func()
        json_a.upload('finance.json',new_operation)
        return (f"Операция с id {self.id} загружена")

    def filter_operation(self,filter):
        json_a = json_func()
        return json_a.filter('finance.json',filter,True)

    def feedback(self,date):
        if len(date) == 1:
            date = date[0]
            data = self.filter_operation({'date' : date})
            profit = 0
            for i in data:
                profit+=float(i['amount'])
            return f"За {date} прибыль составила {profit}"
        else:
            date=f"{date[0]}-{date[1]}"
            data = self.filter_operation({'date' :  date})
            profit = 0
            for i in data:
                profit+=float(i['amount'])
            return f"За {date} прибыль составила {profit}"


    def export_finance(self):
        csv_a = csv_func()
        json_a = json_func()
        data = json_a.check('finance.json', ['id', 'amount', 'category', 'date', 'description',])
        return csv_a.export_csv('export_finance.csv', data)

    def import_finance(self,filename):
        csv_a = csv_func()
        json_a = json_func()
        data = csv_a.import_csv(filename)
        return json_a.new_file('finance.json', data)


class Calculator():

    def summary(self,number):
        return sum(number)

    def minus(self,number):
        return (number[0]-number[1])

    def multiply(self,number):
        return  number[0]*number[1]

    def division(self,number):
        try:
            self.last_number = number[0]/number[1]
        except:
            return 'Недопустимое значение'
        return number[0]/number[1]


class csv_func():

    def import_csv(self,filename):
        res = []
        with open(filename,'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        return data

    def export_csv(self,filename,data):
        with open(filename,'w') as f:
            writer = csv.writer(f)
            writer.writerow(data[0].keys())
            for dict_ in data:
                writer.writerow(dict_.values())
        return f"Все данные сохранены в файл {filename}"

class json_func():

    def new_file(self,filename,data):
        with open(filename,'w') as f:
            json.dump(data,f)
        return f"Все данные сохраненны в файл {filename} "

    def upload(self,filename,new_data):
        with open(filename,'r') as f:
            data = json.load(f)
        data.append(new_data)
        with open(filename,'w') as f:
            json.dump(data,f)

    def check(self,filename,need):
        with open(filename,'r') as f:
            data = json.load(f)
        res =[]
        for dict_ in data:
            needs = dict()
            for key in need:
                needs[key] = dict_[key]
            res.append(needs)
        return res

    def search(self,filename,id):
        with open(filename, 'r') as f:
            data = json.load(f)
        file = 'Такого id не существует'
        for dict_ in data:
            if int(dict_['id']) == id:
                file = dict_
        return file

    def delete(self,filename,id):
        with open(filename, 'r') as f:
            data = json.load(f)
        for dict_ in data:
            if int(dict_['id']) == id:
                del_file = dict_
        try:
            data.remove(del_file)
        except:
            print("Такого id не существует")
        with open(filename,'w') as f:
            json.dump(data,f)
    def filter(self,filename,filter,case=False):
        res =[]
        with open(filename,'r') as f:
            data = json.load(f)
        for dict_ in data:
            flag = True
            for key in filter:
                if not case:
                    if dict_[key] == filter[key]:
                        continue
                    else:
                        flag = False
                        break
                elif case:
                    if filter[key] in dict_[key] or dict_[key] in filter[key]:
                        continue
                    else:
                        flag = False
                        break
            if flag:
                res.append(dict_)

        return res




data = [{'id' : 1, 'title' : 'Example', 'content' : 'Example', 'timestamp' : 'dd-mm-yyyy hh:mm:ss'}]
with open('notes.json', 'w') as f:
    json.dump(data,f)
data = [{'id' : 1, 'title' : 'Example', 'description' : 'Example', 'done' : False,'priority' : 'example', 'due_date' : 'dd-mm-yyyy'}]
with open('tasks.json', 'w') as f:
    json.dump(data,f)
data = [{'id' : 1, 'name' : 'NAME', 'phone' : '88005553535', 'email' : '@gmail.com'}]
with open('contacts.json','w') as f:
    json.dump(data,f)
data = [{'id' : 1, 'amount' : 9999.0, 'category' : 'Food', 'date' : '28-10-2006', 'description' : 'exapmle........'}]
with open('finance.json','w') as f:
    json.dump(data,f)

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