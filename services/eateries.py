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