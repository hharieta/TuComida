from flask import abort, make_response
from config import db
from models import Saucer, saucer_schema, saucers_schema


class SearchSaucer():
    @classmethod
    def read_like(cls, tag):
        saucer = "%{}%".format(tag)
        posts = Saucer.query.filter(Saucer.saucer_name.ilike(saucer)).all()
        
        if posts: 
            return saucers_schema.dump(posts)
        return None