from datetime import datetime

from sqlalchemy import  DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.products import Product


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False,unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),    
    default=datetime.utcnow,
    nullable=False, 
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),    
    default=datetime.utcnow,
    onupdate=datetime.utcnow,
    nullable=False, 
    )
    products: Mapped[list["Product"]] = relationship(
    back_populates="category",
)