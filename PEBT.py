budget_limit = None
total_expenses = 0
expenses = []

print("Welcome to the PEBT! Your Personal Expense and Budget Tracker!")
user_name = input("What´s your name? ").capitalize()
print(f"What a beautiful name {user_name}!")

while True:
         print("-------------------------------------------------------------------------------MENU---------------------------------------------------------------------------------------------------------------")
         first_answer = input(f"What you would like to do today {user_name}? \n[1] Add a new expense\n[2] See your total expenses\n[3] Expenses History \n[4] Set a Budget Limit\n[5] Delete an expense \n[6] Exit " )

         try:
            if first_answer == "1":
                  expense_month = input("What´s the month of the expense? ").capitalize()
                  expense_day = input("And the day?")
                  expense_category = input("What´s the category of the expense? ").capitalize()
                  expense_description = float(input("What's the amount of money that you would like to put on? "))
                  expenses.append((expense_month, expense_day, expense_category, expense_description))
                  total_expenses += expense_description
                  print(f"{expense_description:.2f} of Category: {expense_category}, from the data {expense_month} {expense_day} has been Added!")
                  
                  if budget_limit is not None:
                          if total_expenses > budget_limit:
                            print(f"⚠️ WARNING!: Your total expenses exceed your budget limit of {budget_limit}, Please reconsider the way you´re spending your money!")
                          else:
                            budget = budget_limit - total_expenses
                            print(f"Remaining Budget at the moment is: {budget:.2f}")


                  
                  
            if first_answer == "2":
                  if not total_expenses:
                         print(f"You don´t have any expenses added yet {user_name}!")
                  else:
                         print(f"Your total expenses are: {total_expenses:.2f}")

                         if budget_limit is not None:
                                   if total_expenses > budget_limit:
                                          print(f"⚠️ WARNING!: Your total expenses exceed your budget limit of {budget_limit}, Please reconsider the way you´re spending your money!")
                                   else:
                                          budget = budget_limit - total_expenses
                                          print(f"Remaining Budget at the moment is: {budget:.2f}")
              

                  

            if first_answer == "3":
                             if not expenses:
                                  print("You don´t have any expenses added yet!")
                             else:
                                    for num, (month, day, category, price) in enumerate(expenses, start = 1):
                                           print(f"{num} | Data: {month}/{day} | Category: {category} | Price: {price:.2f}")

                                    if budget_limit is not None:
                                            if total_expenses > budget_limit:
                                                    print(f"⚠️ WARNING!: Your total expenses exceed your budget limit of {budget_limit}, Please reconsider the way you´re spending your money!")
                                            else:
                                                 budget = budget_limit - total_expenses
                                                 print(f"Remaining Budget at the moment is: {budget:.2f}")
                                                 

                             

            
            if first_answer == "4":
                   budget_limit = float(input("Enter your budget limit: "))
                   print(f"Your budget limit of {budget_limit:.2f} got added!")
                   
            
            if first_answer == "5":
                   if not expenses:
                          print("You don´t have any expenses to delete!")
                   else:
                         delete_user_answer = (input("Are you sure you would like to delete an expense?"))
                         if delete_user_answer == "yes":
                             expense_to_delete = int(input("Which expense would you like to delete?"))
                             removed_item = expenses.pop(expense_to_delete - 1)
                             total_expenses -= removed_item[3]
                             print("Expense deleted!")
                         if delete_user_answer == "no":
                             continue

            if first_answer == "6":
                 print(f"Thank you so much for using the PEBT. Have a nice day {user_name}!")
                 break

         except ValueError:
            print("It seems something got wrong! Could you try it again?")
            continue





        


        
