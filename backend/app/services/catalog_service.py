from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.catalog import CategoryCreate, CategoryUpdate
from sqlalchemy.exc import IntegrityError

def create_category(
    db: Session,
    category_data: CategoryCreate,
) -> Category:
    existing_category = db.scalar(
        select(Category).where(Category.name == category_data.name)
    )

    if existing_category:
        raise ValueError("Category already exists")

    category = Category(
        name=category_data.name,
        description=category_data.description,
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_category(
    db: Session,
    category_id: int,
) -> Category | None:
    return db.scalar(
        select(Category).where(Category.id == category_id)
    )


def get_categories(
    db: Session,
) -> list[Category]:
    return list(
        db.scalars(
            select(Category).order_by(Category.id)
        ).all()
    )


def update_category(
    db: Session,
    category_id: int,
    category_data: CategoryUpdate,
) -> Category | None:
    category = get_category(db, category_id)

    if category is None:
        return None

    update_data = category_data.model_dump(
        exclude_unset=True
    )

    if "name" in update_data:
        existing_category = db.scalar(
            select(Category).where(
                Category.name == update_data["name"],
                Category.id != category_id,
            )
        )

        if existing_category:
            raise ValueError("Category already exists")

    for field, value in update_data.items():
        setattr(category, field, value)

    db.commit()
    db.refresh(category)

    return category


def delete_category(
    db: Session,
    category_id: int,
) -> bool:
    category = get_category(db, category_id)

    if category is None:
        return False

    db.delete(category)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise ValueError(
            "Cannot delete category because products are assigned to it"
        ) from exc

    return True