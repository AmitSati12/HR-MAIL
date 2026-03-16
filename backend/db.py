from pymongo import MongoClient
import os

# Read MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

# database name
db = client["jobmailer"]

# collection name
collection = db["applications"]

def insert_application(company, role, email, message):

    data = {
        "company": company,
        "role": role,
        "email": email,
        "message": message
    }

    collection.insert_one(data)

# import oracledb

# # Oracle connection details
# connection = oracledb.connect(
#     user="truckuser",
#     password="truckuser",
#     dsn="localhost:1521/TRUCKLDB_PDB"
# )

# def insert_application(company, role, email, message):

#     cursor = connection.cursor()

#     query = """
#     INSERT INTO JOB_APPLICATIONS
#     (COMPANY_NAME, JOB_ROLE, HR_EMAIL, MESSAGE)
#     VALUES (:1, :2, :3, :4)
#     """

#     cursor.execute(query, (company, role, email, message))

#     connection.commit()

#     cursor.close()