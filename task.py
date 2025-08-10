from datetime import datetime
from enum import Enum
import uuid
from typing import Optional
import json

class TaskStatus(Enum):
    NOT_DONE = 'not done'
    DONE = 'done'

class Task:
    def __init__(self,
                 id: str,
                 title: str, 
                 description: str, 
                 created_at: datetime, 
                 status: TaskStatus = TaskStatus.NOT_DONE, 
                 finished_at: Optional[datetime] = None,
                 ):
        self._id = id
        self._title = title
        self._description = description
        self._created_at = created_at
        self._status = status
        self._finished_at = finished_at
        
# properties

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def status(self):
        return self._status
    
    @property
    def finished_at(self):
        return self._finished_at

# setters
    @title.setter
    def title(self, value: str):
        if not value:
            raise ValueError('Title can not be empty!')
        self._title = value

    @description.setter
    def description(self, value: str):
        self._description = value

# status

    def complete(self, completion_time: datetime):
        if self._status == TaskStatus.DONE :
            print('Task is already done!')
            return
        self._finished_at = completion_time
        self._status = TaskStatus.DONE

    def reopen(self):
        if self.status == TaskStatus.NOT_DONE:
            print('Task is already not done!')
            return
        self._finished_at = None
        self._status = TaskStatus.NOT_DONE

# print task

    def __str__(self):
        created = self.created_at.strftime('%Y-%m-%d %H:%M')
        status = self.status.value

        finished = self.finished_at.strftime('%Y-%m-%d %H:%M') if self.finished_at else 'Not finished'
        
        return (f"\nID: {self.id}\n"
                f"  Title: {self.title}\n"
                f"  Description: {self.description}\n"
                f"  Created at: {created}\n"
                f"  Status: {status}\n"
                f"  Finished at: {finished}")
    
    def __repr__(self):
       created = self.created_at.strftime('%Y-%m-%d %H:%M')
       return (f"ID: {self.id}; Title: {self.title}; Created at: {created}")


class TastFactory():
    
    @staticmethod
    def create_task(title: str, description: str,) -> Task:
        id = str(uuid.uuid4())[:9]
        created_at = datetime.now()
        return Task(id, title, description, created_at)


class TaskSerializer():
    
    @staticmethod
    def to_dict(task: Task) -> dict:
        return {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'created_at': task.created_at.isoformat(),
            'status': task.status.value,
            'finished_at': task.finished_at.isoformat() if task.finished_at else None,
        }

    @staticmethod
    def from_dict(task_dict: dict) -> Task:
        return Task(
            id=task_dict['id'],
            title=task_dict['title'],
            description=task_dict['description'],
            created_at=datetime.fromisoformat(task_dict['created_at']),
            status=TaskStatus(task_dict['status']),
            finished_at=datetime.fromisoformat(task_dict['finished_at']) if task_dict.get('finished_at') else None
        )

    @staticmethod
    def json_from_task(task: Task) -> str:
        return json.dumps(TaskSerializer.to_dict(task), indent=4)


    # def dict_from_task(self):
    #     return {
    #         'title': self.title, 
    #         'description': self.description, 
    #         'created_at': self.created_at.isoformat(), 
    #         'status': self.status, 
    #         'finished_at': self.finished_at, 
    #         'id': self.id,
    #     }


