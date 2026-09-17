from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.role import Role
from app.models.user import User

DEFAULT_ROLES = [
    ("CUSTOMER", "Regular grocery customer"),
    ("ADMIN", "Full system administrator"),
    ("STAFF", "Shop staff member"),
    ("DELIVERY", "Delivery personnel"),
]


def seed_roles() -> None:
    db = SessionLocal()

    try:
        for name, description in DEFAULT_ROLES:
            existing_role = db.scalar(
                select(Role).where(Role.name == name)
            )

            if existing_role:
                continue

            db.add(
                Role(
                    name=name,
                    description=description,
                )
            )

        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    seed_roles()
    print("Roles seeded successfully.")