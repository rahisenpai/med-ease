from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, DateTime, ForeignKey, Text, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Database Models
class Customer(Base):
    __tablename__ = "Customers"
    
    CustomerID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255), nullable=False)
    FirstName = Column(String(255), nullable=False)
    MiddleName = Column(String(255))
    LastName = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    Pincode = Column(String(6), nullable=False)
    PhoneNumber = Column(String(255), nullable=False)
    EmailID = Column(String(255), unique=True, nullable=False)
    Password = Column(String(255), nullable=False)
    LoyaltyPoints = Column(Integer, default=0)
    
    # Relationships
    orders = relationship("Order", back_populates="customer")
    cart_items = relationship("Cart", back_populates="customer")
    reviews = relationship("DeliveryManReview", back_populates="customer")

class Supplier(Base):
    __tablename__ = "Suppliers"
    
    SupplierID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255), nullable=False)
    PhoneNumber = Column(String(255), nullable=False)
    
    # Relationships
    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = "Products"
    
    ProductID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255), nullable=False)
    Description = Column(String(2550), nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)
    Category = Column(String(255), nullable=False)
    Quantity = Column(Integer, nullable=False)
    SupplierID = Column(Integer, ForeignKey("Suppliers.SupplierID"))
    Image = Column(LargeBinary)
    
    # Relationships
    supplier = relationship("Supplier", back_populates="products")
    orders = relationship("Order", back_populates="product")
    cart_items = relationship("Cart", back_populates="product")

class DeliveryMan(Base):
    __tablename__ = "DeliveryMen"
    
    DeliveryManID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(255), nullable=False)
    FirstName = Column(String(255), nullable=False)
    MiddleName = Column(String(255))
    LastName = Column(String(255), nullable=False)
    MobileNumber = Column(String(255), nullable=False)
    VehicleNumber = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    Pincode = Column(String(255), nullable=False)
    
    # Relationships
    orders = relationship("Order", back_populates="delivery_man")
    order_history = relationship("OrderHistory", back_populates="delivery_man")
    reviews = relationship("DeliveryManReview", back_populates="delivery_man")

class Order(Base):
    __tablename__ = "Orders"
    
    OrderID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"), nullable=False)
    ProductID = Column(Integer, ForeignKey("Products.ProductID"), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)
    DeliveryAddress = Column(String(255), nullable=False)
    OrderStatus = Column(String(255), nullable=False)
    DeliveryManID = Column(Integer, ForeignKey("DeliveryMen.DeliveryManID"))
    PlacedTime = Column(DateTime, nullable=False, default=func.now())
    
    # Relationships
    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    delivery_man = relationship("DeliveryMan", back_populates="orders")

class OrderHistory(Base):
    __tablename__ = "OrderHistory"
    
    OrderID = Column(Integer, ForeignKey("Orders.OrderID"), primary_key=True)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"), nullable=False)
    ProductID = Column(Integer, ForeignKey("Products.ProductID"), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)
    DeliveryAddress = Column(String(255), nullable=False)
    OrderStatus = Column(String(255), nullable=False)
    DeliveryManID = Column(Integer, ForeignKey("DeliveryMen.DeliveryManID"))
    PlacedTime = Column(DateTime, nullable=False)
    DeliveredToCustomer = Column(DateTime)
    
    # Relationships
    customer = relationship("Customer")
    product = relationship("Product")
    delivery_man = relationship("DeliveryMan", back_populates="order_history")

class Cart(Base):
    __tablename__ = "Cart"
    
    CartID = Column(Integer, primary_key=True, index=True)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"), nullable=False)
    ProductID = Column(Integer, ForeignKey("Products.ProductID"), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)
    
    # Relationships
    customer = relationship("Customer", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")

class DeliveryManReview(Base):
    __tablename__ = "DeliveryManReviews"
    
    ReviewID = Column(Integer, primary_key=True, index=True)
    CustomerID = Column(Integer, ForeignKey("Customers.CustomerID"), nullable=False)
    DeliveryManID = Column(Integer, ForeignKey("DeliveryMen.DeliveryManID"), nullable=False)
    Rating = Column(Integer, nullable=False)
    ReviewText = Column(String(2550))
    Time = Column(DateTime, nullable=False, default=func.now())
    
    # Relationships
    customer = relationship("Customer", back_populates="reviews")
    delivery_man = relationship("DeliveryMan", back_populates="reviews")

class Admin(Base):
    __tablename__ = "Admin"
    
    Admin_Username = Column(String(255), primary_key=True)
    Admin_Password = Column(String(16), nullable=False)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
