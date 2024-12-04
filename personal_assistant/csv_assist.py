import csv

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