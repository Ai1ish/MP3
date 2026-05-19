from datetime import datetime

products = {}

sales_history = []

def add_product():

    product_id = input("Enter Product ID: ")

    if product_id in products:

        print("Product ID already exists!")

        return

    name = input("Enter Product Name: ")

    price = float(input("Enter Product Price: "))

    stock = int(input("Enter Initial Stock: "))

    products[product_id] = {

        "name": name,

        "price": price,

        "stock": stock

    }

    print("Product added successfully!")

def update_product():

    product_id = input("Enter Product ID to update: ")

    if product_id not in products:

        print("Product not found!")

        return

    print("\n1 - Update Name")

    print("2 - Update Price")

    print("3 - Update Stock")

    choice = input("Enter choice: ")

    match choice:

        case "1":

            new_name = input("Enter new product name: ")

            products[product_id]["name"] = new_name

            print("Product name updated!")

        case "2":

            new_price = float(input("Enter new product price: "))

            products[product_id]["price"] = new_price

            print("Product price updated!")

        case "3":

            new_stock = int(input("Enter new stock quantity: "))

            products[product_id]["stock"] = new_stock

            print("Product stock updated!")

        case _:

            print("Invalid choice!")

def record_sale():

    product_id = input("Enter Product ID sold: ")

    if product_id not in products:

        print("Product not found!")

        return

    quantity = int(input("Enter quantity sold: "))

    if quantity > products[product_id]["stock"]:

        print("Insufficient stock!")

        return

    total = quantity * products[product_id]["price"]

    products[product_id]["stock"] -= quantity

    sales = {

        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "product_id": product_id,

        "name": products[product_id]["name"],

        "quantity": quantity,

        "total": total

    }

    sales_history.append(sales)

    print("Sale recorded successfully!")

    print(f"Total Amount: ₱{total:.2f}")

def low_stock_alert():

    print("\nLow Stock Products:")

    found = False

    for product_id, details in products.items():

        if details["stock"] <= 5:

            print(f"ID: {product_id}")

            print(f"Name: {details['name']}")

            print(f"Stock: {details['stock']}")

            print("----------------------")

            found = True

    if not found:

        print("No low stock products.")

def total_inventory_value():

    subtotal = 0

    for details in products.values():

        subtotal += details["price"] * details["stock"]

    print(f"\nTotal Inventory Value (Raw): ₱{subtotal:.2f}")

    # Discount

    apply_discount = input("Apply discount to total? (y/n): ").lower()

    discount_amount = 0

    if apply_discount == "y":

        print("\n1 - Percentage Discount (%)")

        print("2 - Fixed Amount Discount (₱)")

        discount_choice = input("Enter choice: ")

        if discount_choice == "1":

            discount_rate = float(input("Enter discount percentage (e.g. 10 for 10%): "))

            discount_amount = subtotal * (discount_rate / 100)

            print(f"Discount ({discount_rate}%): -₱{discount_amount:.2f}")

        elif discount_choice == "2":

            discount_amount = float(input("Enter discount amount (₱): "))

            if discount_amount > subtotal:

                print("Discount amount cannot exceed total! No discount applied.")

                discount_amount = 0

            else:

                print(f"Discount (Fixed): -₱{discount_amount:.2f}")

        else:

            print("Invalid choice! No discount applied.")

    after_discount = subtotal - discount_amount

    # VAT

    apply_vat = input("Apply VAT to total? (y/n): ").lower()

    vat_amount = 0

    if apply_vat == "y":

        vat_rate = float(input("Enter VAT rate (e.g. 12 for 12%): "))

        vat_amount = after_discount * (vat_rate / 100)

        print(f"VAT ({vat_rate}%): +₱{vat_amount:.2f}")

    total = after_discount + vat_amount

    print("\n--------------------------------------")

    print(f"Subtotal    : ₱{subtotal:.2f}")

    print(f"Discount    : -₱{discount_amount:.2f}")

    print(f"VAT         : +₱{vat_amount:.2f}")

    print(f"GRAND TOTAL : ₱{total:.2f}")

    print("--------------------------------------")

def search_product():

    search = input("Enter Product ID or Name: ").lower()

    found = False

    for product_id, details in products.items():

        if search == product_id.lower() or search == details["name"].lower():

            print("\nProduct Found:")

            print(f"ID: {product_id}")

            print(f"Name: {details['name']}")

            print(f"Price: ₱{details['price']}")

            print(f"Stock: {details['stock']}")

            found = True

    if not found:

        print("Product not found!")

def view_sales_history():

    if not sales_history:

        print("No sales history available.")

        return

    print("\nSales History:")

    for sale in sales_history:

        print("----------------------")

        print(f"Date: {sale['date']}")

        print(f"Product ID: {sale['product_id']}")

        print(f"Product Name: {sale['name']}")

        print(f"Quantity Sold: {sale['quantity']}")

        print(f"Total Amount: ₱{sale['total']}")

# ─────────────────────────────────────────────
# NEW FEATURE: VAT and Discount Calculator
# ─────────────────────────────────────────────

def calculate_vat_discount():

    print("\n===== VAT / DISCOUNT CALCULATOR =====")

    product_id = input("Enter Product ID: ")

    if product_id not in products:

        print("Product not found!")

        return

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:

        print("Quantity must be greater than zero!")

        return

    subtotal = quantity * products[product_id]["price"]

    print(f"\nSubtotal: ₱{subtotal:.2f}")

    # Discount

    apply_discount = input("Apply discount? (y/n): ").lower()

    discount_amount = 0

    if apply_discount == "y":

        print("\n1 - Percentage Discount (%)")

        print("2 - Fixed Amount Discount (₱)")

        discount_choice = input("Enter choice: ")

        if discount_choice == "1":

            discount_rate = float(input("Enter discount percentage (e.g. 10 for 10%): "))

            discount_amount = subtotal * (discount_rate / 100)

            print(f"Discount ({discount_rate}%): -₱{discount_amount:.2f}")

        elif discount_choice == "2":

            discount_amount = float(input("Enter discount amount (₱): "))

            if discount_amount > subtotal:

                print("Discount amount cannot exceed subtotal!")

                return

            print(f"Discount (Fixed): -₱{discount_amount:.2f}")

        else:

            print("Invalid choice! No discount applied.")

    price_after_discount = subtotal - discount_amount

    # VAT

    apply_vat = input("Apply VAT? (y/n): ").lower()

    vat_amount = 0

    if apply_vat == "y":

        vat_rate = float(input("Enter VAT rate (e.g. 12 for 12%): "))

        vat_amount = price_after_discount * (vat_rate / 100)

        print(f"VAT ({vat_rate}%): +₱{vat_amount:.2f}")

    total = price_after_discount + vat_amount

    print("\n--------------------------------------")

    print(f"Product     : {products[product_id]['name']}")

    print(f"Quantity    : {quantity}")

    print(f"Subtotal    : ₱{subtotal:.2f}")

    print(f"Discount    : -₱{discount_amount:.2f}")

    print(f"VAT         : +₱{vat_amount:.2f}")

    print(f"TOTAL       : ₱{total:.2f}")

    print("--------------------------------------")

    save = input("Record this as a sale? (y/n): ").lower()

    if save == "y":

        if quantity > products[product_id]["stock"]:

            print("Insufficient stock! Sale not recorded.")

            return

        products[product_id]["stock"] -= quantity

        sales = {

            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "product_id": product_id,

            "name": products[product_id]["name"],

            "quantity": quantity,

            "total": total

        }

        sales_history.append(sales)

        print("Sale recorded successfully!")

# ─────────────────────────────────────────────

while True:

    print("\n===== INVENTORY MANAGEMENT MENU =====")

    print("1 - Add New Product")

    print("2 - Update Product Info and Stock")

    print("3 - Record Sales Transaction")

    print("4 - Generate Low Stock Alerts")

    print("5 - Calculate Total Inventory Value")

    print("6 - Search Product")

    print("7 - View Sales History")

    print("8 - VAT / Discount Calculator")

    print("9 - Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":

            add_product()

        case "2":

            update_product()

        case "3":

            record_sale()

        case "4":

            low_stock_alert()

        case "5":

            total_inventory_value()

        case "6":

            search_product()

        case "7":

            view_sales_history()

        case "8":

            calculate_vat_discount()

        case "9":

            print("Exiting Inventory Management System...")

            break

        case _:

            print("Invalid choice! Please try again.")