import json

def updateinventory(records):
    fd=open('INEVENTORYwithJSON.json','w')
    fd.write(json.dumps(records))
    fd.close()
    
import datetime
def saleshistory(item_purchased,quantity,total_price,email,phone):
    fk=open('salesJSON.txt','a')
    now=datetime.datetime.now()
    now=now.strftime("%y-%m-%d %H:%M:%S")
    fk.write(item_purchased+","+str(quantity)+","+str(total_price)+","+email+","+phone+","+now+"\n")
    fk.close()


choice="y"
password="ARYAN"

    
while(True):
    
    choice=input("Do you want to continue with our service? y/n ?")
    print("-"*50)
    if choice not in ["y","Y"]:
        break
    role=input("are you a customer or the owner? c/o ?")
    print("-"*50)
    
    if role=="c":
    
        while(True):
            
            print()
            print("--------------PICK AN OPTION-----------------")
            print("| 1 | ==> Show me the available store items |")
            print("| 2 | ==>         Buy a Product             |")
            print("---------------------------------------------")
            option=int(input("option :- "))
            print()
            
            
            if option==1:
                
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
                
            
            elif option==2:
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
                    
                        fp=open('INEVENTORYwithJSON.json','r')
                        records=json.loads(fp.read())
                        fp.close()
                        print()
                        print("you chose :-")
                        print("-"*91)
                        print("   Product ID   |             NAME             |        PRICE        |       Quantity     |")
                        print("-"*91)
                        print("|"+f"{pid:^15}"+":"+f"{records[pid]['Name']:^30}"+":"+f"{str(records[pid]['Price']):^21}"+":"+f"{str(records[pid]['Quantity']):^20}"+"|")
                        print("-"*91)
                        print()




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
                            c=input(" would you like to proceed? y/n ")
                            print()
                            if c in ["y","Y"]:
                                records[pid]['Quantity']=str(int(records[pid]['Quantity'])-q)
                                print()
                                print(f"{' '+str(z)+' ruppees have been debited '}".center(40, "#"))
                                print(f"{' you got '+str(q)+' '+records[pid]['Name']+' items '}".center(40,"#"))
                                print()
                                updateinventory(records)
                                phone=input("please provide your phone no:- ")
                                email=input("please provide your email:- ")
                                saleshistory(records[pid]['Name'],q,z,email,phone)
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
                            print("**************************")
                            print("  NOTICE  :   Available Quantity of item is only ",records[pid]['Quantity'])
                            print("**************************")
                            print()
                            ch = input(" would you like to proceed ? y/n :- ")
                            if ch=='Y' or ch=='y':

                                print()
                                print("..................BILL.................")
                                print("-"*40)  
                                print("Name             :",f"{records[pid]['Name']:^20}")
                                print("Price            :",f"{records[pid]['Price']:^20}")
                                print("Quantity         :",f"{records[pid]['Quantity']:^20}")
                                print("-"*40)
                                z=records[pid]['Price']*records[pid]['Quantity']
                                print("Total Spending   :",f"{z:^20}")
                                if q*records[pid]['Price']>=5000:
                                    print("Discount         :",f"{' 10% ':^20}")
                                    z-=z*(1/10)
                                    print("After Discount   :",f"{z:^20}")
                                print("."*40) 
                                c=input(" would you like to proceed? y/n ")
                                print()
                                if c in ["Y","y"]:
                                    records[pid]['Quantity']=0
                                    print()
                                    print(f"{' '+str(z)+' ruppees have been debited '}".center(40, "#"))
                                    print(f"{' you got '+str(q)+' '+records[pid]['Name']+' items '}".center(40,"#"))
                                    print()
                                    updateinventory(records)
                                    phone=input("please provide your phone no:- ")
                                    email=input("please provide your email:- ")
                                    saleshistory(records[pid]['Name'],q,z,email,phone)
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
            else:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                print("xx   Invalid Option   xx")
                print("xxxxxxxxxxxxxxxxxxxxxxxx")
                print()
            
    
            choice=input("Do you want to continue? y/n ?")
            if choice not in ["y","Y"]:
                print()
                print("**********")
                print("*   Exit as a customer   *")
                print("**********")
                print()
                break
                
    elif role=="o":
        print()
        if input(" ENTER THE PASSWORD :- ").upper()==password:
            print()
            while(True):
            
                print()
                print("---------------------PICK AN OPTION-----------------------")
                print("| 1 | ==> Show me the total revenue                      |")
                print("| 2 | ==> Show me the total number of items remaining    |")
                print("| 3 | ==> Show me the total number of items already sold |")
                print("| 4 | ==> Add a product                                  |")
                print("| 5 | ==> Update a product                               |")
                print("| 6 | ==> Delete a product                               |")
                print("| 7 | ==> SORT                                           |")
                print("----------------------------------------------------------")
                option=int(input("option :- "))
                print()
            
                if option==1:
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
                elif option==2:
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
                elif option==3:
                
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
                elif option==4:

                    fx =  open("INEVENTORYwithJSON.json", 'r')
                    data = json.load(fx)

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
                        fx.close()

                        fx = open("INEVENTORYwithJSON.json",'w')
                        json.dump(data,fx)

                        fx.close()

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
                elif option==5:

                    fk =  open("INEVENTORYwithJSON.json", 'r')
                    data = json.load(fk)

                    product_id =  input("enter the id of the product you want to update:- ")
                    if product_id in data:
                        
                        choice = input("what do you want to update? Name Price Quantity ?")
                        
                        if choice.upper() == "NAME":
                            name = input("enter the new name of the product:- ")
                            data[product_id]["Name"] = name
                            updateinventory(data)
                            fk.close()
                        elif choice.upper() == "QUANTITY":
                            quantity = input("enter the new quantity of the product:- ")
                            data[product_id]["Quantity"] = quantity
                            updateinventory(data)
                            fk.close()
                        elif choice.upper() == "PRICE":
                            price = input("enter the new price of the product:- ")
                            data[product_id]["Price"] = price
                            updateinventory(data)
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
                elif option==6:

                    fk =  open("INEVENTORYwithJSON.json", 'r')
                    data = json.load(fk)

                    product_id =  input("enter the ID of the product you want to delete - ")
                    if product_id in data:
                        del data[product_id]
                        updateinventory(data)
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
                elif option==7:

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


                else:
                    print()
                    print("xxxxxxxxxxxxxxxxxxxxxxxx")
                    print("xx   Invalid Option   xx")
                    print("xxxxxxxxxxxxxxxxxxxxxxxx")
                    print()
                    
                choice=input("Do you want to continue? y/n ?")
                if choice not in ["y","Y"]:
                    print()
                    print("**************************")
                    print("*    Exit as an owner    *")
                    print("**************************")
                    print()
                    break
        else:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("xx   Incorrect Password   xx")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
            
                
    else:
        print()
        print("xxxxxxxxxxxxxxxxxxxxxxxx")
        print("xx   Invalid Option   xx")
        print("xxxxxxxxxxxxxxxxxxxxxxxx")
        print()
print(f"{'THANK-YOU FOR SHOPPING':^100}")