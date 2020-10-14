from flask import Blueprint, render_template
from flask_login import login_required
from app.models import db, Table, MenuItem, Order
from sqlalchemy.orm import joinedload
from app.forms import OrderForm

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    tables = list(Table.query.options(joinedload(Table.orders)).all())
    menu_items = list(MenuItem.query.options(joinedload(MenuItem.type)).all())
    form = OrderForm()
    return render_template("orders.html", tables=tables, menu=menu_items, form=form)

@bp.route("/table/<int:id>", methods=['POST', 'DELETE'])
@login_required
def table(id):
    form = OrderForm()
    if form.validate_on_submit():
        french_fries = form.french_fries.data
        dr_pepper = form.dr_pepper.data
        jambalaya = form.jambalaya.data
        order = Order.query.filter(Order.table_id==id).all()
        if order:
            pass
        else:
            order = Order() 
    return render_template("orders.html")

