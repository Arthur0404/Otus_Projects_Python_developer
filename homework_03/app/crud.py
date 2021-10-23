from typing import Dict, List

from schemas import UserIn, User

USER_ID_TO_USER: Dict[int, User] = {}
USER_TOKEN_TO_USER: Dict[str, User] = {}


def create_user(user_in: UserIn) -> User:
    user = User(id=len(USER_ID_TO_USER) + 1, **user_in.dict())
    USER_ID_TO_USER[user.id] = user
    USER_TOKEN_TO_USER[user.token] = user
    return user


def list_users() -> List[User]:
    return list(USER_ID_TO_USER.values())
