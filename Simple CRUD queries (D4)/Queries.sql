-- 1) List the top 3 customers with the highest total purchase amount:
-- Relational expression:-
-- π CustomerName, TotalPurchaseAmount (δ Desc(TotalPurchaseAmount) (γ CustomerID, SUM(Price) → TotalPurchaseAmount (σ Orders.CustomerID = Customers.CustomerID (Orders ⨝ Customers))))


-- Query :-
SELECT c.Name AS CustomerName, SUM(o.Price) AS TotalPurchaseAmount
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.Name
ORDER BY TotalPurchaseAmount DESC
LIMIT 3;


-- 2) Find out the total number of orders delivered each day:
-- Relational expression:-
-- π OrderDate, TotalOrdersDelivered (γ DATE(PlacedTime) → OrderDate, COUNT(*) → TotalOrdersDelivered (σ OrderStatus = 'Delivered' (Orders)))
-- Query :-
SELECT DATE(PlacedTime) AS OrderDate, COUNT(*) AS TotalOrdersDelivered
FROM Orders
WHERE OrderStatus = 'Delivered'
GROUP BY DATE(PlacedTime);

-- 3) Find the average rating received by each delivery man:
-- Relational expression:-
-- πDeliveryManName,AverageRating((DeliveryMen ⨝ DeliveryMen.DeliveryManID=DeliveryManReviews.DeliveryManID DeliveryManReviews))
-- Query :-
SELECT d.Name AS DeliveryManName, AVG(r.Rating) AS AverageRating
FROM DeliveryMen d
JOIN DeliveryManReviews r ON d.DeliveryManID = r.DeliveryManID
GROUP BY d.Name;


-- 4) To find the average delivery man rating:
-- Relational expression:-
-- γ AVG(Rating) → AverageRating (DeliveryManReviews)
-- Query :-
SELECT AVG(Rating) AS AverageRating
FROM DeliveryManReviews;

-- 5) To find the 5 most commonly ordered products:
-- Relational expression:-
-- π ProductID, ProductName, TotalOrders (δ Desc(TotalOrders) (π ProductID, Name, COUNT(OrderID) → TotalOrders (σ Products.ProductID = Orders.ProductID (Products ⨝ Orders)))))




-- Query :-
SELECT
p.ProductID, p.Name AS ProductName, COUNT(o.OrderID) AS TotalOrders
FROM
Products p
INNER JOIN
Orders o ON p.ProductID = o.ProductID
GROUP BY
p.ProductID, p.Name
ORDER BY
TotalOrders DESC
LIMIT 5;


-- 6) Increase prices of products by 10 percent where the product is supplied by Verma Suppliers.
-- Query:-
Update products
Set Price = Price*1.1
where SupplierID = (select SupplierID
from suppliers
where Name = 'Verma Suppliers');

-- 7) Add 10 Loyalty Points to the customers who have spent at least 100 rupees in the month of March, 2024.

-- Query:-
UPDATE customers
SET LoyaltyPoints = LoyaltyPoints + 10
WHERE CustomerID IN (SELECT CustomerID
FROM orderhistory
WHERE PlacedTime LIKE '2024-03%'
GROUP BY CustomerID
HAVING SUM(Price) > 100 );





-- 8) Clear the cart where user is Rahul Kumar.

-- Query:-
DELETE c FROM cart c, customers cus
WHERE c.CustomerID = cus.CustomerID
AND cus.Name = 'Rahul Kumar';



-- 9) Use 10 Loyalty Points of the user on Pending Order, where OrderID is 4. (Note:1 point gives 1 rupee discount)

-- Query:-
UPDATE orders ord, customers cus
SET ord.Price = ord.Price - 10, cus.LoyaltyPoints = cus.LoyaltyPoints - 10
WHERE ord.CustomerID = cus.CustomerID
AND ord.OrderID = 4;



-- 10) To view customer feedback for Vikram Singh (deliveryman)

-- Relational expression:-
-- πRating,ReviewText,Time (σdeliverymen.name="Vikram Singh"(⨝DeliveryManID=DeliveryManID(DeliveryMen ⨝ DeliveryManReviews)))

-- Query:-
select Rating,ReviewText,Time from deliverymen, deliverymanreviews
where deliverymen.name = "Vikram Singh" and deliverymanreviews.DeliveryManID = deliverymen.DeliveryManID;




-- Note For Queries 11-12: This query violates the constraints, as we are trying to remove records from parent table, so foreign key constraints are violated and this will give error

-- 11) Delete Customer whose Name is Rahul Kumar.

-- Query:-
DELETE FROM customers
WHERE Name = 'Rahul Kumar';




-- 12) Delete Deliverymen whose average rating is 3 or less than 3.

-- Query:-
DELETE FROM deliverymen
WHERE DeliveryManID IN
     (SELECT DeliveryManID
      FROM deliverymanreviews
      GROUP BY DeliveryManID
      HAVING AVG(Rating)<=3);
