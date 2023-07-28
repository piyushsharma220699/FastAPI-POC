from fastapi import FastAPI, Path
from models import Customer
from database import db

app = FastAPI()

@app.get("/api/v1/allcustomers")
def fetch_all_customers():
    return db

@app.get("/api/v1/customer/{customer_id}")
def get_customer_detail(customer_id: int):
    for customer_detail in db:
        if customer_detail.id == customer_id:
            return customer_detail

@app.post("/api/v1/customer")
def add_customer_detail(customer: Customer):
    db.append(customer)
    return {"id": customer.id}
