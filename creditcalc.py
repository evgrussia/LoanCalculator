import math
import argparse
import math
parser = argparse.ArgumentParser(description="Loan calculator")
parser.add_argument("--type", type=str, choices=["annuity", "diff"], help="Enter the type of payment :")
parser.add_argument("--payment", type=float, help="Enter the monthly payment :")
parser.add_argument("--principal", type=float, help="Enter a loan principal : ")
parser.add_argument("--periods", type=int, help="Enter a number of periods : ", choices=range(700))
parser.add_argument("--interest", type=float, help="Enter the loan interest : ")
args = parser.parse_args()
full_payment=0

if args.type == None or args.interest==None:
    print ("Incorrect parameters")


if args.type == 'annuity' and args.principal and args.payment and args.interest:
    loan_principal = args.principal
    monthly_payment = args.payment
    loan_interest = args.interest
    i = loan_interest / (12 * 100)
    n = math.log((monthly_payment / (monthly_payment - i * loan_principal)), 1 + i)
    n_month = int(n % 12) + 1
    n_year = int(n // 12)
    if n_month < 12:
        print(f'It will take {n_year} years and {n_month} month to repay this loan')
    else:
        print(f'It will take {n_year + 1} years to repay this loan')
    full_payment = monthly_payment*math.ceil(n)
    overpayment = full_payment - loan_principal
    print(f'Overpayment = {int ( overpayment )}')

elif args.type == 'diff' and args.principal and args.periods and args.interest:
    loan_principal = args.principal
    month_number = args.periods
    loan_interest = args.interest
    i = loan_interest / (12 * 100)
    for m in range(1, month_number+1):
        diff_payment = math.ceil((loan_principal/month_number) + i * (loan_principal - (loan_principal * (m - 1) / month_number)))
        full_payment += diff_payment
        print(f'Month {m} payment is {diff_payment}')
        if m == month_number:
            overpayment = full_payment - loan_principal
            print(f'Overpayment = {int(overpayment)}')

elif args.type == 'annuity' and args.principal and args.periods and args.interest:
    loan_principal = args.principal
    month_number = args.periods
    loan_interest = args.interest
    i = loan_interest / (12 * 100)
    annuity_payment = round(loan_principal * ((i * (pow(1 + i, month_number))) / (pow(1 + i, month_number) - 1)))+1
    print(f'Your annuity payment = {annuity_payment}!')
    full_payment=annuity_payment*month_number
    overpayment = full_payment - loan_principal
    print(f'Overpayment = {int ( overpayment )}')

elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    annuity_payment = args.payment
    month_number = args.periods
    loan_interest = args.interest
    i = loan_interest / (12 * 100)
    loan_principal = annuity_payment/((i * (pow(1 + i, month_number)))/(pow(1 + i, month_number) - 1))
    print(f'Your loan principal = {round(loan_principal)}!')
    full_payment = annuity_payment * month_number
    overpayment = full_payment - loan_principal
    print ( f'Overpayment = {int ( overpayment )}' )



