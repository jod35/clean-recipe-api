from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


engine=create_engine('postgresql://postgres:nathanoj35@localhost/recipe',echo=False)

Base=declarative_base()

Session=sessionmaker(bind=engine)