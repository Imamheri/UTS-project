import mysql.connector  

mydb = mysql.connector.connect(  
    host="localhost",  
    user="root",  
    password="",  
    port="3306",  
    database="db_penjualan"  
)  

mycursor = mydb.cursor()  
sql = "SELECT * FROM kategori where id ='roti'"  
mycursor.execute(sql)  
myresult = mycursor.fetchall()  

for x in myresult:  
    print(x)