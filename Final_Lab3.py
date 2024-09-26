monthly_salary = int(input("Provide your monthly salary:"))

if monthly_salary >= 30000:
    loan_amount = int(input ("Provide your requested loan amount:"))
    if loan_amount <= monthly_salary * 10:
        print("You are eligible for a loan!") # Display eligibility for a loan
        months = int(input ("Months to pay:")) # Input months to pay
        interest = loan_amount * 0.10 # Adding 10% Interest
        new_loan_amount = loan_amount + interest # Loan with added interest
        payable = new_loan_amount / months # Loan with added interest divided to months to pay
        print("Your monthly payment is:", payable)  
    else: 
        print("You are not eligible for a loan, too high loan request")
else:
    print("You are not eligible for a loan, low salary")