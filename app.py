import pandas as pd
from flask import Flask, request, jsonify, render_template
import dbconnect
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ecomdb"
)
mycursor = mydb.cursor()


app = Flask(__name__, template_folder='templates', static_folder='static')

#SIGNUP API.
@app.route("/signup/<uid>/<un>/<pw>/<fn>/<ln>", methods=['POST'])
def signup(uid,un,pw,fn,ln):
    sql = "INSERT INTO Userlogin (UID, Username, Password, Fname, Lname) VALUES (%s, %s, %s, %s, %s)"
    val = (uid,un,pw,fn,ln)
    mycursor.execute(sql, val)
    mydb.commit()
    return dbconnect.userdetails


#USER LOGIN API.
@app.route("/userlogin/<un>/<pw>", methods = ['GET'])
def UserLogin(un,pw):
    data = dbconnect.userdetails
    success_login = 0
    for i in data:
        if un == i[1]:
            if pw == i[2]:
                success_login = 1
                response = {
                    "response" : 200,
                    "text" : (f"welcome {i[3]} {i[4]}"),
                }
                return jsonify(response)
            else:
                response = {
                    "response" : 200,
                    "text" : "wrong password.",
                }
                return jsonify(response)
        else:
            continue
    if success_login == 0:
        response = {
                    "response" : 200,
                    "text" : "Wrong credentials.",
                }
        return jsonify(response)
    



#COUPON CODE API.
@app.route("/<string:a>/<string:n>", methods = ['GET'])
def CouponCode(a,n):
    data = dbconnect.coupons
    uid = request.args.get('uid')
    if a == '1':
        d_entered = n
        s = 0
        q = 0
        for i in data:
            q+=1
            if d_entered == i[1]:
                s = q 
                break
        if s != 0:
            return(f'{d_entered} is applied {i[2]}% discount is applied.{uid}')
        else:
            return("invalid coupon!")
    else:
        return (f'{n} coupon is successfully removed!')

@app.route("/")
def main():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    