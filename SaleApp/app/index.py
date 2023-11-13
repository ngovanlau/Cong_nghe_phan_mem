from flask import render_template, request
import dao
from app import app, login


@app.route("/")
def home():
    kw = request.args.get('kw')

    cate = dao.get_categories()
    pro = dao.get_products(kw)
    return render_template('index.html', categories = cate, products = pro)


#Path param
@app.route("/hello/<name>")
def hello(name):
    return render_template('index.html', message="XIN CHAO %s!!!" % name)


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == "__main__":
    from app import admin
    app.run(debug=True)