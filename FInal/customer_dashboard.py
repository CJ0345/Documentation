from db_connection import Database
import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector

# Customer Dashboard GUI
class CustomerPage(ctk.CTk):
    def __init__(self):
        self.db = Database()
        super().__init__()

        self.title("Customer Dashboard")
        self.geometry("800x550")
        
        self.db = Database()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    

        self.total_products, self.total_orders = self.fetch_dashboard_data()

        self.product_card = ctk.CTkFrame(self, corner_radius=15)
        self.product_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.product_count_label = self._create_card(
        self.product_card, "Products Available", self.total_products, "🛒", self.show_products)

        self.order_card = ctk.CTkFrame(self, corner_radius=15)
        self.order_card.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self._create_card(self.order_card, "My Orders", self.total_orders, "📦", self.show_orders)
        
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

        style = ttk.Style(self)
        style.configure("Treeview", 
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        style.map("Treeview", 
                  background=[('selected', '#347083')])

        self.data_table = ttk.Treeview(self, columns=("ID", "Name", "Price", "Size"), show="headings", style="Treeview")
        self.data_table.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self._setup_table()      
        
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

        label_title = ctk.CTkLabel(frame, text=title, font=("Arial", 18, "bold"), anchor="center")
        label_title.pack(pady=(10, 0))

        label_emoji = ctk.CTkLabel(frame, text=emoji, font=("Arial", 36), anchor="center")
        label_emoji.pack(pady=(5, 0))

        label_count = ctk.CTkLabel(
            frame,
            text=f"{count}",
            font=("Arial", 24),
            anchor="center",
            justify="center"
        )
        label_count.pack(pady=(5, 10))

        frame.bind("<Button-1>", lambda e: command())
        label_title.bind("<Button-1>", lambda e: command())
        label_emoji.bind("<Button-1>", lambda e: command())
        label_count.bind("<Button-1>", lambda e: command())

        return label_count

    def show_products(self):
        window = ctk.CTkToplevel(self)
        window.title("Available Products")
        window.geometry("800x400")
        window.transient(self)
        window.grab_set()

        columns = ["ID", "Name", "Price", "Size"]
        tree = ttk.Treeview(window, columns=columns, show="headings", style="Treeview")
        tree.pack(fill=ctk.BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor= "center", width=100)
            
        conn = self.db.get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, price, size FROM products")
        for row in cursor.fetchall():
            tree.insert("", ctk.END, values=(row[0], row[1], f"₱{row[2]:.2f}", row[3]))

        order_button = ctk.CTkButton(window, text="Place Order", command=lambda: self.show_place_order_tab(tree))
        order_button.pack(side=ctk.LEFT, padx=10, pady=10)

    def show_place_order_tab(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No product selected for order.")
            return

        item_values = tree.item(selected_item, "values")
        product_id = item_values[0]
        product_name = item_values[1]
        product_price = float(item_values[2].strip("₱"))

        self.place_order_tab = ctk.CTkToplevel(self)
        self.place_order_tab.title("Place Order")
        self.place_order_tab.geometry("500x700")
        self.place_order_tab.transient(self)
        self.place_order_tab.grab_set()

        ctk.CTkLabel(self.place_order_tab, text="Place Order", font=("Arial", 24)).pack(pady=20)

        ctk.CTkLabel(self.place_order_tab, text="Product Name:").pack(pady=5)
        ctk.CTkLabel(self.place_order_tab, text=product_name).pack(pady=5)

        ctk.CTkLabel(self.place_order_tab, text="Name:").pack(pady=5)
        self.user_name_entry = ctk.CTkEntry(self.place_order_tab)
        self.user_name_entry.pack(pady=5)

        ctk.CTkLabel(self.place_order_tab, text="Contact Number:").pack(pady=5)
        self.contact_number_entry = ctk.CTkEntry(self.place_order_tab)
        self.contact_number_entry.pack(pady=5)

        ctk.CTkLabel(self.place_order_tab, text="Delivery Address:").pack(pady=5)
        self.address_entry = ctk.CTkEntry(self.place_order_tab)
        self.address_entry.pack(pady=5)

        ctk.CTkLabel(self.place_order_tab, text="Quantity:").pack(pady=5)
        self.quantity_entry = ctk.CTkEntry(self.place_order_tab)
        self.quantity_entry.pack(pady=5)

        ctk.CTkLabel(self.place_order_tab, text="Delivery Date (YYYY-MM-DD):").pack(pady=5)
        self.date_entry = ctk.CTkEntry(self.place_order_tab)
        self.date_entry.pack(pady=5)

        ctk.CTkLabel(self.place_order_tab, text="Delivery Time (HH:MM(24hrs)):").pack(pady=5)
        self.time_entry = ctk.CTkEntry(self.place_order_tab)
        self.time_entry.pack(pady=5)
    
        self.total_price_label = ctk.CTkLabel(self.place_order_tab, text="Total Price: ₱0.00")
        self.total_price_label.pack(pady=10)

        self.product_price = product_price
        self.quantity_entry.bind("<KeyRelease>", self.calculate_total_price)

        ctk.CTkButton(self.place_order_tab, text="Place Order", command=lambda: self.add_to_orders(product_id)).pack(pady=10)

    def calculate_total_price(self, event):
        try:
            quantity = int(self.quantity_entry.get())
            total_price = quantity * self.product_price
            self.total_price_label.configure(text=f"Total Price: ₱{total_price:.2f}")
        except ValueError:
            self.total_price_label.configure(text="Invalid Quantity")

    def add_to_orders(self, product_id):
        try:       
            user_name = self.user_name_entry.get()  
            quantity = int(self.quantity_entry.get())  
            delivery_address = self.address_entry.get()  
            delivery_date = self.date_entry.get()  
            delivery_time = self.time_entry.get()  
            contact_number = self.contact_number_entry.get()

            if not contact_number.isdigit() or len(contact_number) < 7:
                messagebox.showerror("Error", "Please enter a valid contact number.")
                return

            if not user_name or not delivery_address or not delivery_date or not delivery_time or not contact_number:
                messagebox.showerror("Error", "All fields are required.")
                return
            
            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be greater than zero.")
                return

            if not user_name or not delivery_address or not delivery_date or not delivery_time:
                messagebox.showerror("Error", "Name, Address, Delivery Date, and Delivery Time are required.")
                return

            total_price = quantity * self.product_price
            
            conn = self.db.get_db_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO orders 
                (product_id, customer_name, address, contact_number, quantity, delivery_date, delivery_time, total_price) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (product_id, user_name, delivery_address, contact_number, quantity, delivery_date, delivery_time, total_price))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", f"Order added successfully!\nTotal Price: ₱{total_price:.2f}")
            self.place_order_tab.destroy()  
            self.show_dashboard()  

        except ValueError:
            
            messagebox.showerror("Error", "Please enter a valid quantity.")
        except mysql.connector.Error as e:
            
            messagebox.showerror("Database Error", f"An error occurred while placing the order: {str(e)}")
        except Exception as e:
           
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def show_orders(self):
        window = ctk.CTkToplevel(self)
        window.title("My Orders")
        window.geometry("1080x500")
        window.transient(self)
        window.grab_set()

        columns = [
            "Order ID", "Product Name", "Size", "Name", "Address", 
            "Contact Number", "Quantity", "Delivery Date", "Delivery Time", "Total Price"
        ]
        tree = ttk.Treeview(window, columns=columns, show="headings")
        tree.pack(fill=ctk.BOTH, expand=True)

        # Set headings and column configurations
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=120, stretch=False)

        conn = self.db.get_db_connection()
        cursor = conn.cursor()

        # Updated query to include Size from products
        cursor.execute("""
            SELECT 
                orders.id AS order_id,
                products.name AS product_name,
                products.size AS product_size,
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

        # Insert data into the tree view
        for row in cursor.fetchall():
            tree.insert(
                "", ctk.END, 
                values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], f"₱{row[9]:.2f}")
            )

        cursor.close()
        conn.close()

        def delete_order():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No order selected for deletion.")
                return

            item_values = tree.item(selected_item, "values")
            order_id = item_values[0]

            conn = self.db.get_db_connection()  # Reopen connection
            cursor = conn.cursor()
            cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
            conn.commit()
            cursor.close()
            conn.close()
            
            tree.delete(selected_item)
            messagebox.showinfo("Success", "Order deleted successfully!")

        def edit_order():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showerror("Error", "No order selected for editing.")
                return

            item_values = tree.item(selected_item, "values")
            order_id = item_values[0]
            product_name = item_values[1]
            product_size = item_values[2]
            customer_name = item_values[3]
            address = item_values[4]
            contact_number = item_values[5]
            quantity = item_values[6]
            delivery_date = item_values[7]
            delivery_time = item_values[8]
            total_price = float(item_values[9].strip("₱"))

            edit_order_tab = ctk.CTkToplevel(self)
            edit_order_tab.title("Edit Order")
            edit_order_tab.geometry("500x750")
            edit_order_tab.transient(self)
            edit_order_tab.grab_set()

            ctk.CTkLabel(edit_order_tab, text="Product Name:").pack(pady=5)
            ctk.CTkLabel(edit_order_tab, text=product_name).pack(pady=5)

            ctk.CTkLabel(edit_order_tab, text="Product Size:").pack(pady=5)
            ctk.CTkLabel(edit_order_tab, text=product_size).pack(pady=5)
            
            ctk.CTkLabel(edit_order_tab, text="Name:").pack(pady=5)
            user_name_entry = ctk.CTkEntry(edit_order_tab)
            user_name_entry.insert(0, customer_name)
            user_name_entry.pack(pady=5)

            ctk.CTkLabel(edit_order_tab, text="Delivery Address:").pack(pady=5)
            address_entry = ctk.CTkEntry(edit_order_tab)
            address_entry.insert(0, address)
            address_entry.pack(pady=5)

            ctk.CTkLabel(edit_order_tab, text="Contact Number:").pack(pady=5)
            contact_number_entry = ctk.CTkEntry(edit_order_tab)
            contact_number_entry.insert(0, contact_number)
            contact_number_entry.pack(pady=5)

            ctk.CTkLabel(edit_order_tab, text="Quantity:").pack(pady=5)
            quantity_entry = ctk.CTkEntry(edit_order_tab)
            quantity_entry.insert(0, quantity)
            quantity_entry.pack(pady=5)

            ctk.CTkLabel(edit_order_tab, text="Delivery Date (YYYY-MM-DD):").pack(pady=5)
            date_entry = ctk.CTkEntry(edit_order_tab)
            date_entry.insert(0, delivery_date)
            date_entry.pack(pady=5)

            ctk.CTkLabel(edit_order_tab, text="Delivery Time (24hr HH:MM):").pack(pady=5)
            time_entry = ctk.CTkEntry(edit_order_tab)
            time_entry.insert(0, delivery_time)
            time_entry.pack(pady=5)

            total_price_label = ctk.CTkLabel(edit_order_tab, text=f"Total Price: ₱{total_price:.2f}")
            total_price_label.pack(pady=10)

            def calculate_total_price(event):
                try:
                    quantity = int(quantity_entry.get())
                    new_total_price = quantity * (total_price / int(item_values[5]))
                    total_price_label.configure(text=f"Total Price: ₱{new_total_price:.2f}")
                except ValueError:
                    total_price_label.configure(text="Invalid Quantity")

            quantity_entry.bind("<KeyRelease>", calculate_total_price)

            def save_changes():
                try:
                    new_customer_name = user_name_entry.get()
                    new_address = address_entry.get()
                    new_contact_number = contact_number_entry.get()
                    new_quantity = int(quantity_entry.get())
                    new_delivery_date = date_entry.get()
                    new_delivery_time = time_entry.get()
                    new_total_price = new_quantity * (total_price / int(item_values[5]))

                    if not new_customer_name or not new_address or not new_contact_number:
                        messagebox.showerror("Error", "All fields are required.")
                        return

                    conn = self.db.get_db_connection()
                    cursor = conn.cursor()

                    query = """
                        UPDATE orders
                        SET customer_name = %s, address = %s, contact_number = %s, 
                            quantity = %s, delivery_date = %s, delivery_time = %s, total_price = %s
                        WHERE id = %s
                    """
                    cursor.execute(query, (
                        new_customer_name, new_address, new_contact_number, 
                        new_quantity, new_delivery_date, new_delivery_time, 
                        new_total_price, order_id
                    ))

                    conn.commit()
                    cursor.close()
                    conn.close()

                    messagebox.showinfo("Success", "Order updated successfully!")
                    edit_order_tab.destroy()
                    window.destroy()  
                    self.show_orders()  

                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")

            ctk.CTkButton(edit_order_tab, text="Save", command=save_changes).pack(pady=20)
 
        delete_button = ctk.CTkButton(window, text="Delete Order", command=delete_order)
        delete_button.pack(side=ctk.LEFT, padx=10, pady=10)

        edit_button = ctk.CTkButton(window, text="Edit Order", command=edit_order)
        edit_button.pack(side=ctk.LEFT, padx=10, pady=10)

        return delete_order, edit_order

    def update_order(self, order_id, user_name_entry, address_entry, contact_number_entry, quantity_entry, date_entry, time_entry):
        try:
            updated_customer_name = user_name_entry.get()
            updated_address = address_entry.get()
            updated_contact_number = contact_number_entry.get()
            updated_quantity = int(quantity_entry.get())
            updated_delivery_date = date_entry.get()
            updated_delivery_time = time_entry.get()

            if not updated_customer_name or not updated_address or not updated_contact_number or not updated_delivery_date or not updated_delivery_time:
                messagebox.showerror("Error", "All fields are required.")
                return

            original_total_price = float(self.item_values[8].strip("₱"))
            original_quantity = int(self.item_values[5])
            unit_price = original_total_price / original_quantity
            total_price = updated_quantity * unit_price

            conn = self.db.get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE orders
                SET customer_name = %s, address = %s, contact_number = %s, quantity = %s, delivery_date = %s, delivery_time = %s, total_price = %s
                WHERE id = %s
            """, (updated_customer_name, updated_address, updated_contact_number, updated_quantity, updated_delivery_date, updated_delivery_time, total_price, order_id))

            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Order updated successfully!")
            self.edit_order_tab.destroy()
            
            self.show_orders()  
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"An error occurred while updating the order: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def _setup_table(self):
        """Setup the data table for display."""
        self.data_table.heading("#0", text="")
        self.data_table.heading("ID", anchor="center", text="ID")
        self.data_table.heading("Name", anchor="center", text="Name")
        self.data_table.heading("Price", anchor="center", text="Price")
        self.data_table.heading("Size", anchor="center", text="Size")

        self.data_table.column("#0", width=0, stretch=False)
        self.data_table.column("ID", anchor="center", width=50)
        self.data_table.column("Name", anchor="center", width=150)
        self.data_table.column("Price", anchor="center", width=100)
        self.data_table.column("Size", anchor="center", width=100)
        
        conn = self.db.get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        for row in cursor.fetchall():
            self.data_table.insert("", ctk.END, values=(row[0], row[1], f"₱{row[2]:.2f}", row[3]))
            
    def logout(self): 
        messagebox.showinfo("Logout", "You have been logged out.") 
        self.destroy() 

    def clear_frame(self):
        """Clear the current frame.""" 
        for widget in self.winfo_children(): 
            if isinstance(widget, ctk.CTkFrame) or isinstance(widget, ctk.CTkLabel):
                widget.grid_forget()  

    def show_dashboard(self): 
        """Show the dashboard frame.""" 
        self.clear_frame() 

        self.product_card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew") 
        self.order_card.grid(row=0, column=1, padx=20, pady=20, sticky="nsew") 


if __name__ == "__main__":
    app = CustomerPage()
    app.mainloop()
