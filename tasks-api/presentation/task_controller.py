from fastapi import APIRouter, Depends, status, HTTPException
from presentation.auth_utils import get_logged_user
from persistence.task_models import UserRead, TaskCreate, Task
from persistence.task_repository import TaskRepository

router = APIRouter()
prefix = '/tasks'


@router.get('/')
def get_all_tasks(repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    return repo.get_all_by_user(logged_user)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    task = Task.from_task_create(task_create)
    task.user_id = logged_user.id

    created_task = repo.save(task)
    return created_task


@router.put('/{id}/done', status_code=status.HTTP_200_OK)
def task_done(id: str, repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    task = repo.get_by_id(id)

    if task is not None and task.user_id == logged_user(id):
        repo.task_done(task,True)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

@router.put('/{id}/not_done',status_code=status.HTTP_200_OK)
def task_not_done(id: str, repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    task = repo.get_by_id(id)

    if task is not None and task.user_id == logged_user(id):
        repo.task_done(task,False)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: str, repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    task = repo.get_by_id(id)

    if task is not None and task.user_id == logged_user(id):
        repo.delete_by_user(id)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
