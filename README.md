# Inventory Management System

Welcome to the Inventory Management System! This application allows customers to view items, purchase products, and allows store owners to manage inventory, track sales, and more.

## Features

### Customer Features
1. **View Available Store Items**: Display a list of all available items, including product ID, name, price, and quantity.
2. **Buy a Product**: Select a product to purchase, specify quantity, and proceed with the payment. If the total cost exceeds 5000 units, a 10% discount is applied.
3. **Sales History**: Purchases are logged with details such as item name, quantity, total price, email, and phone number.

### Owner Features
1. **Show Total Revenue**: View the total revenue generated from all sales.
2. **Show Remaining Inventory**: Display the quantity of each item currently in stock.
3. **Show Sold Items**: Display the total number of items sold.
4. **Add a Product**: Add new products to the inventory.
5. **Update a Product**: Update details of existing products such as name, price, or quantity.
6. **Delete a Product**: Remove products from the inventory.
7. **Sort Inventory**: Sort items based on price or quantity.

## How to Use

### Running the Program
To start the program, simply run the script. The program will prompt you to choose whether you want to continue with the service and whether you are a customer or the owner.

### For Customers
- **Option 1**: View available store items.
- **Option 2**: Purchase a product. You will need to provide the product ID, quantity, and personal information (email and phone) for the transaction.

### For Owners
- Enter the password to access owner functionalities.
- Choose from the available options to manage inventory and view sales data.

## Files Used
1. **INEVENTORYwithJSON.json**: Contains information about products, including their names, prices, and quantities.
2. **salesJSON.txt**: Logs each sale with details including item purchased, quantity, total price, email, phone number, and date/time of purchase.

## Requirements
- Python 3.x
- No additional libraries are required beyond the standard library.

## Code Structure

1. **updateinventory(records)**: Updates the inventory file with the current state of `records`.
2. **saleshistory(item_purchased, quantity, total_price, email, phone)**: Logs sales information into `salesJSON.txt`.

## Sample Output

**Customer Mode**:
```
--------------PICK AN OPTION-----------------
| 1 | ==> Show me the available store items |
| 2 | ==>         Buy a Product             |
---------------------------------------------
```

**Owner Mode**:
```
---------------------PICK AN OPTION-----------------------
| 1 | ==> Show me the total revenue                      |
| 2 | ==> Show me the total number of items remaining    |
| 3 | ==> Show me the total number of items already sold |
| 4 | ==> Add a product                                  |
| 5 | ==> Update a product                               |
| 6 | ==> Delete a product                               |
| 7 | ==> SORT                                           |
----------------------------------------------------------
```

## Contributions
Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Thank you for using the Inventory Management System! We hope you have a great experience.
