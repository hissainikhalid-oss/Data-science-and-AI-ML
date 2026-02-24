file=open("sample.text.py","w")
file.write("hello,this is a file handling example,")
file.close()

file=open("sample.text.py","r")
content=file.read()
print(content)
file.close()

with open ("sample.text.py") as file:
    content=file.read()
    file.close()
    
#Create a data.csv file
import csv

with open("khalid.csv","r") as file:
    reader = csv.reader(file) #reads structured row
    for row in reader: # line by line
        print(row)
        
        
        
try:
    
    with open("missing.text","r") as filr:
        content=file.read()
        print(content)
        
except FileNotFoundError:
    print("such file not exists")

#task 1
name = input("What is your name? ")
goal = input("What is your Daily Goal? ")

with open("journal.txt", "a") as file:
    file.write(f"{name}: {goal}\n")

with open("journal.txt","r") as file:
    print(file.read())

#task 2
import csv

with open("Student.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Students who have passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
            
#task 3

filename = input("Enter a filename")

try:
    with open(filename,"r") as file:
           contents = file.read()
           print("file contents:")
           print(contents)
           
except FileNotFoundError:
    print("Oops! That file doesn't' exist yet.") 