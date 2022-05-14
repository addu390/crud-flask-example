from flask import render_template, request, redirect
from app import app, db
from app.models import Inventory, History


@app.route('/')
@app.route('/index')
def index():
    inventories = Inventory.query.all()
    histories = History.query.all()
    return render_template('index.html', inventories=inventories, histories=histories)


@app.route('/update/<int:id>')
def updateRoute(id):
    inventory = Inventory.query.get(id)
    return render_template('update.html', inventory=inventory)


@app.route('/delete/<int:id>')
def deleteRoute(id):
    inventory = Inventory.query.get(id)
    return render_template('delete.html', inventory=inventory)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        inventory = Inventory(title=title, description=description)
        db.session.add(inventory)
        db.session.commit()
    return redirect('/')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    inventory = Inventory.query.get(id)
    if inventory:
        form = request.form
        inventory.title = form.get('title')
        inventory.description = form.get('description')
        db.session.add(inventory)
        db.session.commit()
    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if request.method == 'POST':
        form = request.form

        inventory = Inventory.query.get(id)
        inventory.status = "DELETED"
        db.session.add(inventory)

        comment = form.get('comment')
        delete_history = History(comment=comment, entity_id=id, operation="DELETE")
        db.session.add(delete_history)
        db.session.commit()
    return redirect('/')


@app.route('/undo/<int:id>')
def undo(id):
    inventory = Inventory.query.get(id)
    delete_histories = History.query.filter_by(entity="INVENTORY", entity_id=id, status="DELETED").all()

    if len(delete_histories) > 1:
        return "Multiple delete histories", 400
    delete_history = delete_histories[0]

    if inventory.status == "DELETED":

        inventory.status = "ACTIVE"
        delete_history.status = "RESTORED"

        db.session.add(inventory)
        db.session.add(delete_history)

        db.session.commit()
    return redirect('/')
