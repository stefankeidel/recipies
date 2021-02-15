import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from models import Recipe
from object_types import RecipeType
#from .mutations import CreateBikeMutation, UpdateBikeMutation, DeleteBikeMutation


# class Mutations(graphene.ObjectType):
#     create_bike = CreateBikeMutation.Field()
#     update_bike = UpdateBikeMutation.Field()
#     delete_bike = DeleteBikeMutation.Field()


class Query(graphene.ObjectType):
    node = Node.Field()
    recipies = MongoengineConnectionField(RecipeType)

schema = graphene.Schema(query=Query, types=[RecipeType])
