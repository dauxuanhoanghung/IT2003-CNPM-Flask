from sqlalchemy import Column, Integer, Float, Boolean, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(150))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        # c1 = Category(name='Điện thoại')
        # c2 = Category(name='Máy tính bảng')
        # c3 = Category(name='Phụ kiện')
        # 
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # 
        # db.session.commit()
        p1 = Product(name="iPhone 14 Plus",
                     description="Apple, 256GB, RAM: 6GB, iOS16",
                     price=28990000,
                     image="https://m.media-amazon.com/images/I/61YSNhAb00L._SL1500_.jpg",
                     category_id=1)
        p2 = Product(name="iPad Pro 2020",
                     description="Apple, 128GB, RAM: 6GB",
                     price=37000000,
                     image=
                     "https://cdn.tgdd.vn/Products/Images/522/238645/ipad-pro-m1-129-inch-wifi-sliver-600x600.jpg",
                     category_id=2)
        p3 = Product(name="Galaxy S22 Ultra 5G",
                     description="Samsung, 128GB, RAM: 8GB",
                     price=25990000,
                     image=
                     "https://cdn.tgdd.vn/Products/Images/42/271697/Galaxy-S22-Ultra-Green-600x600.jpg",
                     category_id=1)
        p4 = Product(name="iPhone 14 Plus",
                     description="Apple, 256GB, RAM: 6GB, iOS16",
                     price=28990000,
                     image=
                     "https://m.media-amazon.com/images/I/61YSNhAb00L._SL1500_.jpg",
                     category_id=1)
        p5 = Product(name="iPad Pro 2020",
                     description="Apple, 128GB, RAM: 6GB",
                     price=37000000,
                     image=
                     "https://cdn.tgdd.vn/Products/Images/522/238645/ipad-pro-m1-129-inch-wifi-sliver-600x600.jpg",
                     category_id=2)
        p6 = Product(name="Galaxy S22 Ultra 5G",
                     description="Samsung, 128GB, RAM: 8GB",
                     price=25990000,
                     image=
                     "https://cdn.tgdd.vn/Products/Images/42/271697/Galaxy-S22-Ultra-Green-600x600.jpg",
                     category_id=1)

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)

        db.session.commit()
