import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase"
)

mycursor = mydb.cursor()

# CREATE TABLE statements copied directly from our last project report
mycursor.execute("DROP TABLE IF EXISTS Species")
mycursor.execute("CREATE TABLE Species \
                (Species_name VARCHAR(15) NOT NULL, \
                Category VARCHAR(15), \
                Habitat VARCHAR(15), \
                Lifespan INT NOT NULL, \
                PRIMARY KEY (Species_name))")

mycursor.execute("DROP TABLE IF EXISTS Indoor_complex")
mycursor.execute("CREATE TABLE Indoor_complex \
                (ComplexID CHAR(1) NOT NULL, \
                Address_nbr INT NOT NULL, \
                Street_name VARCHAR(15) NOT NULL, \
                PRIMARY KEY (ComplexID))")

mycursor.execute("DROP TABLE IF EXISTS Enclosure")
mycursor.execute("CREATE TABLE Enclosure \
                (EnclosureID CHAR(6) NOT NULL, \
                Temperature INT, \
                Habitat VARCHAR(15), \
                Length INT, \
                Width INT, \
                Height INT, \
                ComplexID CHAR(1), \
                PRIMARY KEY (EnclosureID), \
                FOREIGN KEY (ComplexID) REFERENCES Indoor_complex(ComplexID))")

mycursor.execute("DROP TABLE IF EXISTS Exhibit")
mycursor.execute("CREATE TABLE Exhibit \
                (ExhibitID CHAR(7) NOT NULL, \
                Start_date DATE NOT NULL, \
                End_date DATE NOT NULL, \
                PRIMARY KEY (ExhibitID))")

mycursor.execute("DROP TABLE IF EXISTS Animal")
mycursor.execute("CREATE TABLE Animal \
                (Name VARCHAR(15) NOT NULL, \
                Birth_date DATE, \
                Sex CHAR(1), \
                Species_name VARCHAR(15) NOT NULL, \
                EnclosureID CHAR(6) NOT NULL, \
                ExhibitID CHAR(7), \
                PRIMARY KEY (Name), \
                FOREIGN KEY (Species_name) REFERENCES Species(Species_name), \
                FOREIGN KEY (EnclosureID) REFERENCES Enclosure(EnclosureID), \
                FOREIGN KEY (ExhibitID) REFERENCES Exhibit(ExhibitID))")

mycursor.execute("DROP TABLE IF EXISTS Employee")
mycursor.execute("CREATE TABLE Employee \
                (EmployeeID CHAR(5) NOT NULL, \
                Name VARCHAR(15), \
                Address VARCHAR(15), \
                Email VARCHAR(20), \
                Phone_number CHAR(10), \
                Start_date DATE, \
                PRIMARY KEY (EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Species_diet")
mycursor.execute("CREATE TABLE Species_diet \
                (Diet VARCHAR(15) NOT NULL, \
                Species_name VARCHAR(15) NOT NULL, \
                CONSTRAINT pk_SpeciesDiet PRIMARY KEY (Diet, Species_name), \
                FOREIGN KEY (Species_name) REFERENCES Species(Species_name))")

mycursor.execute("DROP TABLE IF EXISTS Manager")
mycursor.execute("CREATE TABLE Manager \
                (EmployeeID CHAR(5) NOT NULL, \
                PRIMARY KEY (EmployeeID), \
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Store")
mycursor.execute("CREATE TABLE Store \
                (Store_name VARCHAR(15) NOT NULL, \
                Type VARCHAR(15), \
                Manager_EID CHAR(5) NOT NULL, \
                PRIMARY KEY (Store_name), \
                FOREIGN KEY (Manager_EID) REFERENCES Manager(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Vaccine_recd")
mycursor.execute("CREATE TABLE Vaccine_recd \
                (Vaccine_name VARCHAR(15) NOT NULL, \
                Date DATE NOT NULL, \
                Animal_name VARCHAR(15) NOT NULL, \
                CONSTRAINT pk_VaccineRecd PRIMARY KEY (Vaccine_name, Date, Animal_name), \
                FOREIGN KEY (Animal_name) REFERENCES Animal(Name))")

mycursor.execute("DROP TABLE IF EXISTS Procedure_recd")
mycursor.execute("CREATE TABLE Procedure_recd \
                (Procedure_name VARCHAR(15) NOT NULL, \
                Date DATE NOT NULL, \
                Animal_name VARCHAR(15) NOT NULL, \
                CONSTRAINT pk_ProcedureRecd PRIMARY KEY (Procedure_name, Date, Animal_name), \
                FOREIGN KEY (Animal_name) REFERENCES Animal(Name))")

mycursor.execute("DROP TABLE IF EXISTS Animal_condition")
mycursor.execute("CREATE TABLE Animal_condition \
                (Condition_name VARCHAR(15) NOT NULL, \
                Animal_name VARCHAR(15) NOT NULL, \
                CONSTRAINT pk_AnimalCondition PRIMARY KEY (Condition_name, Animal_name), \
                FOREIGN KEY (Animal_name) REFERENCES Animal(Name))")

mycursor.execute("DROP TABLE IF EXISTS Daily_revenue")
mycursor.execute("CREATE TABLE Daily_revenue \
                (Date DATE NOT NULL, \
                Revenue FLOAT NOT NULL, \
                Store_name VARCHAR(15) NOT NULL, \
                CONSTRAINT pk_DailyRevenue PRIMARY KEY (Date, Revenue, Store_name), \
                FOREIGN KEY (Store_name) REFERENCES Store(Store_name))")

mycursor.execute("DROP TABLE IF EXISTS Inventory_item")
mycursor.execute("CREATE TABLE Inventory_item \
                (Item_price VARCHAR(15) NOT NULL, \
                Item_name DATE NOT NULL, \
                Store_name VARCHAR(15) NOT NULL, \
                CONSTRAINT pk_InventoryItem PRIMARY KEY (Item_price, Item_name, Store_name), \
                FOREIGN KEY (Store_name) REFERENCES Store(Store_name))")

mycursor.execute("DROP TABLE IF EXISTS Zookeeper")
mycursor.execute("CREATE TABLE Zookeeper \
                (EmployeeID CHAR(5) NOT NULL, \
                PRIMARY KEY (EmployeeID), \
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Zookeeper_specialization")
mycursor.execute("CREATE TABLE Zookeeper_specialization \
                (Specialization VARCHAR(15) NOT NULL, \
                Zookeeper_EID CHAR(5) NOT NULL, \
                CONSTRAINT pk_ZookeeperSpecialization PRIMARY KEY (Specialization, Zookeeper_EID), \
                FOREIGN KEY (Zookeeper_EID) REFERENCES Zookeeper(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Entertainer")
mycursor.execute("CREATE TABLE Entertainer \
                (EmployeeID CHAR(5) NOT NULL, \
                PRIMARY KEY (EmployeeID), \
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Entertainer_exhibit")
mycursor.execute("CREATE TABLE Entertainer_exhibit \
                (EmpID CHAR(5) NOT NULL, \
                ExhibitID CHAR(7) NOT NULL, \
                CONSTRAINT pk_EntertainerExhibit PRIMARY KEY (EmpID, ExhibitID), \
                FOREIGN KEY (EmpID) REFERENCES Entertainer(EmployeeID), \
                FOREIGN KEY (ExhibitID) REFERENCES Exhibit(ExhibitID))")

mycursor.execute("DROP TABLE IF EXISTS Other_employee")
mycursor.execute("CREATE TABLE Other_employee \
                (EmployeeID CHAR(5) NOT NULL, \
                Store_name VARCHAR(15), \
                PRIMARY KEY (EmployeeID), \
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID), \
                FOREIGN KEY (Store_name) REFERENCES Store(Store_name))")

mycursor.execute("DROP TABLE IF EXISTS Receptionist")
mycursor.execute("CREATE TABLE Receptionist \
                (EmployeeID CHAR(5) NOT NULL, \
                PRIMARY KEY (EmployeeID), \
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Pass")
mycursor.execute("CREATE TABLE Pass \
                (PassID CHAR(9) NOT NULL, \
                Sold_price FLOAT, \
                Date_issued DATE, \
                Receptionist_EID CHAR(5), \
                PRIMARY KEY (PassID), \
                FOREIGN KEY (Receptionist_EID) REFERENCES Receptionist(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Membership")
mycursor.execute("CREATE TABLE Membership \
                (Email VARCHAR(20) NOT NULL, \
                Member_name VARCHAR(15), \
                Duration INT NOT NULL, \
                PassID CHAR(9) NOT NULL, \
                PRIMARY KEY (Email), \
                FOREIGN KEY (PassID) REFERENCES Pass(PassID))")

mycursor.execute("DROP TABLE IF EXISTS Cares_for")
mycursor.execute("CREATE TABLE Cares_for \
                (Zookeeper_EID CHAR(5) NOT NULL, \
                Species_name VARCHAR(15) NOT NULL, \
                CONSTRAINT pk_CaresFor PRIMARY KEY (Zookeeper_EID, Species_name), \
                FOREIGN KEY (Zookeeper_EID) REFERENCES Zookeeper(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Manager_previousrole")
mycursor.execute("CREATE TABLE Manager_previousrole \
                (Previous_role VARCHAR(15) NOT NULL, \
                Manager_EID CHAR(5) NOT NULL, \
                CONSTRAINT pk_ManagerPreviousrole PRIMARY KEY (Previous_role, Manager_EID), \
                FOREIGN KEY (Manager_EID) REFERENCES Manager(EmployeeID))")

mycursor.execute("DROP TABLE IF EXISTS Ticket")
mycursor.execute("CREATE TABLE Ticket \
                (TicketID CHAR(8) NOT NULL, \
                PassID CHAR(9) NOT NULL, \
                PRIMARY KEY (TicketID), \
                FOREIGN KEY (PassID) REFERENCES Pass(PassID))")

mycursor.execute("DROP TABLE IF EXISTS Fundraiser")
mycursor.execute("CREATE TABLE Fundraiser \
                (FundraiserID CHAR(5) NOT NULL, \
                Theme VARCHAR(15), \
                PRIMARY KEY (FundraiserID))")

mycursor.execute("DROP TABLE IF EXISTS Overlooks")
mycursor.execute("CREATE TABLE Overlooks \
                (Manager_EID INT NOT NULL, \
                FundraiserID CHAR(5) NOT NULL, \
                CONSTRAINT pk_Overlooks PRIMARY KEY (Manager_EID, FundraiserID), \
                FOREIGN KEY (FundraiserID) REFERENCES Fundraiser(FundraiserID))")

mycursor.execute("DROP TABLE IF EXISTS Donor")
mycursor.execute("CREATE TABLE Donor \
                (DonorID CHAR(6) NOT NULL, \
                Name VARCHAR(15), \
                Address VARCHAR(15), \
                Email VARCHAR(20), \
                Phone_number CHAR(10), \
                PRIMARY KEY (DonorID))")

mycursor.execute("DROP TABLE IF EXISTS Donates_to")
mycursor.execute("CREATE TABLE Donates_to \
                (DonorID CHAR(6) NOT NULL, \
                FundraiserID CHAR(5) NOT NULL, \
                Amount FLOAT NOT NULL, \
                Date DATE NOT NULL, \
                CONSTRAINT pk_DonatesTo PRIMARY KEY (DonorID, FundraiserID), \
                FOREIGN KEY (DonorID) REFERENCES Donor(DonorID), \
                FOREIGN KEY (FundraiserID) REFERENCES Fundraiser(FundraiserID))")

mycursor.execute("DROP TABLE IF EXISTS Emp_signin")
mycursor.execute("CREATE TABLE Emp_signin \
                (EmpID CHAR(5) NOT NULL, \
                Password CHAR(10) NOT NULL, \
                CONSTRAINT pk_EmpSignin PRIMARY KEY (EmpID, Password), \
                FOREIGN KEY (EmpID) REFERENCES Employee(EmployeeID))")