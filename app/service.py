from .constants import *
from .storage import InventoryDao, HistoryDao
from .dto import ItemDto, HistoryDto

inventory_dao = InventoryDao()
history_dao = HistoryDao()


class InventoryService:
    def get(self, id):
        return inventory_dao.get(id)

    def get_all(self):
        return inventory_dao.get_all()

    def add(self, item):
        inventory_dao.add(item)

    def update(self, id, item):
        inventory = inventory_dao.get(id)
        if inventory:
            inventory_dao.update(id, item)
        else:
            return error_response("Invalid item ID"), 400

    def delete(self, id, history):
        inventory_dao.delete(id, False)
        history_dao.add(history, True)

    def undo(self, id):
        inventory = inventory_dao.get(id)
        delete_histories = history_dao.get(INVENTORY, id, DELETED)

        if len(delete_histories) > 1:
            return error_response("Multiple delete histories"), 400
        delete_history = delete_histories[0]

        if inventory.get(STATUS) == DELETED:

            inventory_dao.update(id, ItemDto(status=ACTIVE), False)
            history_dao.update(delete_history.get('id'), HistoryDto(status=RESTORED), True)
        else:
            return error_response("Only deleted item can be restored"), 400


class HistoryService:
    def get_all(self):
        return history_dao.get_all()


def error_response(message):
    return {"error": message}
