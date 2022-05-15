DESCRIPTION = "description"
TITLE = "title"
QUANTITY = "quantity"
COMMENT = "comment"
STATUS = "status"

ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"
INVENTORY_STATUS = (
    (ACTIVE, "Active"),
    (INACTIVE, "Inactive"),
)

INVENTORY = "INVENTORY"
HISTORY_ENTITY = (
    (INVENTORY, "Inventory")
)

DELETED = "DELETED"
RESTORED = "RESTORED"
HISTORY_STATUS = (
    (DELETED, "Deleted"),
    (RESTORED, "Restored"),
)

DELETE = "DELETE"
OPERATIONS = (
    (DELETE, "Delete")
)
