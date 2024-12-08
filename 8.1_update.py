import mysql.connector  

mydb = mysql.connector.connect(  
    host="localhost",  
    user="root",  
    password="",  
    port="3306",  
    database="db_penjualan"  
)  

mycursor = mydb.cursor()  
sql = "UPDATE kategori SET name='roti' where id = 'roti'"  
mycursor.execute(sql)  

mydb.commit()  
print(mycursor.rowcount, "record(s) Updated")