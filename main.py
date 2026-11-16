from expenses import *
from validation import CATEGORIES
from reports import *
expenses = []
def showMenu():
    print("=" * 40)
    print("            EXPENSE TRACKER              ")
    print("=" * 40 )
    print()

    print("""
    1.Add Expense
    2.Show All Expens
    3.Edit Expense
    4.Delete Expens
    5.Search Expens
    6.Show Total Expens
    7.Show Cetogories
    8.Export To CSV

    0.Exit
    """)
showMenu()

def APP():
    while True:
        showMenu()
        choice = int(input("seciminizi daxil edin:"))
        if 0 <= choice < 9:
           if choice == 1:
               title = input("enter expense title:")
               amount = input("enter expense amount:")
               category = input("enter expense categoru:")

               expenses.append(title,amount,category)
               print("Exponse added succesfuly")
               print("Exponse ID:",expenses["id"])
        else:
            print("bele bir secim yoxdur")
APP()
