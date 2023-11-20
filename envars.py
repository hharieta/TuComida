import os
from typing import Dict


def get_envars() -> Dict[str, str]:

    env_vars = {
        "POSTGRES_USERNAME" : os.environ['POSTGRES_USERNAME'],
        "POSTGRES_PASSWORD" : os.environ['POSTGRES_PASSWORD'],
        "POSTGRES_HOST" : os.environ['POSTGRES_HOST'],
        "POSTGRES_DBNAME" : os.environ['POSTGRES_DBNAME'],
        "POSTGRES_PORT" : os.environ['POSTGRES_PORT'],
    }
    
    return env_vars


print(get_envars())