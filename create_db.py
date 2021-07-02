from app.models.database import Base,engine
from app.models.recipes import User,Recipe

print("Creating the database ....")
Base.metadata.create_all(engine)
print("Database created !")