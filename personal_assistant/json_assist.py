import json

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