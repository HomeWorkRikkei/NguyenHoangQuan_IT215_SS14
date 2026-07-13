from sqlalchemy.orm import Session
from app.models.product_model import ProductModel
from app.schemas.product_schema import ProductCreate, ProductUpdate

def get_all_product(db: Session):
    ProductList = db.query(ProductModel).all()
    if not ProductList:
        return None
    return ProductList

def get_product_by_id(db: Session, product_id: int):
    ProductFounded = db.get(ProductModel,product_id)
    if not ProductFounded:
        return None
    return ProductFounded

def create_product(db: Session, product_data: ProductCreate):
    try:
        db_product = ProductModel(**product_data.model_dump())
        db.add(db_product)
        db.flush()
    except Exception as e:
        db.rollback()
        print(e)
        return None
    else:
        db.commit()
        return db_product
    
def update_product(db: Session, product_id: int, product_data: ProductUpdate):
    db_product = get_product_by_id(db=db,product_id=product_id)
    if db_product:
        for key, value in product_data.model_dump().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    else:
        return None
    return db_product

def delete_product(db: Session, product_id:int):
    db_product = get_product_by_id(db=db,product_id=product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return None
    return db_product