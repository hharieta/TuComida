from config import db, ma

class Eatery(db.Model):
    __tablename__ = "eatery"
    id_eatery = db.Column(db.Integer, primary_key=True, autoincrement=True)
    eatery_name = db.Column(db.String(20), nullable=False)
    cuisine = db.Column(db.String(20), nullable=False)
    url_image = db.Column(db.String(300), nullable=False)
    url_maps = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String)
    phone = db.Column(db.String(20))
    description = db.Column(db.String)

    __table_args__ = (
        db.Index('idx_eatery_name', "eatery_name"),
    )

class EaterySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Eatery
        load_instance = True
        sql_session = db.session

eatery_schema = EaterySchema()
eateries_schema = EaterySchema(many=True)