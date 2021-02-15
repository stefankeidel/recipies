# from datetime import datetime
# from mongoengine import Document, EmbeddedDocument, CASCADE
# from mongoengine.fields import DateTimeField, EmbeddedDocumentField, StringField, FloatField, ListField

# class Ingredient(EmbeddedDocument):
#     units = ["tbsp", "tsp", 'l']
#     name = StringField(max_length=512, required=True)
#     quantity = FloatField(required=True)
#     unit = StringField(max_length=10, choices=units, required=True)

# class Recipe(Document):
#     meta = {"allow_inheritance": True, "collection": "recipe"}
#     name = StringField(max_length=255, required=True)
#     ingredients = ListField(EmbeddedDocumentField(Ingredient))

from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
    DictField
)

class Recipe(Document):
    meta = {"collection": "recipe"}
    name = StringField(max_length=255, required=True)
    ingredients = ListField(DictField())
