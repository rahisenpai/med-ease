

---------------------------------------------------------
--inserting data

INSERT INTO Admin (Admin_Username, Admin_Password) VALUES ('admin', 'admin123');

INSERT INTO Customers (CustomerID, Name, FirstName, MiddleName, LastName, Address, Pincode, PhoneNumber, EmailID, Password, LoyaltyPoints) 
VALUES 
(1, 'Rahul Kumar', 'Rahul', NULL, 'Kumar', '23, Gandhi Road', '560001', '9876543210', 'rahul@example.com', 'password123', 50),
(2, 'Priya Sharma', 'Priya', NULL, 'Sharma', '45, Nehru Nagar', '560002', '8765432109', 'priya@example.com', 'password456', 30),
(3, 'Amit Patel', 'Amit', NULL, 'Patel', '12, Gandhi Nagar', '560003', '7654321098', 'amit@example.com', 'password789', 20),
(4, 'Sneha Singh', 'Sneha', NULL, 'Singh', '89, Krishna Street', '560004', '6543210987', 'sneha@example.com', 'passwordabc', 10),
(5, 'Anjali Gupta', 'Anjali', NULL, 'Gupta', '34, Rama Road', '560005', '5432109876', 'anjali@example.com', 'passworddef', 5),
(6, 'Rajesh Khanna', 'Rajesh', NULL, 'Khanna', '78, Laxmi Nagar', '560006', '4321098765', 'rajesh@example.com', 'passwordghi', 0),
(7, 'Kavita Verma', 'Kavita', NULL, 'Verma', '56, Radha Street', '560007', '3210987654', 'kavita@example.com', 'passwordjkl', 100),
(8, 'Manoj Tiwari', 'Manoj', NULL, 'Tiwari', '90, Shiva Road', '560008', '2109876543', 'manoj@example.com', 'passwordmno', 80),
(9, 'Meena Jain', 'Meena', NULL, 'Jain', '67, Ganesh Nagar', '560009', '1098765432', 'meena@example.com', 'passwordpqr', 60),
(10, 'Sanjay Reddy', 'Sanjay', NULL, 'Reddy', '45, Hanuman Street', '560010', '0987654321', 'sanjay@example.com', 'passwordstu', 40);


INSERT INTO Suppliers (SupplierID, Name, PhoneNumber) 
VALUES 
(1, 'Sharma Pharmaceuticals', '9876543210'),
(2, 'Patel Medicals', '8765432109'),
(3, 'Singh Distributors', '7654321098'),
(4, 'Gupta Healthcare', '6543210987'),
(5, 'Khanna Enterprises', '5432109876'),
(6, 'Verma Suppliers', '4321098765'),
(7, 'Tiwari Pharma', '3210987654'),
(8, 'Jain Distributors', '2109876543'),
(9, 'Reddy Pharmaceuticals', '1098765432'),
(10, 'Kumar Medicals', '0987654321');


INSERT INTO Products (ProductID, Name, Description, Price, Category, Quantity, SupplierID) 
VALUES 
(1, 'Paracetamol', 'Fever and Pain Relief Tablets', 50.00, 'Medicine', 100, 1),
(2, 'Amoxicillin', 'Antibiotic Capsules', 80.00, 'Medicine', 150, 2),
(3, 'Omeprazole', 'Acid Reducer Capsules', 120.00, 'Medicine', 80, 3),
(4, 'Aspirin', 'Pain Relief Tablets', 30.00, 'Medicine', 200, 4),
(5, 'Vitamin C', 'Immune System Booster Tablets', 100.00, 'Medicine', 120, 5),
(6, 'Cetirizine', 'Antihistamine Tablets', 60.00, 'Medicine', 90, 6),
(7, 'Calcium Supplement', 'Bone Health Tablets', 150.00, 'Medicine', 70, 7),
(8, 'Iron Capsules', 'Iron Deficiency Treatment', 70.00, 'Medicine', 100, 8),
(9, 'Multivitamin Tablets', 'Overall Health Supplement', 200.00, 'Medicine', 60, 9),
(10, 'Diabetic Care Kit', 'Diabetes Management Products', 500.00, 'Medical Equipment', 20, 10);


INSERT INTO DeliveryMen (DeliveryManID, Name, FirstName, MiddleName, LastName, MobileNumber, VehicleNumber, Address, Pincode) 
VALUES 
(1, 'Ravi Kumar', 'Ravi', NULL, 'Kumar', '9876543210', 'KA-01 AB 1234', '23, Gandhi Road', '560001'),
(2, 'Suresh Sharma', 'Suresh', NULL, 'Sharma', '8765432109', 'KA-02 BC 2345', '45, Nehru Nagar', '560002'),
(3, 'Vikram Singh', 'Vikram', NULL, 'Singh', '7654321098', 'KA-03 CD 3456', '12, Gandhi Nagar', '560003'),
(4, 'Prakash Verma', 'Prakash', NULL, 'Verma', '6543210987', 'KA-04 DE 4567', '89, Krishna Street', '560004'),
(5, 'Amit Tiwari', 'Amit', NULL, 'Tiwari', '5432109876', 'KA-05 EF 5678', '34, Rama Road', '560005'),
(6, 'Rajesh Jain', 'Rajesh', NULL, 'Jain', '4321098765', 'KA-06 FG 6789', '78, Laxmi Nagar', '560006'),
(7, 'Sanjay Reddy', 'Sanjay', NULL, 'Reddy', '3210987654', 'KA-07 GH 7890', '56, Radha Street', '560007'),
(8, 'Vinod Gupta', 'Vinod', NULL, 'Gupta', '2109876543', 'KA-08 HI 8901', '90, Shiva Road', '560008'),
(9, 'Anil Patel', 'Anil', NULL, 'Patel', '1098765432', 'KA-09 IJ 9012', '67, Ganesh Nagar', '560009'),
(10, 'Ajay Kumar', 'Ajay', NULL, 'Kumar', '0987654321', 'KA-10 JK 0123', '45, Hanuman Street', '560010');


-- Sample orders placed by customers
INSERT INTO Orders (OrderID, CustomerID, ProductID, Quantity, Price, DeliveryAddress, OrderStatus, DeliveryManID, PlacedTime) 
VALUES 
(1, 1, 1, 2, 100.00, '23, Gandhi Road', 'Pending', 1, NOW()),
(2, 2, 3, 1, 120.00, '45, Nehru Nagar', 'Delivered', 3, NOW()),
(3, 3, 5, 3, 300.00, '12, Gandhi Nagar', 'Pending', 5, NOW()),
(4, 4, 7, 1, 150.00, '89, Krishna Street', 'Pending', 7, NOW()),
(5, 5, 9, 2, 400.00, '34, Rama Road', 'Delivered', 9, NOW()),
(6, 6, 2, 1, 80.00, '78, Laxmi Nagar', 'Pending', 2, NOW()),
(7, 7, 4, 2, 60.00, '56, Radha Street', 'Pending', 4, NOW()),
(8, 8, 6, 3, 180.00, '90, Shiva Road', 'Delivered', 6, NOW()),
(9, 9, 8, 1, 70.00, '67, Ganesh Nagar', 'Pending', 8, NOW()),
(10, 10, 10, 2, 1000.00, '45, Hanuman Street', 'Pending', 10, NOW());


-- order history with deliveries
INSERT INTO OrderHistory (OrderID, CustomerID, ProductID, Quantity, Price, DeliveryAddress, OrderStatus, DeliveryManID, PlacedTime, DeliveredToCustomer) 
VALUES 
(2, 2, 3, 1, 120.00, '45, Nehru Nagar', 'Delivered', 3, NOW() - INTERVAL 2 DAY, NOW() - INTERVAL 1 DAY),
(5, 5, 9, 2, 400.00, '34, Rama Road', 'Delivered', 9, NOW() - INTERVAL 1 DAY, NOW() - INTERVAL 6 HOUR),
(8, 8, 6, 3, 180.00, '90, Shiva Road', 'Delivered', 6, NOW() - INTERVAL 3 DAY, NOW() - INTERVAL 2 DAY);


INSERT INTO Cart (CartID, CustomerID, ProductID, Quantity, Price) 
VALUES 
(1, 1, 4, 2, 60.00),
(2, 3, 8, 1, 70.00),
(3, 5, 1, 3, 150.00),
(4, 7, 5, 2, 200.00),
(5, 9, 10, 1, 500.00);


INSERT INTO DeliveryManReviews (ReviewID, CustomerID, DeliveryManID, Rating, ReviewText, Time) 
VALUES 
(1, 2, 3, 4, 'Excellent service!', NOW() - INTERVAL 1 DAY),
(2, 5, 9, 5, 'Very polite and punctual.', NOW() - INTERVAL 2 DAY),
(3, 8, 6, 3, 'Could be more punctual.', NOW() - INTERVAL 3 DAY),
(4, 10, 10, 5, 'Best delivery experience ever!', NOW() - INTERVAL 1 DAY);



