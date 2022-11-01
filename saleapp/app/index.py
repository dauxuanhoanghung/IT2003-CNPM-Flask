from flask import render_template, request, redirect
from app import dao, app, admin, login
from flask_login import login_user


@app.route('/')
def index():
    cate_id = request.args.get('category_id')
    keyword = request.args.get('keyword')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    products = dao.load_products(category_id=cate_id, kw=keyword, from_price=from_price, to_price=to_price)
    return render_template('index.html', products=products)


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    p = dao.get_product_by_id(product_id)
    return render_template('details.html', product=p)


@app.context_processor
def common_data():
    categories = dao.load_categories()
    return {
        'categories': categories
    }


@app.route('/login-admin', methods=['post'])
def login_admin():
    username = request.form['username']
    password = request.form['password']

    u = dao.auth_user(username=username, password=password)
    if u:
        login_user(user=u, force=True)

    return redirect('/admin')


@login.user_loader
def user_load(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
