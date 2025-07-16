class budget:
    def __init__(self,amount):
    # the amount of money we have to spend 
        self.funds = amount

    # A dictionary of our items we are spending our buget on; 
    # The key is the name of the item; the value is the budget amount for that item
        self.budgets = {}

    # A dictionary of the expenese of each budgeted item
    # The key is the name of the item; the value is the amount spent on the item
        self.expenses = {}

    # Adds an item to the budget dictionary
    def AddBudget(self, name, amount):
        global funds 
        if name in self.budgets:
            raise ValueError("Budget for this item already exists.")
        if amount > funds:
            raise ValueError("Not enough funds available.")
        self.budgets [name] = amount
        funds -= amount
        self.expenses[name] = 0
        return funds

    def spend(self, name, amount):
        if name not in self.expenses:
            raise ValueError("No budget found for this item.")
        self.expenses[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def PrintBudget(self):
        print("Budget          Budgeted      spend    Remaiing")
        print("--------------------------------------------------")
        totalBudgeted = 0
        totalspent = 0
        totalRemaining = 0
        for name in self.budgets:
            budgeted = self.budgets [name]
            spent = self.expenses[name]
            remainingBudget = budgeted - spent
            print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}' 
                f'{remainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalspent += spent
            totalremaining = remainingBudget
        print(f'{"total":15s}, {totalBudgeted:10.2f}, {spent:10.2f}' 
                f'{remainingBudget:10.2f}')
            


   