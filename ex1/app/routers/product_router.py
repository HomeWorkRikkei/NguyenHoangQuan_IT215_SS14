from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.product_service import get_all_product, get_product_by_id, create_product, update_product, delete_product
from app.database import get_db
from app.schemas.product_schema import ProductResponse, ProductCreate, ProductUpdate

router = APIRouter(
    prefix='/product_database'
)

@router.get('/products', tags=['Products'], response_model=list[ProductResponse])
def show_all_product(db: Session = Depends(get_db)):
    result = get_all_product(db=db)
    if not result:
        raise HTTPException(status_code=status.HTTP_200_OK, detail='danh sach rong')
    return result

@router.get('/product/{product_id}', tags=['Products'], response_model=ProductResponse)
def show_product_by_id(product_id: int, db: Session = Depends(get_db)):
    result = get_product_by_id(db=db, product_id=product_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='khong tim thay')
    return result

@router.post('/products', tags=['Products'], response_model=ProductResponse)
def add_product(product_data: ProductCreate, db: Session = Depends(get_db)):
    result = create_product(db=db, product_data=product_data)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='tao san pham that bai')
    return result

@router.put('/products/{product_id}',tags=['Products'], response_model=ProductResponse)
def eidt_product(product_data: ProductUpdate, product_id: int, db: Session = Depends(get_db)):
    result = update_product(db=db, product_data=product_data, product_id=product_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='khong tim thay san pham')
    return result

@router.delete('/products/{product_id}', tags=['Products'])
def remove_product(product_id: int, db: Session = Depends(get_db)):
    result = delete_product(db=db, product_id=product_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='khong tim thay san pham')
    return {
        'messsage': 'xoa thanh cong'
    }