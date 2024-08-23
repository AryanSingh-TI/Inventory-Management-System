import json
import datetime

class Shop:

    password = "ARYAN"

    def __init__(self):

        while(True):

            print("-"*50)
            choice=input("Do you want to continue with our service? y/n ?")
            print("-"*50)

            if choice not in ["y","Y"]:
                print(f"{'BYE !! HAVE A GREAT DAY':^100}")
                break

            print("-"*50)
            role=input("are you a customer or the owner? c/o ?")
            print("-"*50)

            if role in ["c","C"]:
                c = Customer()

            elif role in ["o","O"]:
                o = Owner()
            else:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                print("xx   Invalid Option   xx")
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                print()


    def updateinventory(self,records):
        fp=open('INEVENTORYwithJSON.json','w')
        fp.write(json.dumps(records))
        fp.close()

    def saleshistory(self,item_purchased,quantity,total_price,email,phone):
        fp=open('salesJSON.txt','a')
        now=datetime.datetime.now()
        now=now.strftime("%y-%m-%d %H:%M:%S")
        fp.write(item_purchased+","+str(quantity)+","+str(total_price)+","+email+","+phone+","+now+"\n")
        fp.close()
            

class Customer(Shop):



    def __init__(self):

        while(True):
            option = self.options()

            if option == 1:
                self.show_menu()

            elif option == 2:
                self.buy_a_product()

            elif option == 3:
                print(f"{'THANK-YOU !! FOR SHOPPING':^100}")
                break
            
            else:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                print("xx   Invalid Option   xx")
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                    
    def options(self):
        print()
        print("--------------PICK AN OPTION-----------------")
        print("| 1 | ==> Show me the available store items |")
        print("| 2 | ==>         Buy a Product             |")
        print("| 3 | ==>       Exit as a Customer          |")
        print("---------------------------------------------")
        return int(input("option :- "))
    
    def show_menu(self):

        fp=open('INEVENTORYwithJSON.json','r')
        records=json.loads(fp.read())
        fp.close()
        print()
        print("..........................................MENU.............................................")
        print("-"*91)
        print("   Product ID   |             NAME             |        PRICE        |       Quantity     |")
        print("-"*91)
        for x,y in records.items():
            print("|"+f"{x:^15}"+":"+f"{y['Name']:^30}"+":"+f"{y['Price']:^21}"+":"+f"{y['Quantity']:^20}"+"|")
        print("-"*91)
        print()
    
    def bill(self,records,pid,q):
        
        print()
        print("..................BILL.................")
        print("-"*40)  
        print("Name             :",f"{records[pid]['Name']:^20}")
        print("Price            :",f"{records[pid]['Price']:^20}")
        print("Quantity         :",f"{str(q):^20}")
        print("-"*40)
        z=q*int(records[pid]['Price'])
        print("Total Spending   :",f"{z:^20}")
        if q*int(records[pid]['Price'])>=5000:
            print("Discount         :",f"{' 10% ':^20}")
            z-=z*(1/10)
            print("After discount   :",f"{z:^20}")
            print("."*40) 
            print()

    def show_product(self,records,pid):

        print()
        print("you chose :-")
        print("-"*91)
        print("   Product ID   |             NAME             |        PRICE        |       Quantity     |")
        print("-"*91)
        print("|"+f"{pid:^15}"+":"+f"{records[pid]['Name']:^30}"+":"+f"{str(records[pid]['Price']):^21}"+":"+f"{str(records[pid]['Quantity']):^20}"+"|")
        print("-"*91)
        print()

    def payment(self,records,pid,q):
        
        amount=q*int(records[pid]['Price'])
        records[pid]['Quantity']=str(int(records[pid]['Quantity'])-q)
        print()
        print(f"{' '+str(amount)+' ruppees have been debited '}".center(40, "#"))
        print(f"{' you got '+str(q)+' '+records[pid]['Name']+' items '}".center(40,"#"))
        print()

    def buy_a_product(self):
        
        print()
        print("-"*91)
        pid=input("|    give the Id of the product you want to buy     |:-  ")
        print("-"*91)
        print()

        fp=open('INEVENTORYwithJSON.json','r')
        records=json.loads(fp.read())
        fp.close()

        if records.get(pid):
                    
            if records[pid]['Quantity']==0:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("xx   Item isn't available for purchase   xx")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()

            else:  
                
                self.show_product(records,pid)

                print()
                print("-"*91)
                q=int(input("|    Give the quantity of the product you want to buy   |   :- "))
                print("-"*91)
                print(records)

                if q<=0:

                    print()
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("xx   Please Enter a Valid Quantity   xx")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print()

                elif q<=int(records[pid]['Quantity']):  

                    self.bill(records,pid,q)
                    ch=input(" would you like to proceed? y/n ")
                    if ch in ["y","Y"]:
                                
                        self.payment(records,pid,q)

                        super().updateinventory(records)
                        phone=input("please provide your phone no:- ")
                        email=input("please provide your email:- ")
                        super().saleshistory(records[pid]['Name'],q,q*int(records[pid]['Price']),email,phone)
                        print()

                    else:
                        print()
                        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                        print("xx     Purchase has been cancelled    xx")
                        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                        print()    

                else:

                    print()
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("xx   Item isn't present in desired Quantity   xx")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print()
                    
                    print()
                    print("************************************************************")
                    print("  NOTICE  :   Available Quantity of item is only  :-",records[pid]['Quantity'])
                    print("************************************************************")
                    print()
                    
                    ch = input(" would you like to proceed ? y/n :- ")

                    if ch=='Y' or ch=='y':

                        self.bill(records,pid,q)
                        ch=input(" would you like to proceed? y/n :- ")

                        if ch in ["Y","y"]:

                            self.payment(records,pid,q)

                            super().updateinventory(records)
                            phone=input("please provide your phone no:- ")
                            email=input("please provide your email:- ")
                            super().saleshistory(records[pid]['Name'],q,q*int(records[pid]['Price']),email,phone)
                            print()

                        else:
                            print()
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            print("xx     Purchase has been cancelled    xx")
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            print()    
                
                    else:
                        print()
                        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                        print("xx     Purchase has been cancelled    xx")
                        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                        print()   

        else:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("xx    Invalid product ID   xx")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()

class Owner(Shop):

    def __init__(self):

        if input(" ENTER THE PASSWORD :- ").upper()==super().password:

            while(True):
                
                option = self.options()

                if option == 1:
                    self.total_revenue()
                elif option == 2:
                    self.items_remaining()
                elif option == 3:
                    self.items_sold()
                elif option == 4:
                    self.add_a_product()
                elif option == 5:
                    self.update_a_product()
                elif option == 6:
                    self.delete_a_product()
                elif option == 7:
                    self.sort_the_products()
                elif option == 8:
                    print("BYE BYE !!")
                    break
                else:
                    print()
                    print("xxxxxxxxxxxxxxxxxxxxxxxx")
                    print("xx   Invalid Option   xx")
                    print("xxxxxxxxxxxxxxxxxxxxxxxx")
                    print()

                
    
    def options(self):

        print()
        print("---------------------PICK AN OPTION-----------------------")
        print("| 1 | ==> Show me the total revenue                      |")
        print("| 2 | ==> Show me the total number of items remaining    |")
        print("| 3 | ==> Show me the total number of items already sold |")
        print("| 4 | ==> Add a product                                  |")
        print("| 5 | ==> Update a product                               |")
        print("| 6 | ==> Delete a product                               |")
        print("| 7 | ==> SORT                                           |")
        print("| 8 | ==> Exit as  an admin                              |")
        print("----------------------------------------------------------")
        return int(input("option :- "))
    
    def total_revenue(self):

        print()
        print("-"*64)
        f=open('salesJSON.txt','r')
        l=f.readlines()
        ts=0
        for i in l:
            if len(i)>3:
                ts+=float(i.split(",")[2])
        print("| total revenue in all the sales ever from the start | :-  ",ts)
        f.close()
        print("-"*64)
        print()

    def items_remaining(self):
        print()
        dk=open('INEVENTORYwithJSON.json','r')
        records=json.loads(dk.read())
        dk.close()
        total_items_remaining=0
        for x,y in records.items():
        
            print("-"*45)
            print("| item name          : ",f"{y['Name']:^18}","|")
            print("| quantity remaining : ",f"{str(y['Quantity']):^18}","|")
            total_items_remaining+=int(y['Quantity'])
        print("-"*45)
        print("total number of items remaining : ",total_items_remaining)
        print()
    
    def items_sold(self):
        f=open('salesJSON.txt','r')
        l=f.readlines()
        ts=0
        for i in l:
            if len(i)>3:
                ts+=int(i.split(",")[1])
        print()
        print("-"*64)
        print("|      total number of items already sold     |   :-  ",ts)
        print("-"*64)
        print()
        f.close()
    
    def add_a_product(self):
        fx =  open("INEVENTORYwithJSON.json", 'r')
        data = json.load(fx)
        fx.close()
        
        product_id =  input("type in the new product id:- ")
        if product_id not in data:
            name =  input("enter the name of the product:- ")
            price = input("enter the price of the product:- ")
            quantity =  input("enter the quantity of the product:- ")

            new_product_data =  {
                "Name": name,
                "Price": price,
                "Quantity": quantity
                                }
    
            data[product_id] = new_product_data
            
            super().updateinventory(data)

            print()
            print("**************************")
            print("*  New Product Addded    *")
            print("**************************")
            print()
        else:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("xx  Product ID already exists  xx")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
    
    def update_a_product(self):

        fk =  open("INEVENTORYwithJSON.json", 'r')
        data = json.load(fk)

        product_id =  input("enter the id of the product you want to update:- ")
        if product_id in data:
            
            choice = input("what do you want to update? Name Price Quantity ?")
            
            if choice.upper() == "NAME":
                name = input("enter the new name of the product:- ")
                data[product_id]["Name"] = name
                super().updateinventory(data)
                fk.close()
            elif choice.upper() == "QUANTITY":
                quantity = input("enter the new quantity of the product:- ")
                data[product_id]["Quantity"] = quantity
                super().updateinventory(data)
                fk.close()
            elif choice.upper() == "PRICE":
                price = input("enter the new price of the product:- ")
                data[product_id]["Price"] = price
                super().updateinventory(data)
                fk.close()
            else:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("xx   Such an entry doesn't exist  xx")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
        else:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("xx  Product ID doesn't exist  xx")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
    
    def delete_a_product(self):

        fk =  open("INEVENTORYwithJSON.json", 'r')
        data = json.load(fk)

        product_id =  input("enter the ID of the product you want to delete - ")
        if product_id in data:
            del data[product_id]
            super().updateinventory(data)
            fk.close()
            print()
            print("**************************")
            print("*    Product Deleted     *")
            print("**************************")
            print()
        
        else:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("xx  Product ID doesn't exist  xx")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
    
    def sort_the_products(self):

        choice = input("Sort on the basis of Price or Quantity ?")
        fp = open('INEVENTORYwithJSON.json','r')
        data = json.load(fp)

        if choice.upper() == "PRICE":
            sorted_inventory = list(sorted(data.items() , key = lambda item : int(item[1]["Price"])))
            for id, dictionary in sorted_inventory:
                print(id,dictionary)
            
        if choice.upper() == "QUANTITY":

            sorted_inventory = list( sorted(data.items() , key = lambda item : int(item[1]["Quantity"])) )
            for id , dictionary in sorted_inventory:
                print(id ,dictionary)
s=Shop()
            

