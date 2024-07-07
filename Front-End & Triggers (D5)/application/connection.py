import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import mysql.connector as x
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

db_pass = "rahi412"  # Check if db password is correct
db = x.connect(
    host="localhost",
    user="root",
    password=db_pass,
    database="medease",
    auth_plugin="mysql_native_password",
)
db.close()

try:
    db = x.connect(host="localhost", user="root", password=db_pass)
    c = db.cursor()
    c.execute("CREATE DATABASE Employee;")
    db.commit()
    c.close()
    db.close()
    print("Database created")
except:
    print("Database already exists")


class medease_dbms:
    def __init__(self, root):
        self.root = root
        self.root.title("Med Ease Applicaton")
        self.root.geometry("1550x800+0+0")
        lbltitle = Label(
            self.root,
            text="MEDEASE Application",
            bd=15,
            relief=RIDGE,
            bg="black",
            fg="white",
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=4,
        )
        lbltitle.pack(side=TOP, fill="x")
        self.root.configure(bg="black")
        lbltitle = Label(
            self.root,
            text="MEDEASE Application",
            bd=15,
            relief=RIDGE,
            bg="black",
            fg="white",
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=4,
        )
        lbltitle.pack(side=TOP, fill="x")

        # variables
        self.customerID_var = IntVar()
        self.productID_var = IntVar()
        self.quantity_var = IntVar()
        self.delAddress_var = StringVar()

        # data
        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1530, height=670)

        DataFrameLeft = LabelFrame(
            DataFrame,
            bd=10,
            relief=RIDGE,
            padx=20,
            text="Place an Order",
            fg="black",
            font=("times new roman", 12),
        )
        DataFrameLeft.place(x=0, y=5, width=500, height=350)

        # order stats
        DataFrameRight = LabelFrame(
            DataFrame,
            bd=10,
            relief=RIDGE,
            padx=20,
            text="User Statistics",
            fg="black",
            font=("times new roman", 12),
        )
        DataFrameRight.place(x=550, y=5, width=900, height=350)

        # main button
        btnPlaceOrder = Button(
            DataFrameLeft,
            text="PLACE ORDER",
            font=("helvetica", 16, "bold"),
            fg="white",
            bg="black",
            command=self.placeOrder,
        )
        btnPlaceOrder.grid(row=25, column=0, columnspan=2, pady=40)

        # btnViewStats = Button(
        #     DataFrameRight,
        #     text="view stats",
        #     font=("times new roman", 12),
        #     fg="black",
        #     bg="darkgreen",
        # )
        # btnViewStats.grid(row=0, column=10)

        # labels for entry
        lblCustomerID = Label(
            DataFrameLeft,
            font=("arial", 13, "bold"),
            text="Customer ID",
            padx=2,
            pady=6,
        )
        lblCustomerID.grid(row=0, column=0, sticky=W)
        entryCustomerID = Entry(
            DataFrameLeft,
            textvariable=self.customerID_var,
            font=("arial", 13, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE,
            width=29,
        )
        entryCustomerID.grid(row=0, column=1, sticky=W)

        lblProductID = Label(
            DataFrameLeft, font=("arial", 13, "bold"), text="Product ID", padx=2, pady=6
        )
        lblProductID.grid(row=1, column=0, sticky=W)
        entryProductID = Entry(
            DataFrameLeft,
            textvariable=self.productID_var,
            font=("arial", 13, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE,
            width=29,
        )
        entryProductID.grid(row=1, column=1, sticky=W)

        lblOrderID = Label(
            DataFrameLeft, font=("arial", 13, "bold"), text="Quantity", padx=2, pady=6
        )
        lblOrderID.grid(row=2, column=0, sticky=W)
        entryOrderID = Entry(
            DataFrameLeft,
            textvariable=self.quantity_var,
            font=("arial", 13, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE,
            width=29,
        )
        entryOrderID.grid(row=2, column=1, sticky=W)

        # lblQuantity=Label(DataFrameLeft,font=("arial",13,"bold"),text="Price",padx=2,pady=6)
        # lblQuantity.grid(row=3,column=0,sticky=W)
        # entryQuantity=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        # entryQuantity.grid(row=3,column=1,sticky=W)

        lblDelAddress = Label(
            DataFrameLeft,
            font=("arial", 13, "bold"),
            text="Delivery Address",
            padx=2,
            pady=6,
        )
        lblDelAddress.grid(row=3, column=0, sticky=W)
        entryDelAddress = Entry(
            DataFrameLeft,
            textvariable=self.delAddress_var,
            font=("arial", 13, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE,
            width=29,
        )
        entryDelAddress.grid(row=3, column=1, sticky=W)

        lblQuantity = Label(
            DataFrameLeft,
            font=("arial", 13, "bold"),
            text="Delivery Instructions",
            padx=2,
            pady=6,
        )
        lblQuantity.grid(row=4, column=0, sticky=W)
        entryQuantity = Entry(
            DataFrameLeft,
            font=("arial", 13, "bold"),
            bg="white",
            bd=2,
            relief=RIDGE,
            width=29,
        )
        entryQuantity.grid(row=4, column=1, sticky=W)

        # right Frame
        side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=0, y=5, width=830, height=300)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("Product ID", "Name", "Description", "Price", "Category", "Quantity", " Supplier ID"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading("Product ID", text="Product ID")
        self.medicine_table.heading("Name", text="Name")       
        self.medicine_table.heading("Description", text="Description")
        self.medicine_table.heading( "Price", text= "Price")
        self.medicine_table.heading("Category", text="Category")
        self.medicine_table.heading("Quantity", text="Quantity")
        self.medicine_table.heading(" Supplier ID", text=" Supplier ID")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH, expand=3)

        self.medicine_table.column("Product ID", width=100)
        self.medicine_table.column("Name", width=150)
        self.medicine_table.column("Description", width=200)
        self.medicine_table.column("Price", width=100)
        self.medicine_table.column("Category", width=100)
        self.medicine_table.column("Quantity", width=100)
        self.medicine_table.column(6, width=100)
        
        # calling view stats
        self.viewStats()
        
        ButtonFrame = Frame(self.root, bd=10, relief=RIDGE, padx=20, bg="light gray")
        ButtonFrame.place(x=20, y=500, width=1500, height=280)

        # Graphs
        btnViewStats = Button(
            ButtonFrame,
            text="PRODUCT CATEGORY DISTRIBUTION",
            font=("arial", 20, "bold"),
            fg="white",
            bg="black",
            command=self.display_stats,
            pady=30
        )
        btnViewStats.grid(row=15, column=0, pady=100, padx=10, sticky="ns")

        # New buttons
        btnMoneyStock = Button(
            ButtonFrame,
            text="PRODUCT WISE STOCK",
            font=("arial", 20, "bold"),
            fg="white",
            bg="black",
            command=self.display_money_stock,
            pady=30
        )
        btnMoneyStock.grid(row=15, column=1, pady=100, padx=10, sticky="ns")

        btnSuppliers = Button(
            ButtonFrame,
            text="MEDICINES BY SUPPLIER",
            font=("arial", 20, "bold"),
            fg="white",
            bg="black",
            command=self.display_medicines_by_supplier  ,
            pady=30
        )
        btnSuppliers.grid(row=15, column=2, pady=100, padx=10, sticky="ns")

        # Set row weights to make buttons span the vertical length
        ButtonFrame.grid_rowconfigure((0, 1, 2), weight=1)

        btnViewStats.grid(row=12, column=0, pady=50, padx=40, sticky="ns")  # Decrease the pady value
        btnMoneyStock.grid(row=12, column=1, pady=50, padx=20, sticky="ns")  # Decrease the pady value
        btnSuppliers.grid(row=12, column=2, pady=50, padx=20, sticky="ns")  # Decrease the pady value

    def display_money_stock(self):
        try:
            db_pass = "rahi412"
            db = x.connect(
                host="localhost",
                user="root",
                password=db_pass,
                database="medease",
                auth_plugin="mysql_native_password",
            )
            my_cursor = db.cursor()

            # Fetch data for product-wise monetary stock
            my_cursor.execute("SELECT ProductID, Quantity, Price FROM PRODUCTS")
            rows = my_cursor.fetchall()

            product_ids = []
            monetary_worths = []

            for row in rows:
                product_id = row[0]
                quantity = row[1]
                price = row[2]
                monetary_worth = quantity * price

                product_ids.append(product_id)
                monetary_worths.append(monetary_worth)

            # Plotting the monetary stock graph
            plt.figure(figsize=(10, 6))
            plt.bar(product_ids, monetary_worths, color='skyblue')
            plt.title('Product-wise Monetary Stock')
            plt.xlabel('Product ID')
            plt.ylabel('Monetary Worth')
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        except x.Error as e:
            print("Error while connecting to MySQL", e)

    # Display medicines by individual suppliers
    # Display medicines by individual suppliers
    def display_medicines_by_supplier(self):
        try:
            db_pass = "rahi412"
            db = x.connect(
                host="localhost",
                user="root",
                password=db_pass,
                database="medease",
                auth_plugin="mysql_native_password",
            )
            my_cursor = db.cursor()

            # Fetch data for maximum quantity sold by each supplier
            my_cursor.execute("""
                SELECT s.SupplierID, MAX(p.Name) AS ProductName, MAX(p.Quantity) AS MaxQuantity
                FROM Products p
                JOIN Suppliers s ON p.SupplierID = s.SupplierID
                GROUP BY s.SupplierID
            """)
            rows = my_cursor.fetchall()

            # Create a new window for displaying the results
            supplier_window = Toplevel(self.root)
            supplier_window.title("Medicines by Supplier")

            # Create a frame to hold the data
            frame = Frame(supplier_window)
            frame.pack(padx=20, pady=20)

            # Create a Treeview widget
            tree = ttk.Treeview(frame, columns=("Supplier ID", "Product Name", "Max Quantity"))

            # Define column headings
            tree.heading("#0", text="Index")
            tree.heading("Supplier ID", text="Supplier ID")
            tree.heading("Product Name", text="Product Name")
            tree.heading("Max Quantity", text="Max Quantity")

            # Insert data into the Treeview
            index = 1
            for row in rows:
                supplier_id = row[0]
                product_name = row[1]
                max_quantity = row[2]
                tree.insert("", "end", text=index, values=(supplier_id, product_name, max_quantity))
                index += 1

            # Pack the Treeview widget
            tree.pack(expand=True, fill="both")

        except x.Error as e:
            print("Error while connecting to MySQL", e)


    # ADD MEDICINE FUNCTIONALITY
    def placeOrder(self):
        try:
            db_pass = "rahi412"
            db = x.connect(
                host="localhost",
                user="root",
                password=db_pass,
                database="medease",
                auth_plugin="mysql_native_password",
            )
            my_cursor = db.cursor()

            query = "SELECT Price FROM Products WHERE ProductID = %s"
            my_cursor.execute(query, (self.productID_var.get(),))
            result = my_cursor.fetchone()

            if result:

                price_per_unit = result[0]
                print(price_per_unit)

                total_price = price_per_unit * self.quantity_var.get()

                sql_query = "INSERT INTO `ORDERS` (CustomerID, ProductID, Quantity, Price, DeliveryAddress, OrderStatus, PlacedTime) VALUES (%s, %s, %s, %s, %s, %s, NOW())"

                my_cursor.execute(
                    sql_query,
                    (
                        self.customerID_var.get(),
                        self.productID_var.get(),
                        self.quantity_var.get(),
                        total_price,
                        self.delAddress_var.get(),
                        "Placed",
                    ),
                )

                # # Insert order into orderhistory table
                # order_history_query = "INSERT INTO orderhistory (CustomerID, ProductID, Quantity, Price, DeliveryAddress, OrderStatus, PlacedTime) VALUES (%s, %s, %s, %s, %s, %s, NOW())"
                # my_cursor.execute(
                #     order_history_query,
                #     (
                #         self.customerID_var.get(),
                #         self.productID_var.get(),
                #         self.quantity_var.get(),
                #         total_price,
                #         self.delAddress_var.get(),
                #         "Placed",
                #     ),
                # )
                # Decrease product quantity
                update_query = "UPDATE Products SET Quantity = Quantity - %s WHERE ProductID = %s"
                my_cursor.execute(update_query, (self.quantity_var.get(), self.productID_var.get()))

                # Increase loyalty points
                loyalty_points_earned = int(total_price)  # Example: 1 loyalty point for every $1 spent
                update_customer_query = "UPDATE customers SET LoyaltyPoints = LoyaltyPoints + %s WHERE CustomerID = %s"
                my_cursor.execute(update_customer_query, (loyalty_points_earned, self.customerID_var.get()))

                # Remove product from cart
                delete_cart_query = "DELETE FROM cart WHERE CustomerID = %s AND ProductID = %s"
                my_cursor.execute(delete_cart_query, (self.customerID_var.get(), self.productID_var.get()))

                db.commit()

                my_cursor.close()
                db.close()

                messagebox.showinfo("SUCCESS", "Your order has been placed.")
            else:
                messagebox.showerror(
                    "ERROR", "Product ID not found in the Products table."
                )

        except x.Error as e:
            print("Error while connecting to MySQL", e)
    
    def viewStats(self):
        db_pass = "rahi412"
        db = x.connect(
            host="localhost",
            user="root",
            password=db_pass,
            database="medease",
             auth_plugin="mysql_native_password",
        )
        my_cursor = db.cursor()
        my_cursor.execute("select * from products")
        rows=my_cursor.fetchall()
        for row in self.medicine_table.get_children():
            self.medicine_table.delete(row)

        for row in rows:
            self.medicine_table.insert("", "end", values=row)

    def display_stats(self):
        db_pass = "rahi412"
        db = x.connect(
            host="localhost",
            user="root",
            password=db_pass,
            database="medease",
            auth_plugin="mysql_native_password",
        )
        my_cursor = db.cursor()

        # Fetch data for computing statistics
        my_cursor.execute("SELECT Category, COUNT(*) FROM products GROUP BY Category")
        category_stats = my_cursor.fetchall()

        # Separate categories and counts for plotting
        categories = [row[0] for row in category_stats]
        counts = [row[1] for row in category_stats]

        # Plotting the statistics
        plt.figure(figsize=(8, 6))
        plt.bar(categories, counts, color='skyblue')
        plt.title('Product Category Statistics')
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.grid(True)

        # Display the plot within Tkinter window
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = Tk()
    obj = medease_dbms(root)
    root.mainloop()
