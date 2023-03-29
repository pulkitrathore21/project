'''
i forget about how to write the date in database so that is why i am writing the logics and other things
'''
from flask import request
from modal import app,Shop
from logic import ShopDb


@app.route("/addintodb",methods=["POST"])
def post():
    id=request.json["id"]
    name=request.json["name"]
    quantity=request.json["quantity"]
    rem_quantity=request.json["rem_quantity"]
    ven_name=request.json["ven_name"]
    p_price=request.json["p_price"]
    s_price=request.json["s_price"]
    ad_date=request.json["ad_date"]
    up_date=request.json["up_date"]
    itemobj=Shop(id,name,quantity,rem_quantity,ven_name,p_price,s_price,ad_date,up_date)
    sendtologic=ShopDb.addItem(itemobj)
    return f"{sendtologic.status_code},{sendtologic.message},{sendtologic.itemobj}"



@app.route("/getdata",methods=["GET"])
def get():
    fetchdb=ShopDb.fetchitem()
    return f"{fetchdb.status_code},{fetchdb.message},{fetchdb.itemobj}"
    

@app.route("/delete/<int:id>",methods=["GET"])
def delete(id):
    
    sendtdelt=ShopDb.deleteitem(id)
    return f"{sendtdelt.status_code},{sendtdelt.message},{sendtdelt.itemobj}"
    

@app.route("/update/",methods=["GET"])
def update():
    id=request.json["id"]
    name=request.json["name"]
    quantity=request.json["quantity"]
    rem_quantity=request.json["rem_quantity"]
    ven_name=request.json["ven_name"]
    p_price=request.json["p_price"]
    s_price=request.json["s_price"]
    ad_date=request.json["ad_date"]
    up_date=request.json["up_date"]
    itemobj=Shop(id,name,quantity,rem_quantity,ven_name,p_price,s_price,ad_date,up_date)

    return f"{itemobj.status_code},{itemobj.message},{itemobj.itemitemobj}"
