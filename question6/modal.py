from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///shopkeeper.sqlite"
db=SQLAlchemy(app)

'''
6. Write a flask application for inventory management of a computer accessories store. 
A store wants to have an inventory management application where the owner/store manager can login and see inventory of the store.
As a manager of the store, I should be able to see name of the accessory, quantities ordered, quantities remaining, vendor name, purchase price per item, selling price per item, date and time when the item was added, date and time when the item was updated. 
I should also be able to add a new accessory, update existing accessory and delete an accessory. 
Also a new manager should be able to register/login in the app. 
'''
'''
I forget about how to add the date in database so that is why i am writing modal and logic thing
'''


class shopstatus:
    def __init__(self,status_code,message,itemobj):
        self.status_code=status_code
        self.message=message
        self.itemobj=itemobj

    
class Shop(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    quantity=db.Column(db.Integer)
    rem_quantity=db.Column(db.Integer)
    ven_name=db.Column(db.String())
    p_price=db.Column(db.Integer)
    s_price=db.Column(db.Integer)
    ad_date=db.Column(db.DateTime) #i forget about the datatype of date
    up_date=db.Column(db.DateTime)

    def __init__(self,name,quantity,rem_quantity,ven_name,p_price,s_price):

        self.name=name
        self.quantity=quantity
        self.rem_quantity=rem_quantity
        self.ven_name=ven_name
        self.p_price=p_price
        self.s_price=s_price
        # self.ad_date=ad_date
        # self.up_date=up_date
    
    def __repr__(self):
        return f"{self.name}=={self.quantity}=={self.rem_quantity}=={self.ven_name}=={self.p_price}=={self.s_price}=={self.ad_date}=={self.up_date}"
    


with app.app_context():
    db.create_all()


app.run(debug=True)
        