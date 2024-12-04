import json

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