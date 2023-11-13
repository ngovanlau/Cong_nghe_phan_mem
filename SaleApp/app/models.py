from sqlalchemy import Integer, Column, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')


    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    products = relationship('Product', backref='category', lazy=True)


    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()
        #
        # p1 = Product(name='iPhone 13', price=20000000, category_id=1)
        # p2 = Product(name='Galaxy S23', price=24999999, category_id=1)
        # p3 = Product(name='Ipad', price=45300000, category_id=2)
        # p4 = Product(name='MSI', price=32300000, category_id=3)
        # p5 = Product(name='Oppo N3 Flip', price=20333000, category_id=1)
        # p6 = Product(name='Galaxy Tab', price=1203000, category_id=2)
        # db.session.add(p1)
        # db.session.add(p2)
        # db.session.add(p3)
        # db.session.add(p4)
        # db.session.add(p5)
        # db.session.add(p6)
        # db.session.commit()