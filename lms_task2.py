#calculate the EMI of mahindra scrpio N
car_variant="z2 E(petrol)"
car_price=1500000
down_payment=1000000
bank_intrest_rate=15
time_period=3

#calculate total loan amount
total_loan_amount=car_price - down_payment

#no of years=3 and so 12*3
monthly_intrest_rate=(bank_intrest_rate/100)/12

#convert year to total number of months
num_payments=time_period*12

#calculate Emi
EMI=total_loan_amount*(monthly_intrest_rate*(1+ monthly_intrest_rate)**num_payments)/((1+ monthly_intrest_rate)**num_payments -1)

#total interest paid
intrest=(EMI* num_payments)-total_loan_amount

#display
print(f"car varient: {car_variant}")
print(f"car price: {car_price}")
print(f"Down payment: {down_payment}")
print(f"bank intrest: {bank_intrest_rate}")
print(f"timen period: {time_period}")
print("-------------------------")
print(f"loan amount: {total_loan_amount}")
print(f"intrest: {intrest}")
print(f"monthly emi: {EMI}")


