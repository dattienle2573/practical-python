# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 0

for i in range(12):
    if principal > 0:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
        month += 1
        print(f"{month:5}, {total_paid:10.2f}, {principal:10.2f}")

while principal > 0 and principal * (1 + rate / 12) > payment:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    month += 1
    print(f"{month:5}, {total_paid:10.2f}, {principal:10.2f}")

total_paid = total_paid + principal * (1 + rate / 12)
principal = 0
month += 1
print(f"{month:5}, {total_paid:10.2f}, {principal:10.2f}")

print(f"Total paid {total_paid} month {month}")
