from sqlalchemy import Column, Integer, Boolean, String
from configs.db import db

class Plan(db.Model):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())
    finished = Column(Boolean)
    priority = Column(Integer)


    def __init__(self, title, description,finished, priority):
        self.title = title
        self.description = description
        self.finished = finished
        self.priority = priority

    @property
    def dictionary(self):
        return dict({
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'finished': self.finished,
            'priority': self.priority,
        })

    
