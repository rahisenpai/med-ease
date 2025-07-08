from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func, text
from typing import List, Optional
from datetime import datetime, timedelta
import uvicorn

from database import get_db, Customer, Product, Order, Cart, Supplier, DeliveryMan, DeliveryManReview, Admin, OrderHistory
from schemas import (
    CustomerCreate, CustomerUpdate, Customer as CustomerSchema,
    ProductCreate, ProductUpdate, Product as ProductSchema,
    OrderCreate, OrderUpdate, Order as OrderSchema,
    CartCreate, CartUpdate, Cart as CartSchema,
    SupplierCreate, Supplier as SupplierSchema,
    DeliveryManCreate, DeliveryMan as DeliveryManSchema,
    ReviewCreate, Review as ReviewSchema,
    UserLogin, Token, AdminLogin,
    CustomerPurchaseStats, DailyOrderStats, DeliveryManRating, PopularProduct
)
from auth import verify_password, get_password_hash, create_access_token, verify_token

# Initialize FastAPI app
app = FastAPI(title="MedEase API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    email = verify_token(token)
    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(Customer).filter(Customer.EmailID == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to MedEase API"}

# Auth endpoints
@app.post("/auth/register", response_model=CustomerSchema)
def register(customer: CustomerCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_customer = db.query(Customer).filter(Customer.EmailID == customer.EmailID).first()
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Get the next available CustomerID
    max_id = db.query(func.max(Customer.CustomerID)).scalar() or 0
    next_id = max_id + 1
    
    # Create new customer (keeping password as plain text to match existing DB structure)
    customer_data = customer.dict()
    customer_data['CustomerID'] = next_id
    db_customer = Customer(**customer_data)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.post("/auth/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(Customer).filter(Customer.EmailID == user_credentials.EmailID).first()
    
    if not user or user.Password != user_credentials.Password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.EmailID}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/auth/admin/login", response_model=Token)
def admin_login(admin_credentials: AdminLogin, db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.Admin_Username == admin_credentials.Admin_Username).first()
    
    if not admin or admin.Admin_Password != admin_credentials.Admin_Password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": admin.Admin_Username, "role": "admin"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Customer endpoints
@app.get("/customers/me", response_model=CustomerSchema)
def get_current_customer(current_user: Customer = Depends(get_current_user)):
    return current_user

@app.put("/customers/me", response_model=CustomerSchema)
def update_current_customer(customer_update: CustomerUpdate, current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    for field, value in customer_update.dict(exclude_unset=True).items():
        if field == "Password" and value:
            value = get_password_hash(value)
        setattr(current_user, field, value)
    
    db.commit()
    db.refresh(current_user)
    return current_user

@app.get("/customers", response_model=List[CustomerSchema])
def get_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = db.query(Customer).offset(skip).limit(limit).all()
    return customers

# Product endpoints
@app.get("/products", response_model=List[ProductSchema])
def get_products(skip: int = 0, limit: int = 100, category: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Product)
    if category:
        query = query.filter(Product.Category == category)
    products = query.offset(skip).limit(limit).all()
    return products

@app.get("/products/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.ProductID == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=ProductSchema)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.ProductID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for field, value in product_update.dict(exclude_unset=True).items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.ProductID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

# Order endpoints
@app.get("/orders", response_model=List[OrderSchema])
def get_orders(current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.CustomerID == current_user.CustomerID).all()
    return orders

@app.post("/orders", response_model=OrderSchema)
def create_order(order: OrderCreate, current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    # Set customer ID from current user
    order.CustomerID = current_user.CustomerID
    
    # Check if product exists and has enough quantity
    product = db.query(Product).filter(Product.ProductID == order.ProductID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.Quantity < order.Quantity:
        raise HTTPException(status_code=400, detail="Insufficient product quantity")
    
    # Create order
    db_order = Order(**order.dict())
    db.add(db_order)
    
    # Update product quantity
    product.Quantity -= order.Quantity
    
    db.commit()
    db.refresh(db_order)
    return db_order

@app.put("/orders/{order_id}", response_model=OrderSchema)
def update_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.OrderID == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    for field, value in order_update.dict(exclude_unset=True).items():
        setattr(db_order, field, value)
    
    db.commit()
    db.refresh(db_order)
    return db_order

# Cart endpoints
@app.get("/cart", response_model=List[CartSchema])
def get_cart(current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    cart_items = db.query(Cart).filter(Cart.CustomerID == current_user.CustomerID).all()
    return cart_items

@app.post("/cart", response_model=CartSchema)
def add_to_cart(cart_item: CartCreate, current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    
    # Check if item already exists in cart
    existing_item = db.query(Cart).filter(
        Cart.CustomerID == current_user.CustomerID,
        Cart.ProductID == cart_item.ProductID
    ).first()
    
    if existing_item:
        # Update quantity
        existing_item.Quantity += cart_item.Quantity
        existing_item.Price = cart_item.Price
        db.commit()
        db.refresh(existing_item)
        return existing_item
    else:
        # Get the next available CartID
        max_cart_id = db.query(func.max(Cart.CartID)).scalar() or 0
        next_cart_id = max_cart_id + 1
        
        # Create new cart item
        cart_data = cart_item.dict()
        cart_data['CustomerID'] = current_user.CustomerID
        cart_data['CartID'] = next_cart_id
        db_cart_item = Cart(**cart_data)
        db.add(db_cart_item)
        db.commit()
        db.refresh(db_cart_item)
        return db_cart_item

@app.delete("/cart/{cart_id}")
def remove_from_cart(cart_id: int, current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    cart_item = db.query(Cart).filter(
        Cart.CartID == cart_id,
        Cart.CustomerID == current_user.CustomerID
    ).first()
    
    if cart_item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    
    db.delete(cart_item)
    db.commit()
    return {"message": "Item removed from cart"}

@app.delete("/cart")
def clear_cart(current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    db.query(Cart).filter(Cart.CustomerID == current_user.CustomerID).delete()
    db.commit()
    return {"message": "Cart cleared successfully"}

# Supplier endpoints
@app.get("/suppliers", response_model=List[SupplierSchema])
def get_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suppliers = db.query(Supplier).offset(skip).limit(limit).all()
    return suppliers

@app.post("/suppliers", response_model=SupplierSchema)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

# DeliveryMan endpoints
@app.get("/delivery-men", response_model=List[DeliveryManSchema])
def get_delivery_men(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    delivery_men = db.query(DeliveryMan).offset(skip).limit(limit).all()
    return delivery_men

@app.post("/delivery-men", response_model=DeliveryManSchema)
def create_delivery_man(delivery_man: DeliveryManCreate, db: Session = Depends(get_db)):
    db_delivery_man = DeliveryMan(**delivery_man.dict())
    db.add(db_delivery_man)
    db.commit()
    db.refresh(db_delivery_man)
    return db_delivery_man

# Review endpoints
@app.get("/reviews", response_model=List[ReviewSchema])
def get_reviews(delivery_man_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(DeliveryManReview)
    if delivery_man_id:
        query = query.filter(DeliveryManReview.DeliveryManID == delivery_man_id)
    reviews = query.all()
    return reviews

@app.post("/reviews", response_model=ReviewSchema)
def create_review(review: ReviewCreate, current_user: Customer = Depends(get_current_user), db: Session = Depends(get_db)):
    review.CustomerID = current_user.CustomerID
    db_review = DeliveryManReview(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

# Analytics endpoints
@app.get("/analytics/top-customers", response_model=List[CustomerPurchaseStats])
def get_top_customers(limit: int = 3, db: Session = Depends(get_db)):
    result = db.execute(text("""
        SELECT c.Name AS CustomerName, SUM(o.Price) AS TotalPurchaseAmount
        FROM Orders o
        JOIN Customers c ON o.CustomerID = c.CustomerID
        GROUP BY c.Name
        ORDER BY TotalPurchaseAmount DESC
        LIMIT :limit
    """), {"limit": limit}).fetchall()
    
    return [{"CustomerName": row[0], "TotalPurchaseAmount": row[1]} for row in result]

@app.get("/analytics/daily-orders", response_model=List[DailyOrderStats])
def get_daily_orders(db: Session = Depends(get_db)):
    result = db.execute(text("""
        SELECT DATE(PlacedTime) AS OrderDate, COUNT(*) AS TotalOrdersDelivered
        FROM Orders
        WHERE OrderStatus = 'Delivered'
        GROUP BY DATE(PlacedTime)
    """)).fetchall()
    
    return [{"OrderDate": str(row[0]), "TotalOrdersDelivered": row[1]} for row in result]

@app.get("/analytics/delivery-ratings", response_model=List[DeliveryManRating])
def get_delivery_ratings(db: Session = Depends(get_db)):
    result = db.execute(text("""
        SELECT d.Name AS DeliveryManName, AVG(r.Rating) AS AverageRating
        FROM DeliveryMen d
        JOIN DeliveryManReviews r ON d.DeliveryManID = r.DeliveryManID
        GROUP BY d.Name
    """)).fetchall()
    
    return [{"DeliveryManName": row[0], "AverageRating": float(row[1])} for row in result]

@app.get("/analytics/popular-products", response_model=List[PopularProduct])
def get_popular_products(limit: int = 5, db: Session = Depends(get_db)):
    result = db.execute(text("""
        SELECT p.ProductID, p.Name AS ProductName, COUNT(o.OrderID) AS TotalOrders
        FROM Products p
        INNER JOIN Orders o ON p.ProductID = o.ProductID
        GROUP BY p.ProductID, p.Name
        ORDER BY TotalOrders DESC
        LIMIT :limit
    """), {"limit": limit}).fetchall()
    
    return [{"ProductID": row[0], "ProductName": row[1], "TotalOrders": row[2]} for row in result]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
