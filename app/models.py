from app import db


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    status = db.Column(db.String(50), nullable=False, default="ACTIVE")

    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    entity = db.Column(db.String(255), nullable=True, default="INVENTORY")
    entity_id = db.Column(db.Integer, nullable=False)

    operation = db.Column(db.String(255))

    status = db.Column(db.String(50), nullable=False, default="DELETED")

    comment = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
