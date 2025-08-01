from datetime import datetime
from enum import Enum
import random
import uuid
from typing import Optional

class TaskStatus(Enum):
    NOT_DONE = 'not done'
    DONE = 'done'

class Task:
    def __init__(self, title: str, 
                 description: str, 
                 created_at: Optional[datetime] = None, 
                 status = TaskStatus.NOT_DONE, 
                 finished_at: Optional[datetime] = None, 
                 id: Optional[str] = None):
        self.title = title
        self.description = description
        self.created_at = created_at or str(datetime.now)
        self.status = status
        self.finished_at = finished_at
        self.id = id or str(uuid.uuid4())[:9]


    def __str__(self):
        return f'''title: {self.title}; description: {self.description}; created_at: {self.created_at}; status: {self.status.value}{f"; finished_at: {self.finished_at}" if self.finished_at else ''}'''
    
    def change_title(self, new_title):
        self.title = new_title

    def change_description(self, new_description):
        self.description = new_description

    def change_status(self, new_status):
        self.status = new_status


