#Write a Python code to configure the MySQL Connector in your system and Insert data to MySQL Table after which you Fetch and Display data from Table

import mysql.connector

cnx = mysql.connector.connect(user='root', password='Maurya@1998',
                              host='localhost',
                              database="college"
                              )

cursor = cnx.cursor()
#cursor.execute("CREATE TABLE student(name varchar(200), address varchar(250), collegeName varchar(230))")

# insert data into database
sql = "INSERT INTO student (name, address, collegeName) VALUES (%s, %s, %s)"
val = ("Kameshwar", "Varanasi", "IET")
cursor.execute(sql, val)
cnx.commit()
print(cursor.rowcount, "record inserted.")

# fetch the data from database

cursor.execute("SELECT * FROM student")

myresult = cursor.fetchall()

for x in myresult:
  print(x)
cnx.close()


