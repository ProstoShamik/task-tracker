import json

class Task_DB:

    def __init__(self):
        db = self.__load_db()

    
    def __load_db(self) -> list:
        try:
            with open('data/task_db.json', 'r') as file:
                self.db = json.load(file)
        except:
            print('''Can't load task_db.json''')
            return []

        for 
        
        

