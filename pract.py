print("===== FINANCIAL SUMMARY =====")
name=input("enter your name")
cur_balance=int(input("enter your cur balance"))
monthly_income=float(input("enter your monthly income"))
monthly_expense=int(input("enter your monthly expense"))
print("Name:",name)
print("Balance:",cur_balance)
print("Income:",monthly_income)
print("expenses:",monthly_expense)
final_balance=cur_balance+monthly_income-monthly_expense
print("final balance:",final_balance)

