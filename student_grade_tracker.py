# Objective:
# Create a Python program that manages student grades using a CSV file. The program should allow users to:
# ✅ Add new student records
# ✅ View all student records
# ✅ Search for a student by name or ID
# ✅ Update a student’s grade
# ✅ Delete a student’s rp
import csv


def add_student_records():
        id = int(input("Enter the student's id: "))      
        name = input("Enter the student's name: ")
        subject = input("Enter the subject's name: ")
        grade = input("Enter the student's grade: ")
        
        with open('grades.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, subject, grade])
            file.close()
def view_student_records():
    print("\n\n")
    with open('grades.csv', mode='r', newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        print(f"{header[0]:<5} {header[1]:<18} {header[2]:<10} {header[3]:<3}")
        print('-'*36)
        for row in reader:
            print(f"{row[0]:<5} {row[1]:<18} {row[2]:<10} {row[3]:<3}")
        file.close()

def search_student():
    name = None
    print("Search by id or name\n")
    search_choice = input("Enter the id or name of the student:")
    try:
        int(search_choice)
        id = search_choice
    except:
       
        name = search_choice

    with open('grades.csv', mode='r', newline="") as file:
        reader = csv.reader(file)
        header = next(reader) # skips the title header
        for row in reader:
            if row[0] == id or row[1] == name:
                print("\n")
                print('-'*36)
               
                print(', '.join(row))
                print('-'*36)
        file.close()

            

while True:
    print("\n\n")
    print("Student Grade Tracker".center(36,'='))
    print("1. Add new Students\n2. View all student records\n3. Search for a Student by name or ID\n4. Update a student's grade\n5. Delete a student's record\n6. Exit")
    choice = int(input("Enter your choice number: "))
    if (choice==1):
        add_student_records()
    elif choice == 2:
        view_student_records()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student_record()
    elif choice == 5:
        delete_student_record()
    elif choice == 6:
        exit()
    
    # Functions
  
    

    

