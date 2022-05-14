from flask import render_template, request, redirect
from app import app, db
from app.models import Inventory, History
from .constants import *
from .storage import InventoryDao, HistoryDao
from .dto import ItemDto, HistoryDto

inventory_dao = InventoryDao()
history_dao = HistoryDao()


@app.route('/')
@app.route('/index')
def index():
    inventories = inventory_dao.get_all()
    histories = history_dao.get_all()
    return render_template('index.html', inventories=inventories, histories=histories)


@app.route('/update/<int:id>')
def updateRoute(id):
    inventory = inventory_dao.get(id)
    return render_template('update.html', inventory=inventory)


@app.route('/delete/<int:id>')
def deleteRoute(id):
    inventory = inventory_dao.get(id)
    return render_template('delete.html', inventory=inventory)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form

        item = ItemDto(title=form.get(TITLE), description=form.get(DESCRIPTION), quantity=int(form.get(QUANTITY)))
        inventory_dao.add(item)
    return redirect('/')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    inventory = inventory_dao.get(id)
    if inventory:
        form = request.form
        item = ItemDto(title=form.get(TITLE), description=form.get(DESCRIPTION), quantity=int(form.get(QUANTITY)))
        inventory_dao.update(id, item)
    else:
        return error_response("Invalid item ID"), 400
    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        form = request.form

        inventory_dao.delete(id, False)

        history = HistoryDto(comment=form.get(COMMENT), entity_id=id, operation=DELETE)
        history_dao.add(history, True)
    return redirect('/')


@app.route('/undo/<int:id>')
def undo(id):
    inventory = inventory_dao.get(id)
    print(inventory)
    delete_histories = History.query.filter_by(entity=INVENTORY, entity_id=id, status=DELETED).all()

    if len(delete_histories) > 1:
        return error_response("Multiple delete histories"), 400
    delete_history = delete_histories[0]

    if inventory.get('status') == DELETED:

        inventory_dao.update(id, ItemDto(status=ACTIVE), False)
        history_dao.update(delete_history.id, HistoryDto(status=RESTORED), True)
    else:
        return error_response("Only deleted item can be restored"), 400
    return redirect('/')


def error_response(message):
    return {"error": message}
