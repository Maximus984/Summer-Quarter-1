import budgetclass

budget = budgetclass.budget(500)


budget.AddBudget("Books", 100)
budget.AddBudget("rent", 800)
budget.AddBudget("car Note", 200)

budget.spend("Books", 50) 
budget.spend("rent",800)
budget.spend("car Note", 200)

budget.PrintBudget()