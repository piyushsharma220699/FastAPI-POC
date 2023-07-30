from fastapi import FastAPI, HTTPException
from models import Customer, CustomerUpdateRequest
from database import db
from uuid import uuid4, UUID

app = FastAPI()

@app.get("/api/v1/allcustomers")
def fetch_all_customers():
    return db

@app.get("/api/v1/customer/{customer_id}")
def read_customer_detail(customer_id: UUID):
    for customer_detail in db:
        if customer_detail.id == customer_id:
            return customer_detail
    
    raise HTTPException(
        status_code=404,
        detail=f"Customer with ID: {customer_id} doesn't exist!"
    )

@app.post("/api/v1/customer")
def create_customer_detail(customer: Customer):
    db.append(customer)
    return {"id": customer.id}

@app.put("/api/v1/customer/{customer_id}")
def update_customer_detail(customer_update: CustomerUpdateRequest, customer_id: UUID):
    for customer_detail in db:
        if customer_detail.id == customer_id:
            if customer_update.first_name is not None:
                customer_detail.first_name = customer_update.first_name
            if customer_update.last_name is not None:
                customer_detail.last_name = customer_update.last_name
            if customer_update.gender is not None:
                customer_detail.gender = customer_update.gender
            if customer_update.email is not None:
                customer_detail.email = customer_update.email
            if customer_update.account_number is not None:
                customer_detail.account_number = customer_update.account_number
            if customer_update.balance is not None:
                customer_detail.balance = customer_update.balance
            if customer_update.is_premium is not None:
                customer_detail.is_premium = customer_update.is_premium
            return customer_detail
    
    raise HTTPException(
        status_code=404,
        detail=f"Customer with ID: {customer_id} doesn't exist!"
    )
            

@app.delete("/api/v1/customer/{customer_id}")
def delete_customer_detail(customer_id: UUID):
    for customer_detail in db:
        if customer_detail.id == customer_id:
            db.remove(customer_detail)
            return {"id": customer_detail.id}
    
    raise HTTPException(
        status_code=404,
        detail=f"Customer with ID: {customer_id} doesn't exist!"
    )
