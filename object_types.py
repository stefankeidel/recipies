from graphene import relay
from graphene_mongo import MongoengineObjectType
from models import Recipe


class RecipeType(MongoengineObjectType):
    class Meta:
        model = Recipe
        interfaces = (relay.Node,)
