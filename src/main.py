from fastapi import FastAPI, HTTPException, Body
from models import Customer, CustomerUpdateRequest
from utils import DecimalEncoder, Decimal
from database import connect_with_db
import json

app = FastAPI()

@app.get("/api/v1/customers")
def fetch_all_customers():
    cursor = connect_with_db()
    
    sql = "SELECT * FROM Customer"
    cursor.execute(sql)
    result = cursor.fetchall()

    json_data = [
        {
            "account_number":row[0],
            "first_name":row[1],
            "last_name":row[2],
            "gender":row[3],
            "email":row[4],
            "balance":Decimal(row[5]),
            "is_premium":row[6]
        } 
        for row in result
    ]
    
    json_string = json.dumps(json_data, cls=DecimalEncoder)
    return json_string


@app.get("/api/v1/customers/{account_number}")
def read_customer_detail(account_number: str):
    cursor = connect_with_db()

    sql = f"SELECT * FROM Customer WHERE account_number={account_number}"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    cursor.close()

    if len(result) > 0:
        row = result[0]
        data = {
                "account_number": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "gender": row[3],
                "email": row[4],
                "balance": Decimal(row[5]),
                "is_premium": row[6]
        }
        json_data = json.dumps(data, cls=DecimalEncoder)
        return json_data
    
    raise HTTPException(
        status_code=404,
        detail=f"Customer with Account Number: {account_number} doesn't exist!"
    )


@app.post("/api/v1/customers")
def create_customer_detail(customer: Customer):
    cursor = connect_with_db()
    try:
        sql = f"INSERT INTO Customer (account_number, first_name, last_name, gender, balance, is_premium) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(customer.account_number,customer.first_name,customer.last_name,customer.gender,customer.balance,customer.is_premium))
        
        cursor.connection.commit()
        cursor.close()

        return {"account_number": customer.account_number}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/api/v1/customers/{account_number}")
def update_customer_detail(account_number: str, customer_update: CustomerUpdateRequest):
    cursor = connect_with_db()

    sql = f"SELECT * FROM Customer WHERE account_number={account_number}"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if len(result) == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Customer with Account Number: {account_number} doesn't exist!"
        )

    sql = "UPDATE Customer SET first_name=%s, last_name=%s, gender=%s, email=%s, balance=%s, is_premium=%s WHERE account_number=%s"
    cursor.execute(sql,(customer_update.first_name, customer_update.last_name, customer_update.gender, customer_update.email, customer_update.balance, customer_update.is_premium, account_number))

    cursor.connection.commit()
    cursor.close()
            

@app.delete("/api/v1/customers/{account_number}")
def delete_customer_detail(account_number: str):
    cursor = connect_with_db()
    
    sql = f"DELETE FROM Customer WHERE account_number={account_number}"
    success = cursor.execute(sql)
    
    cursor.connection.commit()
    cursor.close()

    if success == 1:
        return {"account_number": account_number}
    raise HTTPException(
        status_code=404,
        detail=f"Customer with Account Number: {account_number} doesn't exist!"
    )
    