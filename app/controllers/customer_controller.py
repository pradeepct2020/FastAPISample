from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer_schema import CustomerSchema
from app.db.database import get_db
from app.utils.response_wrapper import api_response

router = APIRouter()

# CREATE Customer
@router.post("/customers/")
def create_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
    if db.query(Customer).filter(Customer.email == customer.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return api_response(data=new_customer, message="Customer created successfully")

@router.get("/customers/")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()
    return api_response(data=customers, message="All customers retrieved")

# READ Single Customer
@router.get("/customers/{customer_id}")
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return api_response(data=customer, message="Customer retrieved successfully")

# UPDATE Customer
@router.put("/customers/{customer_id}")
def update_customer(customer_id: str, customer_update: CustomerSchema, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    for field, value in customer_update.dict(exclude_unset=True).items():
        setattr(customer, field, value)
    
    db.commit()
    db.refresh(customer)
    return api_response(data=customer, message="Customer updated successfully")

# DELETE Customer
@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db.delete(customer)
    db.commit()
    return api_response(message="Customer deleted successfully")