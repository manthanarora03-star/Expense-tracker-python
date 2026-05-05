expenses = []

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (food/travel/gym/other): ")
    date = input("Enter date (DD-MM-YYYY): ")
    
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }
    
    expenses.append(expense)
    print("✅ Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return
    
    print("\n--- All Expenses ---")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. {expense['date']} | {expense['category']} | ₹{expense['amount']}")

def total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\n💰 Total Spending: ₹{total}")

def category_summary():
    summary = {}
    
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    
    print("\n--- Spending by Category ---")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")

def delete_expense():
    view_expenses()
    
    if len(expenses) == 0:
        return
    
    try:
        index = int(input("Enter expense number to delete: ")) - 1
        
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(f"❌ Deleted: {removed['category']} ₹{removed['amount']}")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        print("Exiting... 👋")
        break
    else:
        print("Invalid choice, try again.")