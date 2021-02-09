# flask_graphene_mongo/database.py
from mongoengine import connect
from models import Recipe, Ingredient

# You can connect to a real mongo server instance by your own.
connect("recipies", host="localhost", alias="default")


def init_db():
    # Create the fixtures
    milch = Ingredient(name="Milch", quantity=0.5, unit="l")
    milch.save()

    eier_mit_senf = Recipe(name="Eier mit Senfsauce", ingredients=[milch])
    eier_mit_senf.save()
