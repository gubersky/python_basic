money = int(input("Enter loan amount: "))

two_year_loan = money / 12
five_year_loan = money / 60
remainder = money
print("Loan for 1 year:")
for i in range(1, 12 + 1):
    percent = 0.02 * remainder
    remainder = remainder - two_year_loan
    payment = percent + two_year_loan
    print("Month = {:>2}: Monthly_payment = {:^10.2f}: Interest_per_month = {:>10.2f}".format(i, payment, percent))

remainder = money
print("Loan for 5 years:")

for i in range(1, 60 + 1):
    if i <= 24:
        percent = 0.02 * remainder
        remainder = remainder - five_year_loan
        payment = percent + five_year_loan
        print("Month = {:>2}: Monthly_payment = {:^10.2f}: Interest_per_month = {:>10.2f}".format(i, payment, percent))
    else:
        percent = 0.04 * remainder
        remainder = remainder - five_year_loan
        payment = percent + five_year_loan
        print("Month = {:>2}: Monthly_payment = {:^10.2f}: Interest_per_month = {:>10.2f}".format(i, payment, percent))
