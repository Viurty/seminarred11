from json_assist import json_func
from csv_assist import csv_func

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