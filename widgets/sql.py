from mysql.connector import connect,Error
#from widgets.sql_0 import *
# from mysql.connector import connect,Error
# cn=connect(
#     host="localhost",
#     user="root",
#     password="abde1234",
# )
# cur=cn.cursor()
# class date():
#     @staticmethod
#     def get_column(first_name,last_name,phone):
#         cur.execute="use school"
#         cur.execute("insert into puplies(first_name,last_name,phone) values(%s,%s,%s)",(first_name,last_name,phone))
        
#         cn.commit()

#     @staticmethod
#     def check(first_name:str,last_name:str)->bool:
#         cur.execute("Use school")
#         cur.execute("SELECT first_name,last_name from puplies")
#         ans=cur.fetchall()
#         for i in ans:
#             if i[0]==first_name or i[1]==last_name:
#                 return False
#             else:
#     
#             return True

class date():
    @staticmethod
    def select_pupl():
       return"""Select * from puplies """
    def add_pupl():
       return """ INSERT INTO puplies(first_name,last_name,phone) VALUES(%s,%s,%s)"""
    

cn=connect(
host="localhost",
user="root",
password="abde1234",
database="school"
)
cur=cn.cursor()
