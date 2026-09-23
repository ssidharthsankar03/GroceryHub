from datetime import datetime

from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    is_active: bool | None = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
    
class BrandCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)


class BrandUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    is_active: bool | None = None


class BrandResponse(BaseModel):
    id: int
    name: str
    description: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=200)
    description: str | None = None
    category_id: int
    brand_id: int


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=200)
    description: str | None = None
    category_id: int | None = None
    brand_id: int | None = None
    is_active: bool | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    category_id: int
    brand_id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }