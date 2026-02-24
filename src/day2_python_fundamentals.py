student_age=19
student_name="umar"
print(student_age)
print (student_name)

print(type(student_age))
print(type(student_name))

num1=10
num2=20

print(num1+num2)
print(num1*num2)

num3=int(input("enter the first number"))
num4=int(input("enter the second number"))
num5=num3+num4
print(f"your first number is {num3} and second number is {num4} and the addition of this number is {num5}")

#task 1
user_name=input("enter your name")
user_age=int(input("enter your current age"))

user_age+=4

print(f"hey {user_name} you will be {user_age} years old in 2030")

#task 2

total_bill=float(input("enter total bill"))
total_no_of_people=int(input("enter number of people"))
share_per_person=total_bill/total_no_of_people
print(f"total bill:{total_bill} each person pays: {share_per_person}")

#task 3
item_name="laptop"
quantity=2
price=49999.9
in_stock=True
print(item_name,quantity,price,in_stock)
total_cost=quantity*price
print("total cost:",total_cost)