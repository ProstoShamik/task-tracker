import json
import task

class Task_DB:

    def __init__(self):
        db = self.__load_db_from_json()

    
    def __load_db_from_json(self) -> list:
        try:
            with open('data/task_db.json', 'r') as file:
                tasks_json = json.load(file)
                for task in tasks_json:
                    
        except:
            print('''Can't load task_db.json''')
            return []
        



        
        
        

