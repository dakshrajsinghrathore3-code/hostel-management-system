students = []
complaints = []



def get_name():
    while True:
        name = input("Enter Student Name: ")

        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name! Please enter alphabets only.")


def get_id():
    while True:
        student_id = input("Enter Student ID: ")

        if student_id.isdigit():
            return student_id
        else:
            print("Invalid ID! Please enter numbers only.")


def get_phone():
    while True:
        phone = input("Enter Phone Number: ")

        if phone.isdigit() and len(phone) == 10:
            return phone
        else:
            print("Invalid phone number! Enter exactly 10 digits.")


def get_year():
    while True:
        year = input("Enter Year (1st/2nd/3rd/4th): ")

        if year in ["1st", "2nd", "3rd", "4th"]:
            return year
        else:
            print("Invalid year! Enter 1st, 2nd, 3rd or 4th.")


def get_room():
    while True:
        room = input("Enter Room Number (1-500): ")

        if room.isdigit():
            room = int(room)

            if 1 <= room <= 500:
                return room
            else:
                print("Room number must be between 1 and 500.")
        else:
            print("Invalid room number! Enter numbers only.")


def get_fee():
    while True:
        fee = input("Enter Fee Amount Paid: ")

        if fee.isdigit():
            return fee
        else:
            print("Invalid amount! Enter numbers only.")



def register_student():

    print("\n========== REGISTER STUDENT ==========")

    student_id = get_id()

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = get_name()
    course = input("Enter Course: ")
    phone = get_phone()
    year = get_year()

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "phone": phone,
        "year": year,
        "room": "Not Allocated",
        "fee": 0
    }

    students.append(student)

    print("\nStudent registered successfully!")



def view_students():

    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No student registered yet.")
        return

    for student in students:

        print("\n-----------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Course     :", student["course"])
        print("Phone      :", student["phone"])
        print("Year       :", student["year"])
        print("Room       :", student["room"])
        print("Fee Paid   : ₹", student["fee"])



def search_student():

    print("\n========== SEARCH STUDENT ==========")
    print("1. Search by Name")
    print("2. Search by ID")
    print("3. Search by Room Number")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["name"].lower() == name.lower():

                print("\nStudent Found!")
                print("-----------------------------")
                print("ID       :", student["id"])
                print("Name     :", student["name"])
                print("Course   :", student["course"])
                print("Phone    :", student["phone"])
                print("Year     :", student["year"])
                print("Room     :", student["room"])
                print("Fee Paid : ₹", student["fee"])

                found = True

        if not found:
            print("Student not found.")

    elif choice == "2":

        student_id = get_id()

        found = False

        for student in students:

            if student["id"] == student_id:

                print("\nStudent Found!")
                print("-----------------------------")
                print("ID       :", student["id"])
                print("Name     :", student["name"])
                print("Course   :", student["course"])
                print("Phone    :", student["phone"])
                print("Year     :", student["year"])
                print("Room     :", student["room"])
                print("Fee Paid : ₹", student["fee"])

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "3":

        room = get_room()

        found = False

        print("\n========== STUDENTS IN ROOM", room, "==========")

        for student in students:

            if student["room"] == room:

                print("\n-----------------------------")
                print("ID       :", student["id"])
                print("Name     :", student["name"])
                print("Course   :", student["course"])
                print("Phone    :", student["phone"])
                print("Year     :", student["year"])
                print("Room     :", student["room"])
                print("Fee Paid : ₹", student["fee"])

                found = True

        if not found:
            print("No student found in this room.")

    else:
        print("Invalid choice!")



def find_student():

    print("\n1. Find by Student ID")
    print("2. Find by Student Name")

    choice = input("Enter your choice: ")

    if choice == "1":

        student_id = get_id()

        for student in students:
            if student["id"] == student_id:
                return student

        print("Student not found.")
        return None

    elif choice == "2":

        name = input("Enter Student Name: ")

        for student in students:
            if student["name"].lower() == name.lower():
                return student

        print("Student not found.")
        return None

    else:
        print("Invalid choice!")
        return None


def allocate_room():

    print("\n========== ROOM ALLOCATION ==========")

    if len(students) == 0:
        print("No students registered yet.")
        return

    student = find_student()

    if student is None:
        return

    if student["room"] != "Not Allocated":
        print("Room already allocated:", student["room"])
        return

    room = get_room()

    room_count = 0

    for s in students:
        if s["room"] == room:
            room_count += 1

  
    if room_count >= 3:
        print("\nRoom", room, "is already full!")
        print("Maximum 3 students can stay in one room.")
        return

    student["room"] = room

    print("\nRoom", room, "allocated successfully!")
    print("Students in room:", room_count + 1, "/ 3")



def fee_status():

    print("\n========== FEE MANAGEMENT ==========")

    if len(students) == 0:
        print("No students registered yet.")
        return

    student = find_student()

    if student is None:
        return

    print("\nStudent Name :", student["name"])
    print("Student ID   :", student["id"])
    print("Fee Paid     : ₹", student["fee"])

    amount = get_fee()

    student["fee"] = amount

    print("\nFee updated successfully!")
    print("Total Fee Paid: ₹", student["fee"])


def register_complaint():

    print("\n========== REGISTER COMPLAINT ==========")

    student_id = get_id()

    found = False

    for student in students:

        if student["id"] == student_id:
            found = True
            break

    if found == False:
        print("Student not found.")
        return

    complaint = input("Enter your complaint: ")

    complaints.append({
        "student_id": student_id,
        "complaint": complaint,
        "status": "Pending"
    })

    print("Complaint registered successfully!")



def view_complaints():

    print("\n========== HOSTEL COMPLAINTS ==========")

    if len(complaints) == 0:
        print("No complaints available.")
        return

    for i, complaint in enumerate(complaints):

        print("\n-----------------------------")
        print("Complaint No.:", i + 1)
        print("Student ID   :", complaint["student_id"])
        print("Complaint    :", complaint["complaint"])
        print("Status       :", complaint["status"])

    complaint_no = input(
        "\nEnter Complaint Number to update (or 0 to go back): "
    )

    if not complaint_no.isdigit():
        print("Invalid input! Please enter a number.")
        return

    complaint_no = int(complaint_no)

    if complaint_no == 0:
        return

    if complaint_no < 1 or complaint_no > len(complaints):
        print("Invalid complaint number!")
        return

    selected_complaint = complaints[complaint_no - 1]

    print("\nSelected Complaint:")
    print("Student ID :", selected_complaint["student_id"])
    print("Complaint  :", selected_complaint["complaint"])
    print("Status     :", selected_complaint["status"])

    choice = input("Enter new status (done/pending): ")

    if choice.lower() == "done":

        selected_complaint["status"] = "Done"
        print("\nComplaint status updated to Done!")

    elif choice.lower() == "pending":

        selected_complaint["status"] = "Pending"
        print("\nComplaint status updated to Pending!")

    else:
        print("\nInvalid status! Please enter 'done' or 'pending'.")


while True:

    print("\n")
    print("==========================================")
    print("          HOSTEL MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Allocate Room")
    print("5. Fee Management")
    print("6. Register Complaint")
    print("7. View / Update Complaints")
    print("8. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        allocate_room()

    elif choice == "5":
        fee_status()

    elif choice == "6":
        register_complaint()

    elif choice == "7":
        view_complaints()

    elif choice == "8":
        print("\nThank you for using Hostel Management System!")
        break

    else:
        print("\nInvalid choice! Please enter a valid option.")