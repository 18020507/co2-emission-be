from typing import Optional, List

import jwt
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.models import User, Role
from app.schemas.sche_base import DataResponse
from app.schemas.sche_token import TokenPayload

from app.schemas.sche_user import Register, UserDTO, UserNormalDTO
from app.core.security import verify_password, get_password_hash
from fastapi import Depends, HTTPException

from fastapi_sqlalchemy import db


class UserService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def authenticate(*, email: str, password: str) -> Optional[User]:
        """
        Check username and password is correct.
        Return object User if correct, else return None
        """
        user = db.session.query(User).filter_by(email=email).first()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def get_current_user(http_authorization_credentials=Depends(reusable_oauth2)) -> list[UserDTO]:
        """
        Decode JWT token to get user_id => return User info from DB query
        """
        try:
            payload = jwt.decode(
                http_authorization_credentials.credentials, settings.SECRET_KEY,
                algorithms=[settings.SECURITY_ALGORITHM]
            )
            token_data = TokenPayload(**payload)
        except(jwt.PyJWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Could not validate credentials",
            )
        user, role = db.session.query(User, Role).join(Role, User.role_id == Role.id).filter(
            User.id == token_data.user_id).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.company_id:
            dto = UserDTO(
                id=user.id,
                full_name=user.full_name,
                user_name=user.user_name,
                email=user.email,
                phone_number=user.phone_number,
                role_name=role.role_name,
                role_description=role.description
            )
        else:
            dto = UserNormalDTO(
                id=user.id,
                company_id=user.company_id,
                full_name=user.full_name,
                user_name=user.user_name,
                email=user.email,
                phone_number=user.phone_number,
                role_name=role.role_name,
                role_description=role.description
            )
        return [dto]

    @staticmethod
    def register_user(data: Register, role_id: str, company_id: Optional[str]):
        if company_id:
            register_user = User(
                full_name=data.full_name,
                user_name=data.user_name,
                email=data.email,
                hashed_password=get_password_hash(data.password),
                phone_number=data.phone_number,
                role_id=role_id,
                company_id=company_id
            )
        else:
            register_user = User(
                full_name=data.full_name,
                user_name=data.user_name,
                email=data.email,
                hashed_password=get_password_hash(data.password),
                phone_number=data.phone_number,
                role_id=role_id,
            )
        db.session.add(register_user)
        db.session.commit()
        return register_user

    @staticmethod
    def change_password(email: str, current_password: str, new_password: str):
        user = db.session.query(User).filter_by(email=email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(current_password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect current password")

        user.password = get_password_hash(new_password)
        db.session.commit()

        return DataResponse().success_response([])

    @staticmethod
    def get_user_id_from_token(token: str) -> Optional[int]:
        """
        Decode JWT token to get user_id.
        """
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY,
                algorithms=[settings.SECURITY_ALGORITHM]
            )
            token_data = TokenPayload(**payload)
            return token_data.user_id
        except (jwt.PyJWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Could not validate credentials",
            )




