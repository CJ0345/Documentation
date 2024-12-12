import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from db_connection import Database
import bcrypt
from admin_page import AdminPage  
from customer_dashboard import CustomerPage  
import mysql.connector

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("KAKANIN_HUB Login")
        self.geometry("500x400")
        self.resizable(False, False)

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()

        self.login_frame = ctk.CTkFrame(self, corner_radius=10)
        self.login_frame.pack(pady=20, padx=60, fill="both", expand=True)

        ctk.CTkLabel(self.login_frame, text="Login", font=("Poppins", 20)).pack(pady=12)

        self.email_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Email")
        self.email_entry.pack(pady=10, padx=10)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10, padx=10)

        ctk.CTkButton(self.login_frame, text="Login", command=self.login).pack(pady=12)

        ctk.CTkButton(self.login_frame, text="Signup", command=self.create_signup_frame).pack()

    def create_signup_frame(self):
        self.clear_frame()

        self.signup_frame = ctk.CTkFrame(self, corner_radius=10)
        self.signup_frame.pack(pady=20, padx=60, fill="both", expand=True)

        ctk.CTkLabel(self.signup_frame, text="Signup", font=("Poppins", 20)).pack(pady=12)

        self.signup_email_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="Email")
        self.signup_email_entry.pack(pady=10, padx=10)

        self.signup_password_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="Password", show="*")
        self.signup_password_entry.pack(pady=10, padx=10)

        self.confirm_password_entry = ctk.CTkEntry(self.signup_frame, placeholder_text="Confirm Password", show="*")
        self.confirm_password_entry.pack(pady=10, padx=10)

        ctk.CTkButton(self.signup_frame, text="Signup", command=self.signup).pack(pady=12)

        ctk.CTkButton(self.signup_frame, text="Back to Login", command=self.create_login_frame).pack()

    def signup(self):
        email = self.signup_email_entry.get()
        password = self.signup_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        conn = Database().get_db_connection()
        if conn:
            try:
                c = conn.cursor()
                c.execute("SELECT email FROM users WHERE email = %s", (email,))
                if c.fetchone():
                    messagebox.showerror("Error", "Email already exists!")
                    conn.close()
                    return

                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                c.execute("INSERT INTO users (email, password, role) VALUES (%s, %s, %s)", (email, hashed_password, "customer"))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Signup successful! Please login.")
                self.create_login_frame()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error occurred: {e}")
                conn.close()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if email == "admin@gmail.com" and password == "admin123":
            messagebox.showinfo("Login Success", "Admin logged in successfully!")
            self.withdraw()
            admin_window = AdminPage()
            admin_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(admin_window))
            admin_window.mainloop()
            return

        conn = Database().get_db_connection()
        if conn:
            try:
                c = conn.cursor()
                c.execute("SELECT password, role FROM users WHERE email = %s", (email,))
                user = c.fetchone()
                conn.close()

                if user:
                    stored_password, role = user
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        if role == "admin":
                            messagebox.showinfo("Login Success", "Admin logged in successfully!")
                            self.withdraw()
                            admin_window = AdminPage()
                            admin_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(admin_window))
                            admin_window.mainloop()
                        elif role == "customer":
                            messagebox.showinfo("Login Success", "Customer logged in successfully!")
                            self.withdraw()
                            customer_window = CustomerPage()
                            customer_window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(customer_window))
                            customer_window.mainloop()
                    else:
                        messagebox.showerror("Error", "Invalid credentials!")
                else:
                    messagebox.showerror("Error", "No user found with this email!")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database Error: {e}")

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def on_closing(self, window):
        window.destroy()
        self.deiconify()

if __name__ == "__main__":
    app = Login()
    app.mainloop()
