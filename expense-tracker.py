# Expense Tracker Project
# This program allows user to add expense and calculate total spending


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

# Create an empty list to store all expenses
expenses = []

# keep asking the user to enter expenses until they choose to stop
while True:

    # Get expense details from the user 
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    # Create a new expense object using the user's information
    expense = Expense(name, amount, category)

    # Add the expense object to our expenses list
    expenses.append(expense)

    # Ask the user if they want to add another expense
    more = input("Add another expense? (yes/no): ")

    # Stop the loop if the user does not type yes
    if more.lower() !="yes":
        break

# Display all expenses entered by the user                  
for expense in expenses:
    expense.display()

# Calculate the total amount spent
total = 0

for expense in expenses:
    total = total + expense.amount

#Display the final total
print(f"Total Spending: £{total}")