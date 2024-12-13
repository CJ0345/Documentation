# <p align="center"> &nbsp;&nbsp;&nbsp;&nbsp; Kakanin Hub: </p>
## <p align="center"> Streamlined Ordering and Inventory System </p>

# I. PROJECT OVERVIEW

### Rationale

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbspKakanin Hub is more than just a management system; it's a lifeline for Filipino rice cake (kakanin) businesses. These traditional sweets are a beloved part of Filipino culture, but the small-scale producers who make them often face significant challenges due to outdated manual processes. Kakanin Hub steps in to address these issues, offering a streamlined solution that simplifies ordering, tracks inventory, and provides real-time updates on product availability. This ensures that kakanin producers can efficiently meet customer demand. By integrating modern digital tools, Kakanin Hub preserves the cultural heritage of Filipino rice cakes while bringing innovation to the production and distribution process. It's designed specifically to help small to medium-sized kakanin businesses reduce waste, improve workflow, and enhance the overall customer experience.</p>

### Scope and Limitations

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbspKakanin Hub focuses on automating essential operations for kakanin businesses, making everyday tasks more manageable and efficient. The system includes features such as order management, which simplifies how orders are processed and tracked, ensuring accuracy and efficiency. Inventory tracking provides real-time updates on inventory levels to help minimize waste and ensure products are available when needed. Customer data management stores and manages customer information to enhance engagement and provide personalized services. Additionally, the user-friendly interface is designed with ease of use in mind, making it simple for users to manage orders and view order history. However, the system does not manage employee payroll, accounting tasks, or offer advanced business analytics and reporting tools. It also lacks direct support for e-commerce integration. These limitations mean the primary focus is on improving operational efficiency and customer satisfaction for kakanin producers, rather than handling all aspects of business operations.</p>

### Goals and Targets

<p align="justify"> &nbsp;&nbsp;&nbsp;&nbspThe primary goal of Kakanin Hub is to bring Filipino kakanin businesses into the modern era with a user-friendly and efficient management platform. By implementing real-time inventory monitoring, the project aims to reduce product waste by 50% within the first year of operation. Automated tracking and management tools are expected to improve order fulfillment accuracy by 80%, ensuring that customer orders are handled more efficiently and accurately. Furthermore, by offering personalized order histories and updates, Kakanin Hub aims to enhance customer retention within six months of deployment. These targets are designed to help kakanin makers maintain the authenticity of their traditional products while equipping them with the tools needed to stay competitive in today’s market.</p>






# II. PYTHON CONCEPTS AND LIBRARIES

### Python Tkinter

<p align="justify"> &nbsp;&nbsp;&nbsp;Python Tkinter is a standard graphical user interface library available in Python that provides access to widgets such as labels, buttons, and frames. In this program, the Tkinter library was primarily used for GUI applications, including creating labels, frames, and input fields. The `ttk` module within the Python Tkinter library was also utilized to enhance the appearance of widgets, particularly for displaying data in a tree-like structure using the Treeview widget.</p>

### CustomTkinter

<p align="justify"> &nbsp;&nbsp;&nbsp;CustomTkinter is an advanced UI library based on Tkinter that offers more modern and customizable widgets. This library was extensively used throughout the program to create sleek and polished graphical interfaces. CustomTkinter provides a wide range of customization options, allowing developers to design unique and visually appealing GUIs. Its compatibility with the default Tkinter elements ensures seamless integration, making it an ideal choice for modern GUI development.</p>

### MySQL

<p align="justify"> &nbsp;&nbsp;&nbsp;The program utilizes the *mysql.connector* library to handle MySQL queries and connections. This library offers a comprehensive set of tools for establishing connections to a MySQL database, executing SQL queries, and managing database transactions. The MySQL library is crucial for the program's functionality, enabling efficient data retrieval and storage. By leveraging this library, the program ensures secure and reliable interaction with the database, supporting various operations such as user authentication, order management, and inventory tracking.</p>



# III. SUSTAINABLE DEVELOPMENT GOAL (SDG)
<p align="justify"> &nbsp;&nbsp;&nbsp;&nbsp;The Kakanin Hub project integrates Sustainable Development Goal (SDG) 8 through its features and functionalities. It serves as a platform for small businesses, enabling them to transition into the digital space, thereby empowering them to reach wider audiences and enhance their market presence. Through the AdminPage and CustomerPage features, the app facilitates efficient management of users, data, and orders, ensuring streamlined business operations while promoting accessibility and customer satisfaction. By fostering customer engagement and driving revenue, the application supports economic participation. Its robust authentication and secure database practices build trust with users, ensuring the safety of user data through password hashing, which promotes trust and reliability in the platform. Additionally, the application lays the foundation for further development of similar projects, promoting skills and technological literacy for developers and entrepreneurs. Future potential for further integration includes offering features for business analytics, supporting entrepreneurs with tools like order management and customer feedback, and introducing features for collaboration with local producers. Integration with SDG 12 involves incorporating sustainable practices such as promoting locally sourced products and reducing waste in the business process. Overall, the project supports small-scale businesses while aligning with broader sustainable development objectives by fostering growth, inclusivity, and security.</p>

# IV. INSTRUCTIONS FOR RUNNING THE Kakanin Hub Program

# Kakanin Hub Setup Guide

## 1. Set Up the Database
1. **Navigate to the program files:**
   - Open the directory where the *kakanin_hub* database file is located.

2. **Import the database using phpMyAdmin:**
   - Open phpMyAdmin.
   - Log in with your MySQL credentials.
   - Select the Databases tab and create a new database or select an existing one.
   - Use the Import tab to upload and import the *kakanin_hub* database file into the selected database.

3. **Start the MySQL database using XAMPP:**
   - Open your XAMPP Control Panel.
   - Start the MySQL service. It should show as running once started.

## 2. Install Dependencies
1. **Open the terminal or command prompt:**
   - On Windows, you can open Command Prompt (cmd) or PowerShell.

2. **Navigate to the project directory.**

3. **Install necessary Python packages:**
   - Run the following command to install the required dependencies:

*pip install customtkinter bcrypt mysql-connector-python*
  

## 3. Start the Program
1. **Run the script:**
   - Execute *login.py*.

### Important Notes:
 This will take you to the admin dashboard:
- **Username:** *admin@gmail.com*
- **Password:** *admin123*

