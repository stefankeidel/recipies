import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Recipe as RecipeModel
from models import Ingredient as IngredientModel


class Recipe(MongoengineObjectType):
    class Meta:
        model = RecipeModel
        interfaces = (Node,)


class Ingredient(MongoengineObjectType):
    class Meta:
        model = IngredientModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_recipies = MongoengineConnectionField(Recipe)


schema = graphene.Schema(query=Query, types=[Recipe, Ingredient])
