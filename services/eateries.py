from flask import abort, make_response
from config import db
from models import Eatery, eatery_schema, eateries_schema


class SearchEatery():
    @classmethod
    def eatery_by_id(cls, id):
        eatery = Eatery.query.get(id)
        
        if eatery:
            return eatery_schema.dump(eatery)
        return None
    
    @classmethod
    def eatery_by_name(cls, name):
        name.lower()
        eatery = "%{}%".format(name)
        eatery = Eatery.query.filter(Eatery.eatery_name.ilike(eatery)).first()
        
        if eatery:
            return eatery_schema.dump(eatery)
        return None