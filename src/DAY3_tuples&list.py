#list
fruit_list=("apple","banana","mango")
print(fruit_list[1])
print(type(fruit_list[1]))

#append
fruit_list=["apple","banana","mango"]
fruit_list.append("kiwi")
print(fruit_list)
print(type(fruit_list[3]))

#task1
#create a list 'named inventory

inventory_list=["Apple","Banana","carrots","Dates"]
print(inventory_list)

#append"Eggs"

inventory_list.append("Eggs")
print(inventory_list)

#remove (Bnanas bcos sold out)

inventory_list.remove("Banana")
print(inventory_list)

#organize the inventory alpoblets using sort

inventory_list.sort()
print("final update inventory:",inventory_list)


#task2
#create a list named tempertures
tempertures=[22,24,25,28,30,29,26,24,22]
tempertures[0]
tempertures[-1]

afternature_peak=tempertures[3:6]
print(afternature_peak)
last_3_hours=tempertures[-3]
print(last_3_hours)

print(tempertures)
print(tempertures[0],tempertures[-1])
print(afternature_peak)
print(last_3_hours)

#task3
screen_res=(1920, 1080)
print("Current Resolution: 1920x1080")
print(screen_res)

# screen_res[0] = 1280   # ❌ Commented out because tuples cannot be modified
print("Tuples cannot be modified")
