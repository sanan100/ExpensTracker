import uuid
from datetime import date
from storage import *
from validation import *
from exceptions import expensesNotFound


def addExpense(title,amount,category):
    expenses = loadExpenses()
    
    expense = {
        "id": str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmount(amount),
        "category": validateCategory(category),
        "date": date.today().isoformat()

    }

    expenses.append(expense)
    saveExpenses(expenses)

def getAllExpenses():
    return loadExpenses()

def searchExpenses(expensID):
     expenses = loadExpenses()

     for i in expenses:
         if i["id"] == expensID:
            print(i)
         else:
             print(expensesNotFound())


def updateExpense(expensID,title,amount,category):
    expenses = loadExpenses()
    for i in expenses:
        if i["id"] == expensID:
            i["title"] = validateTitle(title)
            i["category"] = validateCategory(title)
            i["amount"] = validateAmount(title)

            saveExpenses(expenses)
            return i

    expensesNotFound()


def deleteExpens(expensID):
    expenses = loadExpenses()
    for i in expenses:
        if i["id"] == expensID:
            expenses.remove(i)

            saveExpenses(expenses)
    expensesNotFound()