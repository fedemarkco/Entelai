from .. import db


class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    options = db.relationship("Option", backref="node", lazy=True,
                              foreign_keys="Option.node_id")


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.Integer, db.ForeignKey("node.id"), nullable=False)
    next_node_id = db.Column(db.Integer, db.ForeignKey("node.id"))
    option_description = db.Column(db.String(255))
    next_node = db.relationship("Node", foreign_keys=[next_node_id])
