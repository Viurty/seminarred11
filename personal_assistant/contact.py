from json_assist import json_func
from csv_assist import csv_func

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