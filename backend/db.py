import oracledb

# Oracle connection details
connection = oracledb.connect(
    user="truckuser",
    password="truckuser",
    dsn="localhost:1521/TRUCKLDB_PDB"
)

def insert_application(company, role, email, message):

    cursor = connection.cursor()

    query = """
    INSERT INTO JOB_APPLICATIONS
    (COMPANY_NAME, JOB_ROLE, HR_EMAIL, MESSAGE)
    VALUES (:1, :2, :3, :4)
    """

    cursor.execute(query, (company, role, email, message))

    connection.commit()

    cursor.close()