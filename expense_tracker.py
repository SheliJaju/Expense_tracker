import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        self.expenses = []  # Ensure expenses is initialized
        self.filepath = 'expenses.csv'
        self.load_expenses()
        
        # Labels and Entry widgets
        self.date_label = ttk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=10, pady=5, sticky="W")
        self.date_entry = ttk.Entry(root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="E")
        
        self.desc_label = ttk.Label(root, text="Description:")
        self.desc_label.grid(row=1, column=0, padx=10, pady=5, sticky="W")
        self.desc_entry = ttk.Entry(root)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=5, sticky="E")
        
        self.category_label = ttk.Label(root, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")
        self.category_entry = ttk.Entry(root)
        self.category_entry.grid(row=2, column=1, padx=10, pady=5, sticky="E")
        
        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_label.grid(row=3, column=0, padx=10, pady=5, sticky="W")
        self.amount_entry = ttk.Entry(root)
        self.amount_entry.grid(row=3, column=1, padx=10, pady=5, sticky="E")
        
        # Buttons
        self.add_button = ttk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.expense_list = tk.Listbox(root, width=50)
        self.expense_list.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        
        self.delete_button = ttk.Button(root, text="Delete Selected Expense", command=self.delete_expense)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.view_button = ttk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.grid(row=6, column=0, columnspan=2, pady=10)
        
    def add_expense(self):
        date = self.date_entry.get()
        desc = self.desc_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        
        if date and desc and category and amount:
            expense = f"{date} | {desc} | {category} | ${amount}"
            self.expenses.append(expense)
            self.expense_list.insert(tk.END, expense)
            self.save_expenses()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
    
    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
    
    def delete_expense(self):
        selected = self.expense_list.curselection()
        if selected:
            index = selected[0]
            self.expense_list.delete(index)
            del self.expenses[index]
            self.save_expenses()
        else:
            messagebox.showwarning("Selection Error", "Please select an expense to delete.")
    
    def view_expenses(self):
        self.expense_list.delete(0, tk.END)
        for expense in self.expenses:
            self.expense_list.insert(tk.END, expense)
    
    def save_expenses(self):
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            for expense in self.expenses:
                writer.writerow(expense.split(" | "))
    
    def load_expenses(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    expense = " | ".join(row)
                    self.expenses.append(expense)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
