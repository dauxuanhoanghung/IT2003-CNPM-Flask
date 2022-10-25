import json
from app import app
from app.models import Category, Product

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