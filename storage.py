import json

DATA_FILE = "data/expenses.json"

def loadExpenses():
   try:
    with open(DATA_FILE,"r",encoding="utf-8") as file:
      expenses = json.load(file)

    return expenses
   except FileNotFoundError:
     return []
   except json.JSONDecodeError:
      raise ValueError("JSON file is corrupted")

def saveExpenses(expense):
  try:
    with open(DATA_FILE,"w",encoding="utf-8") as file:
      json.dump(expense,f,indent=4,ensure_ascii=False)
      print("data succesful saved")
  except Exception as e:
    print("Error found:",e)