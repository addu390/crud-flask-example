from app.models import Inventory, History
from app import db
from .constants import DELETED


class InventoryDao:
    def get(self, id):
        inventory = Inventory.query.get(id)
        return Inventory.serialize(inventory)

    def get_all(self):
        inventories = [Inventory.serialize(inventory) for inventory in Inventory.query.all()]
        return inventories

    def add(self, item, commit=True):
        inventory = Inventory(title=item.title, description=item.description, quantity=item.quantity)
        db.session.add(inventory)
        if commit:
            db.session.commit()

    def update(self, id, item, commit=True):
        inventory = Inventory.query.get(id)

        if item.title:
            inventory.title = item.title
        if item.description:
            inventory.description = item.description
        if item.quantity:
            inventory.quantity = item.quantity
        if item.status:
            inventory.status = item.status

        db.session.add(inventory)
        if commit:
            db.session.commit()

    def delete(self, id, commit=True):
        inventory = Inventory.query.get(id)
        inventory.status = DELETED
        db.session.add(inventory)
        if commit:
            db.session.commit()


class HistoryDao:
    def get_all(self):
        histories = [History.serialize(history) for history in History.query.all()]
        return histories

    def get(self, entity, entity_id, status):
        histories = [History.serialize(history) for history in
                     History.query.filter_by(entity=entity, entity_id=entity_id, status=status).all()]
        return histories

    def add(self, history, commit=True):
        history_entity = History(comment=history.comment, entity_id=history.entity_id, operation=history.operation)
        db.session.add(history_entity)
        if commit:
            db.session.commit()

    def update(self, id, history, commit=True):
        history_entity = History.query.get(id)

        if history.operation:
            history_entity.operation = history.operation

        if history.status:
            history_entity.status = history.status

        db.session.add(history_entity)
        if commit:
            db.session.commit()

