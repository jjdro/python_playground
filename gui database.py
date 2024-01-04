import sqlite3
import tkinter as tk
from tkinter import ttk

def connect_to_database():
    # Connect to the database or create a new one
    return sqlite3.connect('products.db')

def create_cursor(connection):
    # Create a cursor object for executing SQL queries
    return connection.cursor()

def create_treeview(window):
    # Create a Treeview widget to display the database contents
    tree = ttk.Treeview(window)
    tree["columns"] = ("Name", "Price")

    # Define the column headings
    tree.heading("#0", text="ID")
    tree.heading("Name", text="Pass or Fail")
    tree.heading("Price", text="Location")

    # Pack the Treeview widget
    tree.pack()
    return tree

def retrieve_data(cursor, table_name):
    # Retrieve data from the specified table
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

def insert_data(tree, data):
    # Insert data into the Treeview
    for row in data:
        tree.insert("", tk.END, text=row[0], values=(row[1], row[2]))

def show_products():
    # Clear the Treeview
    tree.delete(*tree.get_children())

    # Retrieve data from the "products" table and insert it into the Treeview
    data = retrieve_data(cursor, "products")
    insert_data(tree, data)

def show_d2products():
    # Clear the Treeview
    tree.delete(*tree.get_children())

    # Retrieve data from the "d2Products" table and insert it into the Treeview
    data = retrieve_data(cursor, "d2Products")
    insert_data(tree, data)

# Create a new Tkinter window
window = tk.Tk()
window.title("Justin's shitty database")

# Set the background color to blue
window.configure(bg="blue")
def insert_data(tree, data):
    # Configure the style for the Treeview
    style = ttk.Style()
    style.configure("Treeview",
                    background="blue",
                    foreground="white")

    # Insert data into the Treeview
    for row in data:
        tree.insert("", tk.END, text=row[0], values=(row[1], row[2]), tags=("data",))

    # Configure the style for the data rows
    style.configure("data",
                    background="blue",
                    foreground="white")

# Rest of the code...
# Connect to the database and create a cursor
with connect_to_database() as conn:
    cursor = create_cursor(conn)

    # Create the Treeview widget
    tree = create_treeview(window)

    # Retrieve data from the "products" table and insert it into the Treeview
    data = retrieve_data(cursor, "products")
    insert_data(tree, data)

    # Create a menu bar
    menu_bar = tk.Menu(window)
    window.config(menu=menu_bar)

    # Create a "View" menu
    view_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=view_menu)

    # Add menu items for "Products" and "d2Products"
    view_menu.add_command(label="Products", command=show_products)
    view_menu.add_command(label="d2Products", command=show_d2products)

    # Configure the menu button with higher contrast
    view_menu.configure(bg="blue", fg="white")
    # Create 3 radio buttons
    radio_var = tk.IntVar()
    radio_button1 = tk.Radiobutton(window, text="Option 1", variable=radio_var, value=1)
    radio_button2 = tk.Radiobutton(window, text="Option 2", variable=radio_var, value=2)
    radio_button3 = tk.Radiobutton(window, text="Option 3", variable=radio_var, value=3)

    # Place the radio buttons below the data
    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()


    # Start the Tkinter event loop
    window.mainloop()
