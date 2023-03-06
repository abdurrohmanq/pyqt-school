from mysql.connector import connect,Error
cn=connect(
    host="localhost",
    user="root",
    password="abde1234",
)
cur=cn.cursor()