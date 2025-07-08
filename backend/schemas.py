from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

# Customer schemas
class CustomerBase(BaseModel):
    Name: str
    FirstName: str
    MiddleName: Optional[str] = None
    LastName: str
    Address: str
    Pincode: str
    PhoneNumber: str
    EmailID: EmailStr

class CustomerCreate(CustomerBase):
    Password: str

class CustomerUpdate(CustomerBase):
    Password: Optional[str] = None
    LoyaltyPoints: Optional[int] = None

class Customer(CustomerBase):
    CustomerID: int
    LoyaltyPoints: int
    
    class Config:
        from_attributes = True

# Product schemas
class ProductBase(BaseModel):
    Name: str
    Description: str
    Price: Decimal
    Category: str
    Quantity: int
    SupplierID: Optional[int] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Price: Optional[Decimal] = None
    Category: Optional[str] = None
    Quantity: Optional[int] = None

class Product(ProductBase):
    ProductID: int
    
    class Config:
        from_attributes = True

# Order schemas
class OrderBase(BaseModel):
    CustomerID: int
    ProductID: int
    Quantity: int
    Price: Decimal
    DeliveryAddress: str
    OrderStatus: str
    DeliveryManID: Optional[int] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    OrderStatus: Optional[str] = None
    DeliveryManID: Optional[int] = None

class Order(OrderBase):
    OrderID: int
    PlacedTime: datetime
    
    class Config:
        from_attributes = True

# Cart schemas
class CartBase(BaseModel):
    ProductID: int
    Quantity: int
    Price: Decimal

class CartCreate(CartBase):
    pass

class CartUpdate(BaseModel):
    Quantity: Optional[int] = None
    Price: Optional[Decimal] = None

class Cart(CartBase):
    CartID: int
    CustomerID: int
    
    class Config:
        from_attributes = True

# Supplier schemas
class SupplierBase(BaseModel):
    Name: str
    PhoneNumber: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    SupplierID: int
    
    class Config:
        from_attributes = True

# DeliveryMan schemas
class DeliveryManBase(BaseModel):
    Name: str
    FirstName: str
    MiddleName: Optional[str] = None
    LastName: str
    MobileNumber: str
    VehicleNumber: str
    Address: str
    Pincode: str

class DeliveryManCreate(DeliveryManBase):
    pass

class DeliveryMan(DeliveryManBase):
    DeliveryManID: int
    
    class Config:
        from_attributes = True

# Review schemas
class ReviewBase(BaseModel):
    CustomerID: int
    DeliveryManID: int
    Rating: int
    ReviewText: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    ReviewID: int
    Time: datetime
    
    class Config:
        from_attributes = True

# Auth schemas
class UserLogin(BaseModel):
    EmailID: EmailStr
    Password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Admin schemas
class AdminLogin(BaseModel):
    Admin_Username: str
    Admin_Password: str

# Analytics schemas
class CustomerPurchaseStats(BaseModel):
    CustomerName: str
    TotalPurchaseAmount: Decimal

class DailyOrderStats(BaseModel):
    OrderDate: str
    TotalOrdersDelivered: int

class DeliveryManRating(BaseModel):
    DeliveryManName: str
    AverageRating: float

class PopularProduct(BaseModel):
    ProductID: int
    ProductName: str
    TotalOrders: int
