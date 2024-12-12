from db_connection import Database
import customtkinter as ctk
from tkinter import ttk, messagebox

# Admin Dashboard GUI
class AdminPage(ctk.CTk):
    def __init__(self):
        self.db = Database()
        super().__init__()

        self.db = Database()  
        self.title("Admin Dashboard")
        self.geometry("800x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.inventory_window = None  

        self.total_products, self.total_orders = self.fetch_dashboard_data()

        self.product_card = ctk.CTkFrame(self, corner_radius=15)
        self.product_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.product_count_label = self._create_card(
        self.product_card, "Inventory", self.total_products, "📦", self.show_inventory)

        self.order_card = ctk.CTkFrame(self, corner_radius=15)
        self.order_card.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self._create_card(self.order_card, "Orders", self.total_orders, "🛒", self.show_orders)

        self.logout_frame = ctk.CTkFrame(self, corner_radius=15)
        self.logout_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="e")

        self.logout_button = ctk.CTkButton(
            self.logout_frame,
            text="🚪← Sign Out",
            fg_color="#1C70C8",
            text_color="white",
            command=self.logout
        )
        
        self.logout_button.bind("<Enter>", lambda event: self.logout_button.configure(fg_color="#BF111D"))
        self.logout_button.bind("<Leave>", lambda event: self.logout_button.configure(fg_color="#1C70C8"))
        
        self.logout_button.pack(pady=10, padx=10)

        self.data_table = ttk.Treeview(self, columns=("ID", "Name", "Price", "Size"), show="headings")
        self.data_table.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self._setup_table()
        self.refresh_table_data()

    def fetch_dashboard_data(self):
        """Fetch stats for the dashboard."""
        try:
            print("Fetching dashboard data...")  
            conn = self.db.get_db_connection()  
            print("Connection fetched:", conn)  

            if not conn:
                raise Exception("Failed to connect to the database.")

            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM products")
            total_products = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM orders")
            total_orders = cursor.fetchone()[0]

            conn.close()
            return total_products, total_orders
        except Exception as e:
            print(f"Error fetching dashboard data: {e}")
            return 0, 0

    def _create_card(self, frame, title, count, emoji, command):
        """Helper to create a dashboard card."""
        frame.grid_propagate(False)

        ctk.CTkLabel(frame, text=title, font=("Arial", 18, "bold"), anchor="center").pack(pady=(10, 0))

        ctk.CTkLabel(frame, text=emoji, font=("Arial", 36), anchor="center").pack(pady=(5, 0))

        label_count = ctk.CTkLabel(frame, text=f"{count}", font=("Arial", 24), anchor="center")
        label_count.pack(pady=(5, 10))

        frame.bind("<Button-1>", lambda e: command())
        return label_count

    def _setup_table(self):
        """Setup the main data table."""
        self.data_table.heading("ID", text="ID")
        self.data_table.heading("Name", text="Name")
        self.data_table.heading("Price", text="Price")
        self.data_table.heading("Size", text="Size")

        self.data_table.column("ID", anchor="center", width=50)
        self.data_table.column("Name", anchor="center", width=150)
        self.data_table.column("Price", anchor="center", width=100)
        self.data_table.column("Size", anchor="center", width=100)

    def refresh_table_data(self):
        """Refresh data displayed in the table."""
        try:
            for item in self.data_table.get_children():
                self.data_table.delete(item)

            conn = self.db.get_db_connection() 
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            for row in cursor.fetchall():
                self.data_table.insert("", ctk.END, values=row)

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error refreshing table data: {e}")

    def show_inventory(self):
        """Show inventory management window."""
        if self.inventory_window is not None and self.inventory_window.winfo_exists():
            self.inventory_window.lift() 
            return

        self.inventory_window = ctk.CTkToplevel(self)
        self.inventory_window.title("Inventory")
        self.inventory_window.geometry("800x400")

        self.inventory_window.attributes("-topmost", True)

        columns = ["ID", "Name", "Price", "Size"]
        tree = ttk.Treeview(self.inventory_window, columns=columns, show="headings")
        tree.pack(fill=ctk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        conn = self.db.get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, size FROM products")
        for row in cursor.fetchall():
            tree.insert("", ctk.END, values=row)

        conn.close()

        ctk.CTkButton(self.inventory_window, text="Add Product", command=self.add_product_form).pack(side=ctk.LEFT, padx=10, pady=10)
        ctk.CTkButton(self.inventory_window, text="Edit Product", command=lambda: self.edit_product(tree)).pack(side=ctk.LEFT, padx=10, pady=10)
        ctk.CTkButton(self.inventory_window, text="Delete Product", command=lambda: self.delete_product(tree)).pack(side=ctk.LEFT, padx=10, pady=10)

    def add_product_form(self):
        """Show form to add a product."""
        form_window = ctk.CTkToplevel(self)
        form_window.title("Add Product")
        form_window.geometry("400x300")

        form_window.attributes("-topmost", True)
        
        form_window.transient(self) 
        form_window.grab_set()  
        form_window.focus_set()

        ctk.CTkLabel(form_window, text="Product Name:").pack(pady=5)
        product_name = ctk.CTkEntry(form_window)
        product_name.pack(pady=5)

        ctk.CTkLabel(form_window, text="Price:").pack(pady=5)
        product_price = ctk.CTkEntry(form_window)
        product_price.pack(pady=5)

        ctk.CTkLabel(form_window, text="Size:").pack(pady=5)
        product_size = ctk.CTkEntry(form_window)
        product_size.pack(pady=5)

        ctk.CTkButton(
            form_window,
            text="Add",
            command=lambda: self.add_product(product_name, product_price, product_size, form_window),
        ).pack(pady=10)

    def add_product(self, name, price, size, form_window):
        """Add a product to the database."""
        try:
            product_name = name.get().strip()
            product_price = float(price.get().strip())
            product_size = size.get().strip()

            if not product_name or not product_price or not product_size:
                raise ValueError("All fields are required!")

            conn = self.db.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, price, size) VALUES (%s, %s, %s)", (product_name, product_price, product_size))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Product added successfully!")
            form_window.destroy()
            self.refresh_table_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error adding product: {e}")
            
    def edit_product(self, tree):
        """Edit selected product."""
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Product", "Please select a product to edit.")
            return

        product_data = tree.item(selected_item)["values"]
        product_id, product_name, product_price, product_size = product_data

        # Create a form for editing
        form_window = ctk.CTkToplevel(self)
        form_window.title("Edit Product")
        form_window.geometry("400x300")
        
        form_window.transient(self)
        form_window.grab_set()
        form_window.focus_set()

        ctk.CTkLabel(form_window, text="Product Name:").pack(pady=5)
        name_entry = ctk.CTkEntry(form_window)
        name_entry.insert(0, product_name)
        name_entry.pack(pady=5)

        ctk.CTkLabel(form_window, text="Price:").pack(pady=5)
        price_entry = ctk.CTkEntry(form_window)
        price_entry.insert(0, product_price)
        price_entry.pack(pady=5)

        ctk.CTkLabel(form_window, text="Size:").pack(pady=5)
        size_entry = ctk.CTkEntry(form_window)
        size_entry.insert(0, product_size)
        size_entry.pack(pady=5)

        def update_product():
            """Update product in database."""
            new_name = name_entry.get().strip()
            new_price = price_entry.get().strip()
            new_size = size_entry.get().strip()

            if not new_name or not new_price or not new_size:
                messagebox.showwarning("Validation Error", "All fields are required!")
                return

            try:
                conn = self.db.get_db_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE products SET name = %s, price = %s, size = %s WHERE id = %s",
                    (new_name, new_price, new_size, product_id)
                )
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Product updated successfully!")
                form_window.destroy()
                self.refresh_table_data()
            except Exception as e:
                messagebox.showerror("Error", f"Error updating product: {e}")

        ctk.CTkButton(form_window, text="Update", command=update_product).pack(pady=10)
        
    def delete_product(self, tree):
        """Delete selected product."""
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Product", "Please select a product to delete.")
            return

        product_id = tree.item(selected_item)["values"][0]

        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete Product ID {product_id}?")
        if not confirm:
            return

        try:
            conn = self.db.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            conn.commit()
            conn.close()

            tree.delete(selected_item)
            messagebox.showinfo("Success", f"Product ID {product_id} deleted successfully!")
            self.refresh_table_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting product: {e}")

    def show_orders(self):
        """Show orders management window."""
        window = ctk.CTkToplevel(self)
        window.title("Orders")
        window.geometry("990x500")
        window.attributes("-topmost", True)

        columns = ["Order ID", "Product Name", "Name", "Address", "Contact Number", "Quantity", "Delivery Date", "Delivery Time", "Total Price"]
        tree = ttk.Treeview(window, columns=columns, show="headings")
        tree.pack(fill=ctk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        try:
            conn = self.db.get_db_connection()
            cursor = conn.cursor()

            cursor.execute(""" 
           SELECT 
                orders.id AS order_id,
                products.name AS product_name,
                orders.customer_name,
                orders.address,
                orders.contact_number,
                orders.quantity,
                orders.delivery_date,
                orders.delivery_time,
                orders.total_price
            FROM orders
            JOIN products ON orders.product_id = products.id

                """)

            for row in cursor.fetchall():
                tree.insert("", ctk.END, values=row)

            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching orders: {e}")

        ctk.CTkButton(window, text="Delete Order", command=lambda: self.delete_order(tree)).pack(side=ctk.LEFT, padx=10, pady=10)
        ctk.CTkButton(window, text="Print Order", command=lambda: self.print_order(tree)).pack(side=ctk.LEFT, padx=10, pady=10)
     
    def delete_order(self, tree):
        """Delete selected order from the table and database."""
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Order", "Please select an order to delete.")
            return

        order_id = tree.item(selected_item)["values"][0] 

        try:

            window = ctk.CTkToplevel(self)
            window.title("Confirm Deletion")
            window.geometry("300x150")
            window.attributes("-topmost", True) 
            window.focus_set() 
            
            window.grab_set()

            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete Order ID {order_id}?")
            
            if not confirm:
                window.destroy()  
                return

            conn = self.db.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
            conn.commit()
            conn.close()

            tree.delete(selected_item)

            messagebox.showinfo("Success", f"Order ID {order_id} deleted successfully!")
            window.destroy()  

        except Exception as e:
            messagebox.showerror("Error", f"Error deleting order: {e}")

    def print_order(self, tree):
        """Print selected order details."""
        
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Select Order", "Please select an order to print.")
            return

        order_data = tree.item(selected_item)["values"]
        order_details = f"""
            Order ID: {order_data[0]}
            Item: {order_data[1]}
            Customer: {order_data[2]}
            Address: {order_data[3]}
            Contact Number:{order_data[4]}
            Quantity: {order_data[5]}
            Delivery Date: {order_data[6]}
            Delivery Time: {order_data[7]}
            Total Price: {order_data[8]}
            """  
        try:

            window = ctk.CTkToplevel(self)
            window.title("Order Details")
            window.geometry("400x300")
            window.attributes("-topmost", True)  
            window.focus_set()  

            window.grab_set()

            order_label = ctk.CTkLabel(window, text=order_details, justify="left", font=("Arial", 12))
            order_label.pack(padx=20, pady=20)

            close_button = ctk.CTkButton(window, text="Close", command=window.destroy)
            close_button.pack(side=ctk.BOTTOM, pady=10)
        
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying order details: {e}")
    def logout(self): 
        messagebox.showinfo("Logout", "You have been logged out.") 
        self.destroy() 
            

# Start the app
if __name__ == "__main__":
    app = AdminPage()
    app.mainloop()