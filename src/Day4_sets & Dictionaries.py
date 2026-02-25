student_obaid={"name":"obaid","age":23,"coures":"cse"}
print(student_obaid)


#task1
contacts={"omair":98765,"obaid":12345,"omar":54321}
print("contacts")

contacts["afnan"]=78600#aading new contacts
print(contacts)
contacts['obaid']=54321
print(contacts)

contacts.get('omar')
#contacts.get('maaz')
#print('contacts not found')
print(contacts.get('maaz','contacts not found'))


print(contacts.items())

for name,phone in contacts.items():
    print('name,phone')

#for key,value in contacts.items():
    #print(f"contacts:{'key'}/phone:{'value'}")
    
#task2

raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]#created a list
unique_users=set(raw_logs)#converting list into set and storing in new variable

print("ID05" in unique_users)

len(raw_logs)
len(unique_users)

print(len(raw_logs)^len(unique_users))

#task3

friend_a={"python","Cooking","Hiking","Movies"}
friend_b={"Hiking","Gaming","Photograoh","Python"}
print(friend_a & friend_b)#shared interest
print(friend_a | friend_b)#all interest
print(friend_a - friend_b)#individual interest

a=(friend_a & friend_b)
b=(friend_a |friend_b)
c=(friend_a- friend_b)
print(f"Shared interest between friend a and b are {a} and all interest are {b} and interest of friend a are {c}")
