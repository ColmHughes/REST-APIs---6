from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "colm"
api = Api(app)




jwt = JWT(app, authenticate, identity) #JWT class creates a new endpoint /auth, when we call /auth we send it a username and password that is used in authenticate and identity.




api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":  #This is so if we do a from app import in another file it doesn't run the app. It will only run if we run app.py. 
                            #When python runs a file it assigns a name to it and that name is __main__   
    from db import db
    db.init_app(app)
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=True)