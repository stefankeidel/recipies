from datetime import datetime
from mongoengine import Document, CASCADE
from mongoengine.fields import DateTimeField, ReferenceField, StringField, FloatField, ListField

class Ingredient(Document):
    units = ["tbsp", "tsp", 'l']
    name = StringField(max_length=512, required=True)
    quantity = FloatField(required=True)
    unit = StringField(max_length=10, choices=units, required=True)

class Recipe(Document):
    meta = {"allow_inheritance": True}
    name = StringField(max_length=255, required=True)
    ingredients = ListField(ReferenceField(Ingredient))
