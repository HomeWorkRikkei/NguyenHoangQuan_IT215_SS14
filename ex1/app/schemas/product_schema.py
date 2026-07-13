from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(max_length=50)
    price: float = Field(ge=0)

class ProductCreate(ProductBase): pass

class ProductUpdate(ProductBase): pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        from_attributes = True