import json
from task import Task, TaskSerializer

class Task_DB:

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Task_DB, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, path='data/task_db.json'):
        if self._initialized:
            return
        self._path = path
        self._tasks: list[Task] = self.__load_db_from_json()
        self._initialized = True


    def __load_db_from_json(self) -> list[Task]:
        try:
            with open(self._path, 'r') as file:
                tasks_json = json.load(file)
                return [TaskSerializer.from_dict(task_data) for task_data in tasks_json]
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Warning: Can't load '{self._path}'. Starting with an empty task list.")
            return []



        
        
        

