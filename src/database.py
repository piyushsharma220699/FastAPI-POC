import pymysql, os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

def connect_with_db():
    print(db_host)
    print(db_user)
    print(str(db_password))
    rds_db = pymysql.connect(host=db_host, user=db_user, password=str(db_password))
    cursor = rds_db.cursor()
    
    sql = f"USE {db_name}"
    cursor.execute(sql)

    return cursor

# CREATE A DATABASE IN AWS RDS USING:
# mysql -h fastapi-poc.cmcrmeiknfnz.us-east-1.rds.amazonaws.com -P 3306 -u admin -p

# CREATE TABLE Customer (
# account_number BIGINT PRIMARY KEY NOT NULL,
# first_name VARCHAR(50) NOT NULL,
# last_name VARCHAR(50) NOT NULL,
# gender ENUM('Male', 'Female') NOT NULL,
# email VARCHAR(100) NOT NULL,
# balance DECIMAL(10,2) NOT NULL,
# is_premium BOOLEAN NOT NULL
# );

# INSERT INTO Customer
# VALUES
# (12345678910, 'Piyush', 'Sharma', 'Male', 'piyushsharma220699@gmail.com', 55000.00, false);

# INSERT INTO Customer
# VALUES
# (98765432110, 'Raghav', 'Dawar', 'male', 'raghavdawar181298@gmail.com', 165000.00, true);

# SELECT * FROM Customer

# SELECT * FROM Customer WHERE account_number=12345678910


# {
#     "first_name": "Vijay",
#     "last_name": "Sharma",
#     "gender": "Male",
#     "email": "vijaysharma30101970@gmail.com",
#     "balance": 175000,
#     "is_premium": true
# }