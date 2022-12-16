#!/usr/bin/env python

from sqlalchemy import *
import click
import os
import json
import logging
from datetime import datetime
from typing import *

DSN: str = os.environ.get("DSN", "postgresql://@localhost/game")
engine = create_engine(DSN)

debug_flag: bool = "DEBUG" in os.environ
logging.basicConfig()
loggingConfig = logging.getLogger('sqlalchemy.engine')
if debug_flag:
    loggingConfig.setLevel(logging.DEBUG)

@click.group()
def cli() -> None:
    pass

@cli.command()
@click.option("--name", "-n")
def put(name: str) -> None:
    writing(name) 

def writing(name: str) -> None:
    import uuid

    users = Table("users", MetaData(bind=engine), autoload=True)

    try:
        with engine.begin() as connection:
            user_id = str(uuid.uuid4())
            dt = datetime.now()
            r = {"user_id": user_id, "name": name, "created_at": dt, "updated_at":dt}
            connection.execute(users.insert(), r)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    cli()
