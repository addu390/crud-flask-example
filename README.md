# Inventory Management - Flask Application

### Usage
- CRUD Operations of inventory.

### Set-up
```
pip install -r requirements.txt
export FLASK_APP=setup.py
flask db init
flask db migrate -m "Migrate Tables"
flask db upgrade
flask run --host=0.0.0.0 --port=80
```
Set `export FLASK_DEBUG=1` for auto-reload.

### Usage
- `Add` action button to add an item to the inventory with details such as Title, Description, and Quantity.
- After adding, `Edit` or `Delete` the item, where `Edit` is a simple update operation on allowed fields.
- `delete` in this context is a soft delete. Ensure to add a comment mentioning the reason for deletion. 
- After deleting, `undo` the deletion if necessary while keeping track of the delete/restore history; the deletion history record will now be updated to `RESTORED`

**Note:**
- The history is not limited to the inventory table or delete operation and is extendable for other operations and entities.
- The Inventory and History tables are always consistent, with "all-or-nothing" atomic transactions.
- At any given point, there can only be one `DELETED` record of an item and 1-or-more record of `RESTORED`.

