from flask import render_template, request, redirect
from app import dao, app, login
from flask_login import login_user, logout_user
import cloudinary.uploader
# from app import admin


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


@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ''
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):
            # upload cloudinary
            avatar=''
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                avatar = res['secure_url']

            # Lưu user
            try:
                dao.register(name=request.form['name'],
                             username=request.form['username'],
                             password=request.form['password'],
                             avatar=avatar)
            except:
                err_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'
            else:
                return redirect('/login')
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect('/')

    return render_template('login.html')


@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect('/login')


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
