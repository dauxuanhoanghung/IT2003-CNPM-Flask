from flask import render_template, request
from app import dao
from app import app


@app.route('/')
def index():
    categories = dao.load_categories()
    cate_id = request.args.get('category_id')
    keyword = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    products = dao.load_products(category_id=cate_id, kw=keyword, from_price=from_price, to_price=to_price)
    return render_template('index.html', categories=categories,
                           products=products)


if __name__ == '__main__':
    app.run(debug=True)
