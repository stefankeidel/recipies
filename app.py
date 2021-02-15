#from database import init_db
from fixtures import fixtures_data
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from mongoengine import connect

connect("recipies", host="mongo", alias="default")

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    fixtures_data()
    app.run()
