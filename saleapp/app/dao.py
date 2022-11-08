from app.models import Category, Product, User
from app import db
import hashlib


def load_categories():
    return Category.query.all()
    # with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
    #     return json.load(f)


def load_products(category_id=None, kw=None, from_price=None, to_price=None):
    # with open('%s/data/products.json' % app.root_path, encoding='utf-8') as f:
    #     products = json.load(f)
    query = Product.query

    if category_id:
        query = query.filter(Product.category_id == category_id)

    if kw:
        query = query.filter(Product.name.contains(kw))

    if from_price:
        query = query.filter(Product.price >= float(from_price))

    if to_price:
        query = query.filter(Product.price <= float(to_price))

    return query.all()


def get_product_by_id(product_id: int):
    return Product.query.get(product_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).digest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()


def register(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()


def get_user_by_id(user_id):
    return User.query.get(user_id)
