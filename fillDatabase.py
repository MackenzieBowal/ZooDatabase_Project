import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase",
    autocommit = True
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO Employee \
                VALUES ('12345', 'Alice Anderson', '1 First Street', \
                'alice2840@gmail.com', '4032370847', '2022-11-29'), \
                ('23456', 'Bob Bartholomew', '2 Second Street', \
                'bobbarth@hotmail.com', '4035418678', '2017-08-01'), \
                ('34567', 'Charlie Clark', '3 Third Street', \
                'charliec5@gmail.com', '5873109226', '2019-09-06'), \
                ('45678', 'Debra Davis', '4 Fourth Street', \
                'debradavis@gmail.com', '4032398596', '2022-04-26'), \
                ('56789', 'Ed Edwards', '5 Fifth Street', \
                'ededed@gmail.com', '4032665740', '2021-03-15')")

mycursor.execute("INSERT INTO Receptionist \
                VALUES (12345)")

mycursor.execute("INSERT INTO Entertainer \
                VALUES (23456)")

mycursor.execute("INSERT INTO Zookeeper \
                VALUES (34567)")

mycursor.execute("INSERT INTO Manager \
                VALUES (45678)")

mycursor.execute("INSERT INTO Store \
                VALUES ('Safari Eatery', 'Restaurant', 45678)")

mycursor.execute("INSERT INTO Other_employee \
                VALUES (56789, 'Safari Eatery')")
                