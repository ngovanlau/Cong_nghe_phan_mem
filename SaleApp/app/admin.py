from app.models import Category, Product
from app import db, app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True


class MyCategoryView(ModelView):
    column_list = ['id', 'name', 'products']


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name='Thống kê và báo cáo'))
