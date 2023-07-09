# LoginSoftware-Project

I came up with a particular real-world example in creating a software application for CompanyXYZ (example company) and utilized MySql, PySide2, and Python to build an entire full-stack application.
I will be going over the implementation and details throughout this comprehensive readme.

## Real-World Example
A company called CompanyXYZ has requested to create a login panel software application for CompanyXYZ clients, clients should be able to log in with correct credentials. The client should also be able to register themselves. A database is going to be used to connect with the software application.

## What Have I Achieved in This Project

I have achieved the following key features in this project:

- Building small features such as database validation connectivity (handling if there is an error with the database)
- Handling user login credentials
- Utilizing password encryption for the database
- Creating a register feature for the person
- Utilizing MySQL to connect this application
- Some other UI features as well...
## Key Accomplishments

Throughout the development of this project, I have successfully achieved the following milestones:

### Database Validation Connectivity

Implemented a database validation connectivity feature, ensuring smooth communication between the software application and the database. This allows for efficient handling of any potential errors or issues that may arise during the database connection.

### User Login Credentials Handling

Designed a secure mechanism to handle user login credentials, ensuring that only authorized users can access the application. This includes implementing a strong password encryption technique in MySQL utilizing SHA256 to protect sensitive user information in the database.

### User Registration Functionality

Developed a user-friendly registration feature that enables individuals to create an account within the application. This feature ensures a seamless onboarding experience for new users, expanding the potential user base for Company XYZ.

### Utilizing MySQL for Enhanced Functionality

Effectively leveraged the capabilities of MySQL to establish a connection between the application and the database. This integration allows for efficient data storage, retrieval, and management, ensuring a reliable and scalable application.

## Screenshots

I have added an Entity-Relationship (EER) diagram and the corresponding MySQL tables to the project. To get started, we need to create a MySQL database named "logindatabase" and implement the following tables:

- Users Table:
  - UserID: An auto-incremented primary key to uniquely identify each user.
  - PersonName: A non-null field to store the person's name.
  - UserName: A non-null field to store the username.
  - UserPassword: A non-null field to store the user's password.

- LoginInfo Table:
  - LoginInfoID: An auto-incremented primary key to uniquely identify each login information entry.
  - UserID: A foreign key referencing the UserID in the Users table, establishing a relationship between the tables.
  - LastLoginDate: A field to store the date of the last login.
  - Registered: A boolean field that defaults to false, indicating whether the user is registered or not.

Please refer to the following images for more details:

- EER Diagram:
  - ![EER Diagram](https://i.gyazo.com/c4101ff18165d8aae6a63df7853ed799.png)

- Table Structure:
  - ![Table Structure](https://i.gyazo.com/d137b6d65bc77313796c80989616926d.png)
  
Here are some screenshots demonstrating the functionality of the software application:

Using QTDesigner to create the software application as the first steps
![Using QTDesigner to create the software application as the first steps](https://i.gyazo.com/cc1de8f2883724717333eb4a96b588af.png)

This screenshot showcases the initial stage of the application development process using QTDesigner. It demonstrates the visual design of the user interface, allowing you to create and customize the layout of the login panel software application.

Demonstrating a successful login on a database stored account
![Demonstrating a successful login on a database stored account](https://i.gyazo.com/d1a68b08f59f9ffcbe94859d2177989d.gif)

Demonstrating a successful login attempt using credentials stored in the database. It shows the user entering their username and password, and upon successful authentication, the application grants access to the user, allowing them to proceed further.

Demonstrating a not valid account login attempt
![Demonstrating a not valid account login attempt](https://i.gyazo.com/a3fb1037cc6c620dacf830bcfea58cc7.gif)

Demonstrating an unsuccessful login attempt using incorrect credentials. The application validates the entered username and password, and when they are not valid, an error message is displayed, indicating that the login attempt has failed.

Demonstrating a login validation with the database
![Demonstrating a login validation with the database](https://i.gyazo.com/65aa1b375b7829f4a69870a02bf03c5d.gif)

Demonstrating the login validation process with the database. The application communicates with the MySQL database to check the validity of the entered credentials. It demonstrates the connection and interaction between the software application and the database during the login process.

Demonstrating a registered account
![Demonstrating a registered account](https://i.gyazo.com/a436f4c5c5b403af5e0039609eda612c.png)

Demonstrating a visual representation of a registered account within the login panel software application showing a successful registration this is handled in the backend as well.

Now the account can be logged into!
![Now the account can be logged into!](https://i.gyazo.com/34eb7c046c75453dbc7b7219c26d1f97.png
)

It indicates that the user can now log into their account using their created credentials, the UI displays a successful login to the user and as well as a welcome message on the bottom left corner- grabbing the clients name from the database that was used from registering.




## Important Notice

This software application, created as a demonstration of a real-world full-stack software application example, which represents the culmination of my original work and is copyrighted under my ownership. With the GitHub repository being public, it allows individuals to access and test this project. As the creator, I take great pride in showcasing this project to potential employers, providing them with an opportunity to evaluate and interact with the software application. The unique and exclusive nature of this software safeguards it from any unauthorized use, for example; duplication, and or distribution, while enabling public access for examination and testing purposes.

## Credits
- This software utilizes icons from the original owner. Credits to the original icon creators.