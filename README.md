# <p align="center"> &nbsp;&nbsp;&nbsp;&nbsp; Kakanin Hub: </p>
## <p align="center"> Streamlined Ordering and Inventory System </p>

# I. PROJECT OVERVIEW

### Rationale
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp; Kakanin Hub was conceived to address the unique challenges faced by Filipino rice cake (kakanin) businesses. Traditional kakanin makers often struggle with manual processes that lead to inefficiencies, such as managing orders, tracking inventory, and maintaining customer information. By leveraging modern technology, Kakanin Hub aims to streamline these operations, reduce waste, and enhance customer satisfaction, thereby preserving the authenticity of Filipino rice cakes while embracing innovative practices.</p>

### Scope and Limitation
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;Kakanin Hub encompasses various functionalities aimed at streamlining the operations of kakanin businesses. It simplifies order management, tracks inventory levels in real-time, and manages customer information, providing an intuitive user interface that enhances workflow efficiency and customer satisfaction. However, the platform does have some limitations, including the necessity of a reliable internet connection and basic technological infrastructure for optimal functionality. Additionally, while it offers a wide range of features, highly specific customizations may require further development. Users might also face an initial learning curve, particularly if they are not technologically inclined. Despite these challenges, Kakanin Hub is a powerful tool for modernizing traditional kakanin businesses.</p>

### Goal and Target
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp; The primary goal of Kakanin Hub is to modernize the operations of kakanin businesses by integrating technology into their traditional processes, thereby improving efficiency, reducing waste, and elevating customer experience. The platform is designed for traditional kakanin makers who wish to modernize their business operations, as well as new entrepreneurs entering the kakanin market. It aims to support small to medium-sized kakanin businesses that value both tradition and innovation, ensuring a smooth and efficient operation from the outset.</p>

# II. PYTHON CONCEPTS AND LIBRARIES

### Python Concepts

 ### Classes and Objects:
  &nbsp;&nbsp;&nbsp;&nbsp; The script defines a Login class that inherits from ctk.CTk. This class encapsulates the functionality of the login and signup interface. Methods like __init__, create_login_frame, create_signup_frame, signup, and login define the behavior of the Login class.

### Functions:
   &nbsp;&nbsp;&nbsp;&nbsp; Methods within the class (create_login_frame, create_signup_frame, signup, login) are defined using the def keyword. These methods perform specific tasks related to the login and signup process.

 ### Conditionals:
   &nbsp;&nbsp;&nbsp;&nbsp; The script uses conditional statements (if, else, elif) to check conditions and execute corresponding code blocks, such as verifying if fields are filled out or if passwords match.

 ### Error Handling:
   &nbsp;&nbsp;&nbsp;&nbsp;Error handling is implemented using try-except blocks to catch and handle exceptions that may occur during database operations.

 ### GUI Elements:
  &nbsp;&nbsp;&nbsp;&nbsp; The script creates and manages graphical user interface (GUI) elements like frames, labels, entries, and buttons using the customtkinter library.

### Python Libraries

 ### Tkinter:
   &nbsp;&nbsp;&nbsp;&nbsp; tkinter is a standard Python library used for creating GUIs. It provides various widgets like labels, buttons, and entries to create interactive interfaces.

 ### Customtkinter (ctk):
   &nbsp;&nbsp;&nbsp;&nbsp; customtkinter is an enhanced version of tkinter that provides modern themes and styles. It allows for better customization and a more polished look for the GUI.

 ### Messagebox:
   &nbsp;&nbsp;&nbsp;&nbsp; Part of tkinter, messagebox is used to display various types of message boxes (error, info, warning) to interact with users.

 ### Bcrypt:
   &nbsp;&nbsp;&nbsp;&nbsp; bcrypt is a library for hashing passwords. It ensures that passwords are securely hashed before being stored in the database, enhancing security.

 ### Mysql.connector:
   &nbsp;&nbsp;&nbsp;&nbsp; mysql.connector is a library for connecting to MySQL databases from Python. It allows for executing SQL queries and interacting with the database.

 ### Database Connection:
   &nbsp;&nbsp;&nbsp;&nbsp; The script imports a custom Database class from db_connection, which is likely designed to handle database connections and interactions.

 ### Admin and Customer Pages:
   &nbsp;&nbsp;&nbsp;&nbsp; AdminPage and CustomerPage are imported from admin_page and customer_dashboard, respectively. These likely define the interfaces and functionalities for admin and customer roles.

# III. SUSTAINABLE DEVELOPMENT GOAL (SDG)
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;The Kakanin Hub project integrates Sustainable Development Goal (SDG) 8 through its features and functionalities. It serves as a platform for small businesses, enabling them to transition into the digital space, thereby empowering them to reach wider audiences and enhance their market presence. Through the AdminPage and CustomerPage features, the app facilitates efficient management of users, data, and orders, ensuring streamlined business operations while promoting accessibility and customer satisfaction. By fostering customer engagement and driving revenue, the application supports economic participation. Its robust authentication and secure database practices build trust with users, ensuring the safety of user data through password hashing, which promotes trust and reliability in the platform. Additionally, the application lays the foundation for further development of similar projects, promoting skills and technological literacy for developers and entrepreneurs. Future potential for further integration includes offering features for business analytics, supporting entrepreneurs with tools like order management and customer feedback, and introducing features for collaboration with local producers. Integration with SDG 12 involves incorporating sustainable practices such as promoting locally sourced products and reducing waste in the business process. Overall, the project supports small-scale businesses while aligning with broader sustainable development objectives by fostering growth, inclusivity, and security.</p>

# IV. Instructions for Running the Kakanin Hub Program

**Run the program.**
   - First things first, make sure everything is set up correctly. Check for any errors and ensure the program runs smoothly.

**Enter your command choice.**
   - Once the program is running, you'll see a menu with several options. Here's what each one does:

   • **Login and Signup:**
     - When you start the program, you'll see the login screen. If you're new, click "Signup" and fill out the details. Once registered, you'll see a message saying, "Account registered successfully." Then, log in using your new credentials.

   • **Admin Dashboard:**
     - Log in using the admin credentials (`admin@gmail.com` and `admin123`). This will take you to the admin dashboard, where you can manage users, view order histories, and handle inventory. You'll see a "Admin logged in successfully" message.

   • **Customer Dashboard:**
     - If you log in with a customer account, you'll access the customer dashboard. Here, you can place orders, track them, manage your account details, and view your order history. A "Customer logged in successfully" message will confirm your login.

   • **Manage Inventory:**
     - As an admin, you can add new products, update existing ones, and view the entire inventory. Select the appropriate option to manage your inventory, and you'll see a "Inventory updated successfully" message.

   • **Order Management:**
     - In the customer dashboard, you can place orders for the available kakanin. Choose the item you want, specify the quantity, and complete your order. The system will update the inventory automatically. A "Order placed successfully" message will appear once you're done.

   • **View Order History:**
     - Both admins and customers can view the order history to track past transactions. This feature gives you detailed information about previous orders. When you use this option, you'll see an "Order history displayed successfully" message.

   • **Exit:**
     - When you're done, you can exit the program by selecting the exit option. The console will close, and you can restart the program if needed. A message saying, "Program exited successfully" will confirm the exit.

**Exit the console.**
   - Choosing the exit option will automatically close the program. If you need to use it again, simply run the program to start over.




