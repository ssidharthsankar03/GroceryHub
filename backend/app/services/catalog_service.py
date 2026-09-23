from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.models.category import Category
from app.schemas.catalog import (
    BrandCreate,
    BrandUpdate,
    CategoryCreate,
    CategoryUpdate,
)
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
    return db.scalar(select(Category).where(Category.id == category_id))


def get_categories(
    db: Session,
) -> list[Category]:
    return list(db.scalars(select(Category).order_by(Category.id)).all())


def update_category(
    db: Session,
    category_id: int,
    category_data: CategoryUpdate,
) -> Category | None:
    category = get_category(db, category_id)

    if category is None:
        return None

    update_data = category_data.model_dump(exclude_unset=True)

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


def create_brand(db: Session, brand_data: BrandCreate) -> Brand:
    existing_brand = db.scalar(select(Brand).where(Brand.name == brand_data.name))

    if existing_brand:
        raise ValueError("Brand already exists")

    brand = Brand(
        name=brand_data.name,
        description=brand_data.description,
    )

    db.add(brand)
    db.commit()
    db.refresh(brand)

    return brand


def get_brand(db: Session, brand_id: int) -> Brand | None:
    return db.scalar(select(Brand).where(Brand.id == brand_id))


def get_brands(db: Session) -> list[Brand]:
    return list(db.scalars(select(Brand).order_by(Brand.id)).all())


def update_brand(
    db: Session,
    brand_id: int,
    brand_data: BrandUpdate,
) -> Brand | None:
    brand = get_brand(db, brand_id)

    if brand is None:
        return None

    update_data = brand_data.model_dump(exclude_unset=True)

    if "name" in update_data:
        existing_brand = db.scalar(
            select(Brand).where(
                Brand.name == update_data["name"],
                Brand.id != brand_id,
            )
        )

        if existing_brand:
            raise ValueError("Brand already exists")

    for field, value in update_data.items():
        setattr(brand, field, value)

    db.commit()
    db.refresh(brand)

    return brand


def delete_brand(db: Session, brand_id: int) -> bool:
    brand = get_brand(db, brand_id)

    if brand is None:
        return False

    db.delete(brand)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise ValueError(
            "Cannot delete brand because products are assigned to it"
        ) from exc

    return True
