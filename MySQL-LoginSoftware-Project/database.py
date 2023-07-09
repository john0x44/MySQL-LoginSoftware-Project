##  Name: database
##  Copyright: © 2023 John0x44. All rights reserved.
##  Author: John0x44
##  Date: 21/06/23 18:10
##  Description: Handling MySQL database connections
            #    Connect to the host database named 'logindatabase' 

import mysql.connector

class SQL:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.user = "root"
        self.host = "localhost"
        self.password = "123456"
        self.database = "logindatabase"

        self.databaseError = False 

    # Connect to database 
    def connectDB(self) -> bool:
        try: 
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("MySQL: Successfully connected")
                return True
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.databaseError = True
            return False
    
    # User login
    def userLogin(self, username, password) -> bool:
        try: 
            print("MySQL: querying Users")
            query = f"SELECT IF(UserPassword = SHA2('{password}', 256), TRUE, FALSE) AS PasswordCheck, UserID FROM Users WHERE UserName = '{username}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()

            # Ok user passed
            if result is not None:
                print("MySQL: querying LoginInfo")
                update_query = f"UPDATE LoginInfo SET LastLoginDate = NOW() WHERE UserID = (SELECT UserID FROM Users WHERE UserName = '{username}')"            
                self.cursor.execute(update_query)
                self.connection.commit()

                return bool(result[0])
            
            # Needs to register 
            return False
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.databaseError = True
            return False
        
    # Register a new user
    def registerUser(self, personName, userName, password) -> bool:
        if not(self.checkUsername(userName)):
            try:
                insert_user_query = f"INSERT INTO Users (PersonName, UserName, UserPassword) VALUES ('{personName}', '{userName}', SHA2('{password}',256))"
                self.cursor.execute(insert_user_query)
                self.connection.commit()
                select_user_id_query = f"SELECT UserID FROM Users WHERE UserName = '{userName}'"
                self.cursor.execute(select_user_id_query)
                insert_login_query = f"INSERT INTO LoginInfo (UserID, LastLoginDate, Registered) VALUES ({self.cursor.fetchone()[0]}, NOW(), TRUE)"
                self.cursor.execute(insert_login_query)
                self.connection.commit()
                return True
            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                self.databaseError = True
                return False
        else:
            return False 

    # Check if username is registered
    def checkUsername(self, username) -> bool:
        try:
            print("MySQL: querying Users")
            query = f"SELECT l.Registered FROM Users u JOIN LoginInfo l ON u.UserID = l.UserID WHERE u.UserName = '{username}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result is not None:
                return bool(result[0])
            else:
                return False
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.databaseError = err
            return False

    # Get Profile name
    def getName(self, username) -> str:
        try:
            print("MySQL: querying Users")
            query = f"SELECT PersonName FROM Users WHERE UserName = '{username}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result is not None:
                return result[0]
            else:
                return ""
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            self.databaseError = True
            return ""

# Testing database
# db = SQL()
# db.connectDB()
# db.registerUser("John","admin","123")
# print(db.userLogin("admin","123"))