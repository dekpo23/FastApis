data = [
    {"ID": 1, "Name": "David Ekpo", "track": "AI Engineering", "age": 25, "comments": "None"},
    {"ID": 2, "Name": "Dolapo Onifade", "track": "AI Developer", "age": 26, "comments": "Fuck you"}
]

def get_dic(id):
    for i, dic in enumerate(data):
        if dic["ID"] == id:
            return i

data.remove(data[get_dic(1)])
print(data)