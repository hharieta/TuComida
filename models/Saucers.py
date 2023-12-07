from config import db, ma
from marshmallow_sqlalchemy import fields
from .Eatery import Eatery, EaterySchema

class Saucer(db.Model):
    __tablename__ = 'saucers'
    id_saucer = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_eatery = db.Column(db.Integer, db.ForeignKey('eatery.id_eatery'), nullable=False)
    saucer_name = db.Column(db.String(30), nullable=False, index=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    url_image = db.Column(db.String(255))
    eatery = db.relationship('Eatery', foreign_keys=[id_eatery])
    __table_args__ = (
        db.UniqueConstraint('id_eatery', 'saucer_name', name='uq_saucer_name_per_eatery'),
        db.Index('idx_saucer_name', "saucer_name"),
        )

    
class SaucerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Saucer
        load_instance = True
        sql_session = db.session
    
    eatery = fields.Nested(EaterySchema, only=('id_eatery', 'eatery', 'cuisine'))

saucer_schema = SaucerSchema()
saucers_schema = SaucerSchema(many=True)
