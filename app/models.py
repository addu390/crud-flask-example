from app import db
from .constants import ACTIVE, INVENTORY, DELETED


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)

    status = db.Column(db.String(50), nullable=False, default=ACTIVE)

    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'quantity': self.quantity,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    entity = db.Column(db.String(255), nullable=True, default=INVENTORY)
    entity_id = db.Column(db.Integer, nullable=False)

    operation = db.Column(db.String(255))

    status = db.Column(db.String(50), nullable=False, default=DELETED)

    comment = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())

    def serialize(self):
        return {
            'id': self.id,
            'entity': self.entity,
            'entity_id': self.entity_id,
            'operation': self.operation,
            'status': self.status,
            'comment': self.comment,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
