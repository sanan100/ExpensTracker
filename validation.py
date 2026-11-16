from exceptions import *


CATEGORIES = [
   
      "Food",
      "Shopping",
      "Education",
      "Health",
      "Entertaiment",
      "Other"

]

def validateTitle(title):
    title = title.strip()

    if not title:
        invalidExpens("Title cannot be empty")

    return title


def  validateAmount(amount):
    try:
        amount = float(amount)
    except ValueError:
        invalidExpens("amount must be number")

    if amount < 0 :
        invalidExpens("amount must be greater than 0")

    return amount