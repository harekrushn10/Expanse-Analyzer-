import json

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount:.2f}")

def get_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

def get_balance(initial_budget, expenses):
    return initial_budget - get_total_expenses(expenses)

def show_budget_details(initial_budget, expenses):
    print(f"\nTotal Budget: {initial_budget:.2f}")
    print("Expenses:")
    if expenses:
        for expense in expenses:
            print(f"- {expense['description']}: {expense['amount']:.2f}")
    else:
        print("No expenses recorded.")
    print(f"Total Spent: {get_total_expenses(expenses):.2f}")
    print(f"Remaining Budget: {get_balance(initial_budget, expenses):.2f}\n")

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    print("Welcome to the Budget App")

    filepath = 'Remaining_Balance_Data.json'
    initial_budget, expenses = load_budget_data(filepath)

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Add more funds")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            while get_balance(initial_budget, expenses) <= 0:
                print(f"\nNo funds available. Your current balance is: {get_balance(initial_budget, expenses):.2f}")
                print("Please add more funds to your budget to proceed.")
                try:
                    additional_funds = float(input("Enter additional funds to add to your budget: "))
                    if additional_funds <= 0:
                        raise ValueError
                    initial_budget += additional_funds
                    print(f"New total budget: {initial_budget:.2f}")
                except ValueError:
                    print("Invalid input. Please enter a positive numeric value.")

            description = input("Enter expense description: ")
            while True:
                try:
                    amount = float(input("Enter expense amount: "))
                    if amount < 0:
                        raise ValueError
                    if amount > get_balance(initial_budget, expenses):
                        print("Insufficient funds. Please add more to your budget or reduce the expense amount.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive numeric value.")
            
            add_expense(expenses, description, amount)

        elif choice == "2":
            show_budget_details(initial_budget, expenses)

        elif choice == "3":
            while True:
                try:
                    additional_funds = float(input("Enter additional funds to add to your budget: "))
                    if additional_funds <= 0:
                        raise ValueError
                    initial_budget += additional_funds
                    print(f"New total budget: {initial_budget:.2f}")
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive numeric value.")

        elif choice == "4":
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting Budget App. Goodbye!")
            break

        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
