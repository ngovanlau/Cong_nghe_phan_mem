import hashlib

from app.models import Category, Product, User
from app import app


def get_categories():
    return Category.query.all()


def get_products(kw, cate_id, page = None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))
    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size

        return products.slice(start, start + page_size)

    return products


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username), User.password.__eq__(password)).first()
