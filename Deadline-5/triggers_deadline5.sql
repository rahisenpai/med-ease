DELIMITER //
CREATE TRIGGER customer_exists
BEFORE INSERT ON ORDERS
FOR EACH ROW
BEGIN
    DECLARE customer_count INT;
    
    SELECT COUNT(*) INTO customer_count FROM Customers WHERE CustomerID = NEW.CustomerID;
    
    IF customer_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer does not exist. Please provide a valid Customer ID.';
    END IF;
END;
//
DELIMITER ;


DELIMITER //

CREATE TRIGGER quantity_less_10
BEFORE INSERT ON ORDERSproducts
FOR EACH ROW
BEGIN
    IF NEW.Quantity > 10 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Quantity cannot exceed 10. Please enter a valid quantity.';
    END IF;
END;

//

DELIMITER ;