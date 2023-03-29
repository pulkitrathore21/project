from modal import Shop,db,shopstatus
from datetime import datetime
'''
 self.name=name
        self.quantity=quantity
        self.rem_quantity=rem_quantity
        self.ven_name=ven_name
        self.p_price=p_price
        self.s_price=s_price
        self.ad_date=ad_date
        self.up_date=up_date
'''
class ShopDb:
    def addItem(itemobj): # for adding my object into database
        print(itemobj)
        itemstatus=shopstatus(0,"added failed",None)
        '''
          if my object is not addedd successfully then shopstatus will be shown in output
        '''

        if itemobj is not None:

            db.session.add(itemobj)
            db.session.commit()
            itemstatus.status_code=1
            itemstatus.message="add successfully"
            itemstatus.itemobj=itemobj
        return itemstatus


    def fetchitem():
        alltheaccessories=Shop.query.all() 
        return alltheaccessories

    def deleteitem(id): #delete the item by taking id from user
        matchitem=Shop.query.filter_by(id=id).first()
        itemstatus=shopstatus(0,"added failed",None)
        if matchitem is not None:
            db.session.delete(matchitem)
            db.session.commit()
            itemstatus.status_code=1
            itemstatus.message="deleted successfully"
            itemstatus.itemobj=matchitem
        return itemstatus
    
    def updateitem(itemobj): # here i taken the parameters to user to update
        match_item=Shop.query.filter_by(id=itemobj.id).first()
        itemstatus=shopstatus(0,"added failed",None)
        if match_item is not None:
            match_item.p_price=itemobj.p_price
            match_item.s_price=itemobj.s_price
            match_item.ad_date=itemobj.ad_date
            match_item.ad_date=itemobj.up_date
            db.session.commit()
            itemstatus.status_code=1
            itemstatus.message="updated  successfully"
            itemstatus.itemobj=match_item
        return itemstatus




    

        

        

    
