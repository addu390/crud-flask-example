from flask import render_template, request, redirect
from app import app
from .constants import *
from .service import InventoryService, HistoryService
from .dto import ItemDto, HistoryDto
from flask_cors import CORS

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

inventory_service = InventoryService()
history_service = HistoryService()


@app.route('/')
@app.route('/index/<int:i_page>/<int:h_page>')
def index(i_page=1, h_page=1):
    inventories = inventory_service.get_page(i_page, OFFSET)
    histories = history_service.get_page(h_page, OFFSET)
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
