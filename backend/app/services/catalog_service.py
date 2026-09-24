from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.models.category import Category
from app.models.products import Product
from app.schemas.catalog import (
    BrandCreate,
    BrandUpdate,
    CategoryCreate,
    CategoryUpdate,
    ProductCreate,
    ProductUpdate,
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

def create_product(
    db: Session,
    product_data: ProductCreate,
) -> Product:
    category = db.scalar(
        select(Category).where(
            Category.id == product_data.category_id
        )
    )

    if category is None:
        raise ValueError("Category not found")

    brand = db.scalar(
        select(Brand).where(
            Brand.id == product_data.brand_id
        )
    )

    if brand is None:
        raise ValueError("Brand not found")

    product = Product(
        name=product_data.name,
        description=product_data.description,
        category_id=product_data.category_id,
        brand_id=product_data.brand_id,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_product(
    db: Session,
    product_id: int,
) -> Product | None:
    return db.scalar(
        select(Product).where(
            Product.id == product_id
        )
    )


def get_products(db: Session) -> list[Product]:
    return list(
        db.scalars(
            select(Product).order_by(Product.id)
        ).all()
    )


def update_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate,
) -> Product | None:
    product = get_product(db, product_id)

    if product is None:
        return None

    update_data = product_data.model_dump(
        exclude_unset=True
    )

    if "category_id" in update_data:
        category = db.scalar(
            select(Category).where(
                Category.id == update_data["category_id"]
            )
        )

        if category is None:
            raise ValueError("Category not found")

    if "brand_id" in update_data:
        brand = db.scalar(
            select(Brand).where(
                Brand.id == update_data["brand_id"]
            )
        )

        if brand is None:
            raise ValueError("Brand not found")

    for field, value in update_data.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    db: Session,
    product_id: int,
) -> bool:
    product = get_product(db, product_id)

    if product is None:
        return False

    db.delete(product)
    db.commit()

    return True