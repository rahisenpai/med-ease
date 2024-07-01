# MedEase Application

Starter repository for the course CSE202 - Fundamentals of Database Management System (Winter 2024), IIIT Delhi.

## Collaborators

Himanshu Raj [@rahisenpai](https://www.github.com/rahisenpai)<br />
Parth Rastogi [@parthrastogicoder](https://www.github.com/parthrastogicoder)<br />
Shagun Yadav [@kyukuu](https://www.github.com/kyukuu)<br />
Tanish Verma [@VerTanish](https://www.github.com/VerTanish)

## Overview

MedEase is an online medicine delivery application designed to facilitate the purchase and delivery of pharmaceutical products to customers. This repository contains the database schema and the initial application code for managing orders, customer information, product inventory, and delivery personnel.

## Database Configuration

### Tables

1. **Customers**
   - Stores information about customers including their personal details, contact information, and loyalty points.

2. **Suppliers**
   - Contains details of suppliers who provide the products.

3. **Products**
   - Holds information about the products available for purchase, including their descriptions, prices, and supplier details.

4. **DeliveryMen**
   - Maintains details of delivery personnel responsible for delivering orders to customers.

5. **Orders**
   - Records information about customer orders, including the product details, quantity, price, delivery address, and order status.

6. **OrderHistory**
   - Archives past orders, including details about the customer, product, quantity, price, delivery address, and order status.

7. **Cart**
   - Tracks items added to the cart by customers before they place an order.

8. **DeliveryManReviews**
   - Contains customer reviews and ratings for delivery personnel.


## Application Code

The application is built using Python and Tkinter for the GUI and connects to a MySQL database for data storage and retrieval. The key features of the application include:

- Placing orders
- Viewing product statistics
- Viewing and managing customer orders
- Reviewing delivery personnel

### Requirements

- Python 3.x
- MySQL Server
- Tkinter library
- MySQL Connector for Python

### Running the Application

1. Ensure MySQL server is running and accessible.
2. Clone this repository.
3. Set up the database using the provided SQL schema.
4. Update the database configuration in the application code if necessary.
5. Run the application using the following command:
   ```bash
   python connection.py
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This README provides a comprehensive overview of the MedEase application, including the database configuration and instructions for setting up and running the application.
