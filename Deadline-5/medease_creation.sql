CREATE DATABASE MedEase;
use MedEase;
CREATE TABLE Customers (
  CustomerID int PRIMARY KEY,
  Name varchar(255) NOT NULL,
   FirstName varchar(255) NOT NULL,
   MiddleName varchar(255),
  LastName varchar(255) NOT NULL,
  Address varchar(255) NOT NULL,
  Pincode varchar(6) NOT NULL,
  PhoneNumber varchar(255) NOT NULL,
  EmailID varchar(255) UNIQUE NOT NULL,
  Password varchar(255) NOT NULL,
  LoyaltyPoints int DEFAULT 0
);
CREATE TABLE Suppliers (
  SupplierID int PRIMARY KEY,
  Name varchar(255) NOT NULL,
  PhoneNumber varchar(255) NOT NULL
);
CREATE TABLE Products (
  ProductID int PRIMARY KEY,
  Name varchar(255) NOT NULL,
  Description varchar(2550) NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  Category varchar(255) NOT NULL,
  Quantity int NOT NULL,
  SupplierID int,
  Image varbinary(255),
  FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);
CREATE TABLE DeliveryMen (
  DeliveryManID int PRIMARY KEY,
  Name varchar(255) NOT NULL,
  FirstName varchar(255) NOT NULL,
  MiddleName varchar(255),
  LastName varchar(255) NOT NULL,
  MobileNumber varchar(255) NOT NULL,
  VehicleNumber varchar(255) NOT NULL,
  Address varchar(255) NOT NULL,
  Pincode varchar(255) NOT NULL
);
CREATE TABLE Orders (
  OrderID int PRIMARY KEY auto_increment,
  CustomerID int NOT NULL,
  ProductID int NOT NULL,
  Quantity int NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  DeliveryAddress varchar(255) NOT NULL,
  OrderStatus varchar(255) NOT NULL,
  DeliveryManID int,
  PlacedTime datetime NOT NULL,
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
  FOREIGN KEY (DeliveryManID) REFERENCES DeliveryMen(DeliveryManID)
);

CREATE TABLE OrderHistory (
  OrderID int PRIMARY KEY,
  CustomerID int NOT NULL,
  ProductID int NOT NULL,
  Quantity int NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  DeliveryAddress varchar(255) NOT NULL,
  OrderStatus varchar(255) NOT NULL,
  DeliveryManID int,
  PlacedTime datetime NOT NULL,
  DeliveredToCustomer datetime,
  FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
  FOREIGN KEY (DeliveryManID) REFERENCES DeliveryMen(DeliveryManID)
);
CREATE TABLE Cart (
  CartID int PRIMARY KEY,
  CustomerID int NOT NULL,
  ProductID int NOT NULL,
  Quantity int NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
CREATE TABLE DeliveryManReviews (
  ReviewID int PRIMARY KEY,
  CustomerID int NOT NULL,
  DeliveryManID int NOT NULL,
  Rating int NOT NULL,
  ReviewText varchar(2550),
  Time datetime NOT NULL,
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
   FOREIGN KEY (DeliveryManID) REFERENCES DeliveryMen(DeliveryManID)
);
CREATE TABLE Admin (
	Admin_Username varchar(255) PRIMARY KEY,
    Admin_Password varchar(16) NOT NULL
);

