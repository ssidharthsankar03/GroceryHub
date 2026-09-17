from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.role import Role
from app.models.user import User
from app.schemas.auth import UserRegister
from app.core.security import create_access_token, hash_password, verify_password
from app.schemas.auth import TokenResponse, UserLogin, UserRegister


def register_user(db: Session, user_data: UserRegister) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == user_data.email)
    )

    if existing_user:
        raise ValueError("Email is already registered")

    existing_phone = db.scalar(
        select(User).where(User.phone_number == user_data.phone_number)
    )

    if existing_phone:
        raise ValueError("Phone number is already registered")

    customer_role = db.scalar(
        select(Role).where(Role.name == "CUSTOMER")
    )

    if not customer_role:
        raise ValueError("CUSTOMER role does not exist")

    user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        phone_number=user_data.phone_number,
        password_hash=hash_password(user_data.password),
    )

    user.roles.append(customer_role)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db: Session, login_data: UserLogin) -> TokenResponse:
    user = db.scalar(
        select(User).where(User.email == login_data.email)
    )

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(login_data.password, user.password_hash):
        raise ValueError("Invalid email or password")

    if not user.is_active:
        raise ValueError("User account is inactive")

    access_token = create_access_token(user.id)

    return TokenResponse(
        access_token=access_token,
    )