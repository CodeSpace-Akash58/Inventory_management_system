class Inventory:

    # item={}
    # cart={}

    def __init__(self,item_name,price,descr,qty):
        self.item_name= item_name
        self.price=price
        self.descr=descr
        self.qty=qty

    def add_items(self,item_name,price,descr,qty):
        item_name = input('Enter the item_name:  ')
        price = eval(input('Enter Price of item:  '))  
        descr = input('Enter Description about item:  ') 
        qty   = eval(input('Enter quantity of items available: '))
        
        obj= Inventory(item_name=item_name,price=price,descr=descr,qty=qty)
        item[obj.item_name]={}
        item[obj.item_name]['item_name'] = item_name
        item[obj.item_name]['price'] = price
        item[obj.item_name]['descr'] = descr
        item[obj.item_name]['qty'] = qty

    def remove_item(self,item_name):
        item_name = input('Enter the item_name to delete: ') 
        
        if item_name in item:
            del item[item_name]
            print(f'{item_name} successfully deleted from inventory')
        else:
            print(f'No item found')

    def update_item(self,item_name):
        item_name = input('Enter the item_name to update: ')
        
        if item_name in item:
            item[item_name]['item_name']=input('Enter Item_name to update: ')
            item[item_name]['price']=eval(input('Enter price to update: '))
            item[item_name]['descr']=input('Enter description to update: ')
            quant = eval(input('Enter quantity of items to add: '))
            item[item_name]['qty']+= quant

    def display_item(self):
        print('-'*50)
        for k,v in item.items():     #returns key_value pair
            print(k,' : ',v)

        # for item_name in item:
        #     print(f'Item Name: {item[item_name]["item_name"]}')
        #     print(f'Price: {item[item_name]["price"]}')
        #     print(f'Description: {item[item_name]["descr"]}')
        #     print(f'Quantity: {item[item_name]["qty"]}')
        #     print('-'*50)
    item_name={}
    def inquire_item(self,item_name):
        print('Items inquiry in inventory')
        item_name = input('Enter the item_name for inquiry: ')
        print('-'*50)
        if item_name in item:
            print(f'Item Name: {item[item_name]["item_name"]}')
            print(f'Price: {item[item_name]["price"]}') 
            print(f'Description: {item[item_name]["descr"]}')
            print(f'Quantity: {item[item_name]["qty"]}')
            print('-'*50)
        
        # check this
    def purchase_item(self,item_name):
        item_name = input('Enter the item_name for purchase: ')
        
        if item_name in item:
            quant1=eval(input('Enter quantity of items to you want to purchase: '))
            if item[item_name]['qty'] > quant1:
                item[item_name]['qty']-=quant1
                print(f'{quant1} item\'s purchase successfully')
                cart[item_name]=quant1  
                print(f'purchase items in cart',cart[item_name])
            else:
                print('Not enough Items')
        else:
            print('Item not found')
        
    def view_purchase_item(self,item_name):
        item_name = input('Enter purchased item_name: ')
        for item_name in cart:
            print(f'items purchase',cart[item_name])

item={}
cart={}

while True:

    obj= Inventory(' ',0,' ',0)

    print('''
            ********** Inventory Management System ***********
                    
                     1 : Add Item to Inventory
                     2 : Remove Item from Inventory
                     3 : Update Specific Item
                     4 : View Items from Inventory
                     5 : Enquiry about Items
                     6 : Purchase from Inventory
                     7 : View Purchase
                     8 : Exit

            ***************************************************        
         '''
    )  

    ch = int(input('Enter Your choice: '))

    if ch == 1:
        obj.add_items(' ',0,' ',0)

    elif ch == 2:
        obj.remove_item(' ')

    elif ch == 3:
        obj.update_item(' ')

    elif ch == 4:
        obj.display_item()
    
    elif ch == 5:
        obj.inquire_item(' ')
    
    elif ch == 6:
        obj.purchase_item(' ')

    elif ch == 7:
        obj.view_purchase_item(' ')
    
    elif ch == 8:
        print('Exit from system..')
        break

    else:
        print('Enter valid choice:')

    

