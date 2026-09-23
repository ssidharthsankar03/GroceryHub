from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import require_role
from app.db.session import get_db
from app.models.user import User
from app.schemas.catalog import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from app.services.catalog_service import (
    create_category,
    delete_category,
    get_categories,
    get_category,
    update_category,
)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("ADMIN")),
):
    try:
        return create_category(db, category_data)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=list[CategoryResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return get_categories(db)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
def get_one(
    category_id: int,
    db: Session = Depends(get_db),
):
    category = get_category(db, category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


@router.patch(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update(
    category_id: int,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("ADMIN")),
):
    try:
        category = update_category(
            db,
            category_id,
            category_data,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )

    return category


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("ADMIN")),
):
    try:
        deleted = delete_category(db, category_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )