from datetime import datetime
from enum import Enum
import random
import uuid
from typing import Optional

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
        if self.status == TaskStatus.NOT_DONE :
            print('Task is alresdy not done!')

# print task

    def __repr__(self):
        created = self.created_at.strftime('%Y-%m-%d %H:%M')
        finished = self.created_at.strftime('%Y-%m-%d %H:%M')
        line1 = f'title: {self.title}'
        line2 = f'\ndescription: {self.description}'
        line3 = f'\ncreated at: {created}'
        line4 = f'\nfinished at: {finished}' if self.finished else ''
        
        # todo

        return (line1, line2, line3, line4)


class TastFactory():
    pass
    # todo

class TaskSerializer():
    pass
    # todo


    # @classmethod
    # def task_from_dict(cls, task_dict):
    #     return cls(task_dict['title'], 
    #                 task_dict['description'], 
    #                 task_dict['created_at'], 
    #                 task_dict['status'], 
    #                 task_dict['finished_at'], 
    #                 task_dict['id'],
    #                 )


    # def dict_from_task(self):
    #     return {
    #         'title': self.title, 
    #         'description': self.description, 
    #         'created_at': self.created_at.isoformat(), 
    #         'status': self.status, 
    #         'finished_at': self.finished_at, 
    #         'id': self.id,
    #     }


