#customer discount calculation
#variables
customer_id=input("Customer ID: ")
customer_name= input("Customer name: ")
is_premium=("is Customer is premium? (yes/no)")
years_partnership= int(input("years of partnership: "))
deal_stage=input("DEAL STAGE? (proposal / negotiation / closeed)")
deal_value=int(input("DEAL VALUE: "))


# applying discont
basediscount=0.0

if is_premium :
    basediscount= 0.01
    print("is a premium coustomer discount allowed 10%")
elif years_partnership>=3 :
    basediscount= 0.05
    print("is a non premium customer allwed dicount 5%")
else :
    basediscount= 0.0

# match case extra discount
extradiscount=0.0
match deal_stage:
    case "proposal":
        extradiscount +=0.02
    case "negotiation":
        extradiscount += 0.03
    case "closed" :
        extradiscount += 0.05

# calculate the final discount  and deal value
total_discount=basediscount + extradiscount
final_discont_amount= deal_value * total_discount
final_value= deal_value - final_discont_amount 

#display
print(f"Customer id:  {customer_id}")
print(f"Customer Name:  {customer_name}")
print(f"Is Premium {is_premium}")
print(f"Years of Partner ship {years_partnership}")
print(f"deal value {deal_value}")
print(f"Deal Stage {deal_stage}")
print(f"base discount {basediscount}")
print(f"Extra discount {extradiscount}")
print(f"total discount {total_discount}")
print(f"final discount {final_value}")
