import mysql.connector
mydb=mysql.connector.connect(
user="root",
host="localhost",
database="atm",
password="12345"
      )
#connection
connection=mydb.cursor()
#print
print("$$$$$$$$welcome to besant bank of india$$$$$$$$")
pin=int(input("enter your pin:"))

if pin==100:
        # choice=int(input("enter the below operation"))
        print("""select the operation
            1.withdrawal
            2.deposite
            3.balance check
            """)
        choice=int(input("enter any above operation:"))
else:
      print("enter the correct pin") 

if choice==1:
  amount=int(input("enter the amount:"))
  sql="update bank set balance = balance-%s"
  wd="update bank set withdrawal = withdrawal+%s"
  connection.execute(sql,(amount,))
  connection.execute(wd,(amount,))
  mydb.commit()
  connection.close()
  mydb.close()
  print("withdrawal amount is added to the database")
  print(f"your amount{amount} is withdrawed")
  
  
if choice==2:
  da=int(input("how much amount u want deposite:"))
  up="update bank set balance = balance+%s"
  dp="update bank set deposite = deposite+%s "
  connection.execute(up,(da,))
  connection.execute(dp,(da,))
  mydb.commit()
  connection.close()
  mydb.close()
  print("your deposite amount is updated succesfully")
  print(f"your amount{da} deposited successfully")
  
if choice==3:
  connection.execute("select balance from bank;")
  result=connection.fetchall()
  print(f" your current balance {result}")



