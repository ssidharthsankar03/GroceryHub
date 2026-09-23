from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.role import Role
from app.models.user import User


EMAIL = "sidharth.test@example.com"


def make_admin() -> None:
    db = SessionLocal()

    try:
        user = db.scalar(
            select(User).where(User.email == EMAIL)
        )

        if user is None:
            raise ValueError(f"User not found: {EMAIL}")

        admin_role = db.scalar(
            select(Role).where(Role.name == "ADMIN")
        )

        if admin_role is None:
            raise ValueError("ADMIN role does not exist")

        if admin_role not in user.roles:
            user.roles.append(admin_role)
            db.commit()

        print(f"{EMAIL} is now an ADMIN.")


    finally:
        db.close()


if __name__ == "__main__":
    make_admin()