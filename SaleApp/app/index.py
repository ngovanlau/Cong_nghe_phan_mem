from flask import Flask, render_template, request
import dao


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)