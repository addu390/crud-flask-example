from flask import render_template, request, redirect
from app import app
from .constants import *
from .service import InventoryService, HistoryService
from .dto import ItemDto, HistoryDto

inventory_service = InventoryService()
history_service = HistoryService()


@app.route('/')
@app.route('/index')
def index():
    inventories = inventory_service.get_all()
    histories = history_service.get_all()
    return render_template('index.html', inventories=inventories, histories=histories)


@app.route('/update/<int:id>')
def updateRoute(id):
    inventory = inventory_service.get(id)
    return render_template('update.html', inventory=inventory)


@app.route('/delete/<int:id>')
def deleteRoute(id):
    inventory = inventory_service.get(id)
    return render_template('delete.html', inventory=inventory)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        item = ItemDto(title=form.get(TITLE), description=form.get(DESCRIPTION), quantity=int(form.get(QUANTITY)))
        inventory_service.add(item)
    return redirect('/')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    item = ItemDto(title=form.get(TITLE), description=form.get(DESCRIPTION), quantity=int(form.get(QUANTITY)))
    inventory_service.update(id, item)
    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        history = HistoryDto(comment=request.form.get(COMMENT), entity_id=id, operation=DELETE)
        inventory_service.delete(id, history)
    return redirect('/')


@app.route('/undo/<int:id>')
def undo(id):
    inventory_service.undo(id)
    return redirect('/')
