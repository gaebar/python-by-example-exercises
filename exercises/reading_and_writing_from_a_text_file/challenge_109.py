"""
Display the following menu to the user:  
1) Create a new life
2) Display the file
3) Add a new item to the file. 
Make a selection 1, 2 or 3:

Ask the user to enter 1, 2 or 3. 
If they select  anything other than 1, 2 or 3 it should display a suitable error message.  
If they select 1, ask the user to enter a school subject and save it to a new file called  
“Subject.txt”. It should overwrite any existing file with a new file.  
If they select 2, display the contents of the  “Subject.txt” file.  
If they select 3, ask the user to enter a new  subject and save it to the file and then display  
the entire contents of the file.  Run the program several times to test the  options. 
"""

print("1) Create a new life")
print("2) Display the file")
print("3) Add a new item to the file. ")

selection = int(input("Make a selection 1, 2 or 3: "))

if selection == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()

elif selection == 2:
    file = open("Subject.txt", "r")
    print(file.read())

elif selection == 3:
    file = open("Subject.txt", "a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())

else:
    print("Invalid option")

