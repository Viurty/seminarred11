from json_assist import json_func
from csv_assist import csv_func

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