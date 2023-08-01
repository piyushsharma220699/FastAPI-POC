import pymysql

def connect_with_db(db_name: str):
    rds_db = pymysql.connect(host="fastapi-poc.cmcrmeiknfnz.us-east-1.rds.amazonaws.com", user="admin", password="12345678")
    cursor = rds_db.cursor()
    
    sql = f"USE {db_name}"
    cursor.execute(sql)

    return cursor

# db: List[Customer] = [
#     Customer(
#         id=uuid4(),
#         first_name="Piyush",
#         last_name="Sharma",
#         gender=Gender.male,
#         email="piyushsharma220699@gmail.com",
#         account_number=123456789102,
#         balance=55000,
#         is_premium=False
#     ),
#     Customer(
#         id=uuid4(),
#         first_name="Rohit",
#         last_name="Sharma",
#         gender=Gender.male,
#         email="rohitsharma261203@gmail.com",
#         account_number=734079774021,
#         balance=75000,
#         is_premium=True
#     )
# ]

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

# "SELECT * FROM Customer WHERE account_number=12345678910"


# {
#     "first_name": "Vijay",
#     "last_name": "Sharma",
#     "gender": "Male",
#     "email": "vijaysharma30101970@gmail.com",
#     "balance": 175000,
#     "is_premium": true
# }