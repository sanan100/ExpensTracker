def expensesNotFound():
    raise LookupError("Expense not founf")

def invalidExpens(message):
    raise ValueError(message)