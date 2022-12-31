import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ecomdb"
)
mycursor = mydb.cursor()


#user Details
mycursor.execute("SELECT * FROM Userlogin")
userdetails = mycursor.fetchall()

#coupon codes data.
mycursor.execute("SELECT * FROM Coupon")
coupons = mycursor.fetchall()