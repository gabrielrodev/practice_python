
def display_invoice(username, amount, due_date):
    print(f"Hi {username}")
    print(f"Your bill of ${amount:.2f} is do: {due_date}")

display_invoice("joe",100.01, "10/20/2025")
