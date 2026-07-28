# Expense Tracker Project
# This program allows user to add expense and calculate total spending

import csv
#creating an Expense class to represent one expense
class Expense:

    #Constructor: run automatically when we create a new expense object
    def __init__(self, name, amount, category):
        self.name = name              # Store expense name
        self.amount = amount          # Store expense amount
        self.category = category      # Store expense category

    # Function  to display expense details
    def display(self):
        print(f"{self.name} - {self.amount} - {self.category}")

# -----------------------------------
# Save expense
# -----------------------------------
def save_expense(expense):
        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            # Writer expense details as one row
            writer.writerow([
                expense.name,
                expense.amount,
                expense.category
            ])

# -----------------------------------
# Load expense 
# -----------------------------------
def load_expenses():
    try:
        # "r" means read mode
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            # Read each row from the CSV file
            for row in reader:
                name = row[0]
                amount = float(row[1])
                category = row[2]
                
                # Creat Expense object from saved data
                expense = Expense(name, amount, category)

                # Add old expense to the list
                expenses.append(expense)

    except FileNotFoundError:
        # If file does not exist, continuenormally
        pass

# -----------------------------------
# Add expense
# -----------------------------------
def add_expense():

    # Get expense details from the user
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    # Create a new Expense object
    expense = Expense(name, amount, category)

    # Add to list
    expenses.append(expense)

    # Save to CSV
    save_expense(expense)
    print("Expense added successsfully!\n")

# -----------------------------------
# View expenses
# -----------------------------------
def view_expenses():

    print("\nYour Expenses:")

    for expense in expenses:
        expense.display()

# -----------------------
# show total
# ----------------------
def show_total():

    total = 0

    for expense in expenses:
        total = total + expense.amount

    print(f"\nTotal Spending: £{total: }")

# ----------------------
# Main program
# ----------------------
expenses = []

# Load expenses
load_expenses()

# keep asking the user to enter expenses until they choose to stop
while True:
   

    print("\n========== Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid option. Please try again.")

