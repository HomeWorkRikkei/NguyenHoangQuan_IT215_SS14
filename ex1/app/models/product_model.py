from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from app.database import Base

class ProductModel(Base):
    __tablename__ = 'Products'

    id: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float)