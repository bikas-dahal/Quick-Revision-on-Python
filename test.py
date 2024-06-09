# Personal Finance Tracker with Detailed Comments

import json
from tkinter import Tk, Label, Entry, Button, messagebox

# Transaction class to represent a financial transaction
class Transaction:
    def __init__(self, amount, date, category):
        self.amount = amount  # The amount of the transaction
        self.date = date      # The date when the transaction occurred
        self.category = category  # The category of the transaction (e.g., 'Salary', 'Groceries')

    def __dict__(self):
        # Method to convert the transaction object to a dictionary for JSON serialization
        return {
            'amount': self.amount,
            'date': self.date,
            'category': self.category
        }

# FinanceTracker class to manage financial transactions
class FinanceTracker:
    def __init__(self):
        self.transactions = []  # List to store all transactions

    def add_transaction(self, amount, date, category):
        # Method to add a new transaction to the tracker
        if amount > 0:
            self.transactions.append(Transaction(amount, date, category))
            print("Transaction added.")
        else:
            print("Invalid transaction amount.")

    def get_transactions_by_category(self, category):
        # Method to retrieve all transactions of a specific category
        return [t for t in self.transactions if t.category == category]

    def generate_report(self):
        # Method to generate a report based on the transactions (implementation not shown)
        pass

    def save_transactions(self):
        # Method to save all transactions to a JSON file
        with open('transactions.json', 'w') as file:
            json.dump([t.__dict__() for t in self.transactions], file)

    def load_transactions(self):
        # Method to load transactions from a JSON file
        try:
            with open('transactions.json', 'r') as file:
                transactions = json.load(file)
                self.transactions = [Transaction(**t) for t in transactions]
        except FileNotFoundError:
            self.transactions = []

    def authenticate_user(self):
        # Method to authenticate the user (implementation not shown)
        username = input("Enter username: ")
        password = input("Enter password: ")
        return True  # Placeholder for actual authentication

    def create_gui(self):
        # Method to create a graphical user interface for the tracker (implementation not shown)
        root = Tk()
        root.title("Personal Finance Tracker")

        # GUI elements go here
        # ...

        root.mainloop()

# Example usage of the FinanceTracker class
tracker = FinanceTracker()
tracker.add_transaction(1000, '2024-01-01', 'Salary')
tracker.save_transactions()
tracker.load_transactions()

# Authenticate user before accessing sensitive data
if tracker.authenticate_user():
    tracker.create_gui()
