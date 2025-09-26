from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    stock_quantity: int = Field(ge=0, default=0)
    low_stock_threshold: int = Field(ge=0, default=10)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    low_stock_threshold: Optional[int] = Field(None, ge=0)

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True

class StockUpdate(BaseModel):
    quantity: int = Field(..., gt=0, description="Quantity to add/remove")