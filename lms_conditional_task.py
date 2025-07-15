# Task to calculate tuition discount claculation in python
#user input
student_name=input("enter name: ")
student_grade=int(input("enter grade(1-12): "))
tution_fee= float(input("enter tution fee "))

is_acedemic_topper_input=input("academic topper  ? (yes/no): ")
is_acedemic_topper=is_acedemic_topper_input=="yes"

#discount set
discount =0.0

#input validation
if 1 <= student_grade <=12:
    print(f"processing discont for {student_name}")

    #discount for 9-12:
    if student_grade >=9 and student_grade <=12:
        if is_acedemic_topper:
            discount = 0.02
            print("academic topper discont applied 20% ")
        else:
            discount = 0.01
            print("primary school discount applied 10% ")
    elif student_grade >=6 and student_grade <=8:
        discount = 0.05
        print("middle scchool discount applied 5% ")
    else:
        discont = 0.0
        print("no discount for this grade")
     
    #match case
    match student_grade:
        case 10:
            discount += 0.03
        case 12:
            discount += 0.05
        case _:
            discount += 0.0
    
    discount_amount= tution_fee * discount
    final_fee= tution_fee - discount_amount

    #display

    print(f"Student name {student_name} ")
    print(f"grade level {student_grade}")
    print(f"Acedemic topper status {is_acedemic_topper}")
    print(f"Tuition fee {tution_fee}")
    print(f"discount amount in percentage  {discount}")
    print(f"discount amount saved  {discount_amount}")
    print(f"final tutuion fee {final_fee}")
else:
    print(f"invalid graede enter between 1-12")