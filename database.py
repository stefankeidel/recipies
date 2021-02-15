# flask_graphene_mongo/database.py
from mongoengine import connect
from models import Recipe, Ingredient

connect("recipies", host="localhost", alias="default")


def init_db():
    # Create some fixtures
    milch = Ingredient(name="Milch", quantity=0.5, unit="l")
    senf = Ingredient(name="Senf", quantity=2, unit="tsp")
    #milch.save()

    eier_mit_senf = Recipe(name="Eier mit Senfsauce", ingredients=[milch, senf])
    eier_mit_senf.save()
