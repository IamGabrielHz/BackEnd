from fastapi import APIRouter, status, HTTPException, Depends
from persistence.task_models import UserCreate
from persistence.auth_repository import AuthRepository
import infrastructure.hash_provider as hash_provider
import infrastructure.jwt_provider as jwt_provider
from presentation.models import LoginData
from presentation.auth_utils import get_logged_user


router = APIRouter()
prefix = '/auth'

auth_repo = AuthRepository()


@router.post('/signup', status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate):

    user_found = auth_repo.get_user_by_login(user.login)

    if user_found:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Login já utilizado!')