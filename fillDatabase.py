import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase",
    auth_plugin='mysql_native_password',
    autocommit = True
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO Species \
                VALUES ('Lion', 'Feline', 'Savannah', 12, 'Carnivore'), \
                ('Squirrel', 'Rodent', 'Forest', 4, 'Omnivore'), \
                ('Buffalo', 'Bovine', 'Plains', 25, 'Herbivore'), \
                ('Platypus', 'Monotreme', 'Small Creeks', 7, 'Carnivore'), \
                ('Macaw', 'Parrot', 'Rainforest', 85, 'Herbivore')")

mycursor.execute("INSERT INTO Indoor_complex \
                VALUES ('1', 5426, 'Zoo Boulevard'), \
                ('2', 389, 'Zoo Avenue')")

mycursor.execute("INSERT INTO Enclosure \
                VALUES ('462736', 21, 'Plains', 40, 50, 20, 2), \
                ('238849', -20, 'Antarctic', 20, 30, 20, '1'), \
                ('171702', 25, 'Small Creeks', 40, 30, 10, '1'), \
                ('350586', 28, 'Savannah', 50, 40, NULL, NULL)")

mycursor.execute("INSERT INTO Exhibit \
                VALUES ('8675309', 'History', '2022-11-18', '2022-12-18'), \
                ('0951287', 'Nocturnal', '2022-03-08', '2022-03-31'), \
                ('3863048', 'Polar', '2013-05-16', '2013-07-24'), \
                ('8324767', 'Birds', '2022-12-01', '2023-01-05'), \
                ('9672122', 'Africa', '2022-11-29', '2022-12-10'), \
                ('5432235', 'Freshwater', '2016-08-15', '2016-09-15'), \
                ('6823527', 'Asia', '2019-12-02', '2020-03-14')")

mycursor.execute("INSERT INTO Animal \
                VALUES ('Rex', '2016-07-15', 'M', 'Lion', '350586', NULL), \
                ('Fluffy', '2013-06-25', 'F', 'Buffalo', '462736', NULL), \
                ('Buddy', NULL, 'M', 'Platypus', '171702', '8675309')")

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

mycursor.execute("INSERT INTO Emp_signin \
                VALUES ('12345', 'password1'), \
                ('23456', 'password2'), \
                ('34567', 'password3'), \
                ('45678', 'password4'), \
                ('56789', 'password5')")

mycursor.execute("INSERT INTO Manager \
                VALUES ('45678'), \
                ('12345')")

mycursor.execute("INSERT INTO Store \
                VALUES ('Safari Eatery', 'Restaurant', '45678'), \
                ('Jungle Fun', 'Souvenir Shop', '45678'), \
                ('Coming Soon', NULL, '45678')")

mycursor.execute("INSERT INTO Daily_revenue \
                VALUES ('2022-11-29', 1024.98, 'Jungle Fun'), \
                ('2022-11-28', 1209.67, 'Jungle Fun'), \
                ('2022-11-27', 1057.34, 'Jungle Fun'), \
                ('2022-11-26', 989.26, 'Jungle Fun'), \
                ('2022-11-25', 1138.94, 'Jungle Fun'), \
                ('2022-11-24', 1055.62, 'Jungle Fun'), \
                ('2022-11-23', 1093.99, 'Jungle Fun'), \
                ('2022-11-22', 1370.25, 'Jungle Fun'), \
                ('2022-11-21', 1254.10, 'Jungle Fun'), \
                ('2022-11-20', 1072.81, 'Jungle Fun'), \
                ('2022-11-19', 1195.87, 'Jungle Fun'), \
                ('2022-11-18', 953.97, 'Jungle Fun'), \
                ('2022-11-17', 1029.63, 'Jungle Fun'), \
                ('2022-11-16', 1176.28, 'Jungle Fun'), \
                ('2022-11-15', 1068.70, 'Jungle Fun'), \
                ('2022-11-29', 1439.28, 'Safari Eatery'), \
                ('2022-11-28', 1304.99, 'Safari Eatery'), \
                ('2022-11-27', 1192.54, 'Safari Eatery'), \
                ('2022-11-26', 1478.81, 'Safari Eatery'), \
                ('2022-11-27', 1503.50, 'Safari Eatery'), \
                ('2022-11-26', 1294.46, 'Safari Eatery'), \
                ('2022-11-25', 1372.60, 'Safari Eatery'), \
                ('2022-11-24', 1265.57, 'Safari Eatery'), \
                ('2022-11-23', 1119.13, 'Safari Eatery'), \
                ('2022-11-22', 1431.42, 'Safari Eatery'), \
                ('2022-11-21', 1585.25, 'Safari Eatery'), \
                ('2022-11-20', 1329.65, 'Safari Eatery'), \
                ('2022-11-19', 1216.79, 'Safari Eatery'), \
                ('2022-11-18', 1373.08, 'Safari Eatery')")

mycursor.execute("INSERT INTO Zookeeper \
                VALUES ('34567')")

mycursor.execute("INSERT INTO Zookeeper_specialization \
                VALUES ('Big Cats', '34567')")

mycursor.execute("INSERT INTO Entertainer \
                VALUES ('23456')")

mycursor.execute("INSERT INTO Other_employee \
                VALUES ('56789', 'Safari Eatery')")

mycursor.execute("INSERT INTO Receptionist \
                VALUES ('12345')")

mycursor.execute("INSERT INTO Pass \
                VALUES ('525630021', 89.99, '2022-11-29', '12345'), \
                ('412967039', 89.99, '2014-02-14', '12345'), \
                ('920475018', 15.99, '2022-09-17', '12345'), \
                ('076139023', 15.99, '2015-04-21', '12345')")

mycursor.execute("INSERT INTO Membership \
                VALUES ('member1@gmail.com', 'Andrew Evans', 30, '525630021'), \
                ('member2@gmail.com', 'Rachel Smith', 13, '412967039')")

mycursor.execute("INSERT INTO Cares_for \
                VALUES ('34567', 'Lion'), \
                ('34567', 'Buffalo'), \
                ('34567', 'Platypus')")

mycursor.execute("INSERT INTO Manager_previousrole \
                VALUES ('Receptionist', '45678'), \
                ('Zookeeper', '45678')")

mycursor.execute("INSERT INTO Ticket \
                VALUES ('47628197', '920475018'), \
                ('13829400', '076139023')")

mycursor.execute("INSERT INTO Fundraiser \
                VALUES ('26930', 'Christmas'), \
                ('59104', 'Earth Day'), \
                ('07183', 'Thanksgiving')")

mycursor.execute("INSERT INTO Overlooks \
                VALUES ('45678', '26930'), \
                ('45678', '59104'), \
                ('12345', '07183')")

mycursor.execute("INSERT INTO Donor \
                VALUES ('392058', 'Ernie Paulson', '34 Donorly Street', \
                'erniepson@gmail.com', '4032680719', 45000), \
                ('145824', 'Bert Morrisson', '16 Donormy Street', \
                'bertm45@gmail.com', '4032887214', 137000), \
                ('879302', 'Oscar Erikson', '90 Donorfy Street', \
                'oscar8282@gmail.com', '4035067985', 1475000)")

mycursor.execute("INSERT INTO Donates_to \
                VALUES ('392058', '26930', 15000.00, '2019-12-23'), \
                ('145824', '59104', 500000.00, '2017-04-22'), \
                ('879302', '07183', 5500.00, '2022-10-10')")
