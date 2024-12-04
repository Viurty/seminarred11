from json_assist import json_func
from csv_assist import csv_func

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