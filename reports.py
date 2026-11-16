import csv

from expenses import getAllExpenses

def totalExpens(expensID,):
    expenses= getAllExpenses()
    total = 0
    for i in expenses:
            if i["id"] == expensID:
                total += i["amount"]
                print("Hesablandi:",total)

def exporToCSV():
  exponses = getAllExpenses

  filePath = "data/expenses.csv"

  fieldNames = ["id","title","amount","category","date"]

  with open(filePath,"w",newline = "",encoding = "utf=-8") as file:
       writer = csv.DictWriter(file,fieldnames = fieldNames)
       writer.writeheader()
       writer.writerows(exponses)


  return filePath