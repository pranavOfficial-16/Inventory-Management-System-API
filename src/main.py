from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from .database import get_db, engine, Base
from .models import Product
from .schemas import ProductCreate, ProductUpdate, ProductResponse, StockUpdate

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Inventory Management API is running"}

# CREATE - Add new product
@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# READ - Get all products
@app.get("/products", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# READ - Get products whose stock quantity is less than or equal to low stock threshold
@app.get("/products/low-stock", response_model=List[ProductResponse])
def get_low_stock_products(db: Session = Depends(get_db)):
    return db.query(Product).filter(
        Product.stock_quantity <= Product.low_stock_threshold
    ).all()
    
# READ - Get single product by ID
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# UPDATE - Update product details
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_data = product_update.dict(exclude_unset=True)
    
    # Validate stock_quantity if provided
    if 'stock_quantity' in update_data and update_data['stock_quantity'] is not None:
        if update_data['stock_quantity'] < 0:
            raise HTTPException(status_code=400, detail="Stock quantity cannot be negative")
    
    for field, value in update_data.items():
        setattr(db_product, field, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

# DELETE - Remove product
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return None

# Increase stock quantity
@app.post("/products/{product_id}/increase-stock", response_model=ProductResponse)
def increase_stock(product_id: int, stock_update: StockUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.stock_quantity += stock_update.quantity
    db.commit()
    db.refresh(product)
    return product

# Decrease stock quantity (with validation)
@app.post("/products/{product_id}/decrease-stock", response_model=ProductResponse)
def decrease_stock(product_id: int, stock_update: StockUpdate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product.stock_quantity < stock_update.quantity:
        raise HTTPException(
            status_code=400, 
            detail=f"Insufficient stock. Available: {product.stock_quantity}, Requested: {stock_update.quantity}"
        )
    
    product.stock_quantity -= stock_update.quantity
    db.commit()
    db.refresh(product)
    return product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)