# the amount of money we have to spend 
funds = 2500

# A dictionary of our items we are spending our buget on; 
# The key is the name of the item; the value is the budget amount for that item
budgets = {}

# A dictionary of the expenese of each budgeted item
# The key is the name of the item; the value is the amount spent on the item
expenses = {}

# Adds an item to the budget dictionary
def AddBudget(name, amount):
    global funds 
    if name in budgets:
        raise ValueError("Budget for this item already exists.")
    if amount > funds:
        raise ValueError("Not enough funds available.")
    budgets [name] = amount
    funds -= amount
    expenses[name] = 0
    return funds

def spend(name, amount):
    if name not in expenses:
        raise ValueError("No budget found for this item.")
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    print("Budget          Budgeted      spend    Remaiing")
    print("--------------------------------------------------")
    totalBudgeted = 0
    totalspent = 0
    totalRemaining = 0
    for name in budgets:
        budgeted = budgets [name]
        spent = expenses[name]
        remainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}' 
              f'{remainingBudget:10.2f}')
        totalBudgeted += budgeted
        totalBudgeted += spent
        totalremaining = remainingBudget
    print(f'{"total":15s}, {totalBu:10.2f}, {spent:10.2f}' 
              f'{remainingBudget:10.2f}')
        


print("Total Funds: ", funds)
AddBudget("Books", 100)
AddBudget("rent", 800)
AddBudget("car Note", 200)

spend("Books", 50) 
spend("rent",800)
spend("car Note", 200)

PrintBudget()