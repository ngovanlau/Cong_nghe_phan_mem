from flask import render_template, request, redirect, jsonify, session
import dao, utils
from app import app, login
from flask_login import login_user


@app.route("/")
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    cate = dao.get_categories()
    pro = dao.get_products(kw, cate_id, page)
    return render_template('index.html', products=pro)


@app.route("/cart")
def cart():
    return render_template('cart.html')


@app.context_processor
def common_respones():
    return {
        'categories': dao.get_categories(),
        'cart_stats': utils.count_cart(session.get('cart'))
    }


# Path param
@app.route("/hello/<name>")
def hello(name):
    return render_template('index.html', message="XIN CHAO %s!!!" % name)


@app.route("/api/cart", methods=['post'])
def add_to_cart():
    data = request.json

    cart = session.get('cart')
    if cart is None:
        cart = {}

    id = str(data.get('id'))

    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            "id": id,
            "name": data.get('name'),
            "price": data.get('price'),
            "quantity": 1
        }

    session['cart'] = cart
    print(cart)
    """
        {
            "1": {
                "id": "1",
                "name": "...",
                "price": 1,
                "quantity": 2
            }, 
            "2": {
                "id": "2",
                "name": "...",
                "price": 1,
                "quantity": 1
            },
        }
    """

    return jsonify(utils.count_cart(cart))


@app.route("/api/cart/<product_id>", methods=['put'])
def update_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        quantity = request.json.get('quantity')
        cart[product_id]['quantity'] = int(quantity)

    session['cart'] = cart
    return jsonify(utils.count_cart(cart))


@app.route("/api/cart/<product_id>", methods=['delete'])
def delete_cart(product_id):
    cart = session.get('cart')
    if cart and product_id in cart:
        del cart[product_id]

    session['cart'] = cart
    return jsonify(utils.count_cart(cart))


@app.route("/admin/login", methods=['post'])
def login_admin():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user)

    return redirect('/admin')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == "__main__":
    from app import admin

    app.run(debug=True)
