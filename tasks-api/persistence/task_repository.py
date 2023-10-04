from persistence.task_models import Task, User
from persistence.db_utils import get_engine
from sqlmodel import Session, select


class TaskRepository:

    def __init__(self):
        self.session = Session(get_engine())

    def save(self, task: Task):
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_all_by_user(self, user: User):
        sttm = select(Task).where(Task.user_id == user.id)
        return self.session.exec(sttm).all()

    def get_by_id(self, id: str):
        return self.session.get(Task, id)
    

    def delete_by_user(self,id: str):
        task = self.get_by_id(id)
        self.session.delete(task)
        self.session.commit()
        self.session.close()
        

    def task_done(self,task : Task,did: bool):
        task.done = did
        self.session.add(did)
        self.session.commit()
        self.session.refresh()
        self.session.close()
        return task
        