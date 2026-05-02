def student_record(student):
    n=int(input("enter no.of students:"))
    for i in range(1,n+1):
        name=input(f"enter a student name {i}: ")
        mark=int(input(f"enter a student mark {i}: "))
        student[name]=mark
    

def display(student):
    if not student:
        print("no records found")
    else:
        for name,mark in student.items():
            print(name,"->",mark)

def topper(student):
    if not student:
        print("no records found")
    else:
        ma_x=float("-inf")
        topper=""
        for k,w in student.items():
            if w>ma_x:
                ma_x=w
                topper=k
        print(topper,"->",ma_x)

data={}
while True:
    print("1. Add students")
    print("2. Display students")
    print("3. Topper")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        student_record(data)
    elif choice==2:
        display(data)
    elif choice==3:
        topper(data)
    elif choice==4:
        break
    else:
        print("Invalid choice")
    
