import json
from task import Task, TaskSerializer, TastFactory
from config import DATA_PATH
from enum import Enum
from typing import Optional
from datetime import datetime

# class Parametrs(Enum):
#     ID = 'id'
#     TITLE = 'title'
#     DESCRIPTION = 'description'
#     CREATED_AT = 'created_at'
#     STATUS = 'status'
#     FINISHED_AT = 'finished_at'


class TaskDB:
    _instance = None
    
    def __new__(cls, path=DATA_PATH):
        if cls._instance is None:
            cls._instance = super(TaskDB, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, path=DATA_PATH):
        if self._initialized:
            return
        self._path = path
        self._tasks: list[Task] = self.load_tasks()
        self._initialized = True

    def load_tasks(self) -> list[Task]:
        try:
            with open(self._path, 'r') as file:
                tasks_json = json.load(file)
                return [TaskSerializer.from_dict(task_data) for task_data in tasks_json]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        try:
            with open(self._path, 'w') as file:
                task_list = [TaskSerializer.to_dict(task) for task in self._tasks]
                json.dump(task_list, file, indent=4)
        except IOError as e:
            print(f"Error: Could not save to '{self._path}'. {e}")

class TaskDB_Manager:
    
    def __init__(self, db_handler: TaskDB):
        self._db_handler = db_handler
        self._tasks = self._db_handler._tasks
        
    def find(self, id: str) -> Optional[Task]:
        
        for task in self._tasks:
            if id in task.id:
                return task
        return None
    
    def find_by_all_parametrs(self, value) -> list[Task]:
        return_list: list[Task] = []
        for task in self._tasks:
            if value in task.id.lower() or value in task.title.lower() or value in task.description.lower():
                return_list.append(task)
        return return_list

    def get_all_tasks(self) -> list[Task]:
        
        return self._tasks

    def add_task(self, title: str, description: str) -> Task:
        
        new_task = TastFactory.create_task(title, description)
        self._tasks.append(new_task)
        self._db_handler.save_tasks()
        print(f"Task '{title}' added.")
        return new_task

    def get_task_by_id(self, id: str) -> list[Optional[Task]]:
        
        task: list[Optional[Task]] = self.find(id)
        if not task:
            print(f"Task with ID '{id}' not found.")
        return task

    def delete_task(self, task_id: str) -> bool:
        
        task = self.find(task_id)
        if task:
            self._tasks.remove(task)
            self._db_handler.save_tasks()
            print(f"Task '{task.title}' (ID: {task_id}) deleted.")
            return True
        print(f"Could not delete. Task with ID '{task_id}' not found.")
        return False

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        task = self.find(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            self._db_handler.save_tasks()
            print(f"Task '{task.title}' (ID: {task_id}) updated.")
            return task
        print(f"Could not update. Task with ID '{task_id}' not found.")
        return None
        
    def complete_task(self, task_id: str) -> Optional[Task]:
        task = self.find(task_id)
        if task:
            task.complete(datetime.now())
            self._db_handler.save_tasks()
            print(f"Task '{task.title}' marked as complete.")
            return task
        print(f"Could not complete. Task with ID '{task_id}' not found.")
        return None

    def reopen_task(self, task_id: str) -> Optional[Task]:
        task = self.find(task_id)
        if task:
            task.reopen()
            self._db_handler.save_tasks()
            print(f"Task '{task.title}' reopened.")
            return task
        print(f"Could not reopen. Task with ID '{task_id}' not found.")
        return None