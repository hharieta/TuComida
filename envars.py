import os
from dotenv import load_dotenv

load_dotenv()


vars = {
        "POSTGRES_USERNAME" : os.environ["PS_USER"],
        "POSTGRES_PASSWORD" : os.environ["PS_PASSWORD"],
        "POSTGRES_HOST" : os.environ["PS_HOST"],
        "POSTGRES_DBNAME" : os.environ["PS_DBNAME"],
        "POSTGRES_PORT" : os.environ["PS_PORT"],
    }
