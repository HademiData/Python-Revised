# 1. Data Transformation Engine Functions

def filter_transactions(transactions, condition):
    """Bonus Constraint: Generic filtration higher-order function."""
    return list(filter(condition, transactions))

def get_income(transactions):
    """Returns only income transactions using filter and a lambda."""
    return filter_transactions(transactions, lambda t: t["type"] == "income")

def get_expenses(transactions):
    """Returns only expense transactions using filter and a lambda."""
    return filter_transactions(transactions, lambda t: t["type"] == "expense")

def calculate_total(transactions):
    """Constraint: Calculates total value manually via map mapping ."""
    # Using map to extract amounts
    amounts = list(map(lambda t: t["amount"], transactions))
    
    total = 0
    for amount in amounts:
        total += amount
    return total


def find_largest(expense_transactions):
    """Constraint: Evaluates the single highest transaction manually."""
    if not expense_transactions:
        return None
    
    largest = expense_transactions[0]
    for current in expense_transactions:
        if current["amount"] > largest["amount"]:
            largest = current
    return largest


def get_balance(income_total, expense_total):
    """Returns the net operational balance calculation."""
    return income_total - expense_total


def get_status(balance):
    """Evaluates text status metrics purely based on numerical boundaries."""
    if balance > 0:
        return "Positive balance"
    elif balance < 0:
        return "Negative balance"
    else:
        return "Break-even"


# 2. Hard Bonus Integration Architecture

def analyze(transactions):
    
    """ Synthesizes structured data analytics without side effects."""
    income_list = get_income(transactions)
    expense_list = get_expenses(transactions)
    
    total_inc = calculate_total(income_list)
    total_exp = calculate_total(expense_list)
    balance = get_balance(total_inc, total_exp)
    
    largest_exp_dict = find_largest(expense_list)
    # Safely extract name string structure or fallback gracefully
    largest_exp_name = largest_exp_dict["name"] if largest_exp_dict else None
    
    # Calculate count manually by checking size index
    expense_count = 0
    for _ in expense_list:
        expense_count += 1

    return {
        "income": total_inc,
        "expenses": total_exp,
        "balance": balance,
        "largest_expense": largest_exp_name,
        "expense_count": expense_count,
        "status": get_status(balance)
    }


# 3. View Processing (Printing/Output)

def display_report(metrics, label="FINANCIAL REPORT"):
    """Handles raw visual rendering cleanly apart from analytics execution algorithms."""
    
    print(f"Total income: {metrics['income']} \n")

    print()
    print(f"Total expenses: {metrics['expenses']} \n")
    print(f"Balance: {metrics['balance']} \n")
    
    # Custom format to handle potential None values safely for largest expense formatting
    if metrics['largest_expense'] is not None:
        print(f"Largest expense: {metrics['largest_expense']} \n")
    else:
        print("Largest expense: None")
        
    print(f"Number of expenses: {metrics['expense_count']} \n")
    print(f"Status: {metrics['status']}")

    



if __name__ == "__main__":
    # Test Dataset 1: Standard Operational Stream
    transactions = [
        {"name": "Laptop", "amount": 250000, "type": "expense"},
        {"name": "Salary", "amount": 500000, "type": "income"},
        {"name": "Internet", "amount": 30000, "type": "expense"},
        {"name": "Freelance", "amount": 150000, "type": "income"},
        {"name": "Food", "amount": 45000, "type": "expense"}
    ]
    
    empty_dataset = []
    only_salary = [{"name": "Salary", "amount": 500000, "type": "income"}]
    
    # Process pipeline metrics
    metrics_standard = analyze(transactions)
    metrics_empty = analyze(empty_dataset)
    metrics_salary = analyze(only_salary)
    
    # Print out pure results 
    display_report(metrics_standard, "STANDARD TEST RUN")
    display_report(metrics_empty, "EDGE CASE: EMPTY DATASET")
    display_report(metrics_salary, "EDGE CASE: INCOME ONLY")
