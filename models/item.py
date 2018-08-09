from db import db

class ItemModel(db.Model):      #Creates a mapping between the database and the objects
    __tablename__ = "items"     #We've to tell sqlalchemy the table name where these models will be saved.
    
    id = db.Column(db.Integer, primary_key=True)        #We've to tell it what columns the table will have cotain.
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {'name': self.name, 'price': self.price}
        
    @classmethod
    def find_by_name(cls, name):   
        return ItemModel.query.filter_by(name=name).first()   #The sql command is built into this, this return an ItemModel object.
            
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
        
        
        