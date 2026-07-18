class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
    
    def display(self):
        print(f"{self.name} - {self.amount} - {self.category}")

expenses = []

expense1 = Expense("coffee", 3.50, "Food")
expense2 = Expense("Bus ticket", 2.00, "Transport")
expense3 = Expense("Book", 10.00, "Education") 

expenses.append(expense1)
expenses.append(expense2)
expenses.append(expense3)

for expense in expenses:
    expense.display()


total = 0

for expense in expenses:
    total = total + expense.amount

print(f"Total Spending: £{total}")