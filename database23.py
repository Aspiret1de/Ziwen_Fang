import psycopg2

DATABASE = "postgres"
USER = "postgres"
PASSWORD = "030310"
HOST = "localhost"
PORT = "5432"

conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
cursor = conn.cursor()

def read_data(student_num):
    cursor.execute("SELECT * FROM student WHERE sno = %s;", (student_num,))
    student = cursor.fetchone()
    if student:
        print(student)
    else:
        print("No that student number.")

def insert_data(student_num, name, age, gender, department_name):
    cursor.execute("SELECT * FROM student WHERE sno = %s;", (student_num,))
    if cursor.fetchone():
        print("Student number already exists.")
    else:
        cursor.execute("INSERT INTO student (sno, sname, sage, sgender, sdept) VALUES (%s, %s, %s, %s, %s);",
                        (student_num, name, age, gender, department_name))
        conn.commit()
        print("Data inserted successfully.")

def update_data(student_num, new_name, new_age, new_gender, new_department_name):
    cursor.execute("SELECT * FROM student WHERE sno = %s;", (student_num,))
    if cursor.fetchone():
        cursor.execute("UPDATE student SET sname=%s, sage=%s, sgender=%s, sdept=%s WHERE sno = %s;",
                        (new_name, new_age, new_gender, new_department_name, student_num))
        conn.commit()
        print("Updated successfully.")
    else:
        print("Student not found.")

def delete_data(student_num):
    cursor.execute("SELECT * FROM sc WHERE sno = %s;", (student_num,))
    if cursor.fetchall():
        cursor.execute("DELETE FROM sc WHERE sno = %s;", (student_num,))
        conn.commit()
        print("Student's course enrollment records deleted.")

    cursor.execute("DELETE FROM student WHERE sno = %s;", (student_num,))
    if cursor.rowcount > 0:
        conn.commit()
        print("Deleted successfully.")
    else:
        print("No student found.")

def main_menu():
    while True:
        print("\nDatabase Management Menu:")
        print("1. Read data")
        print("2. Insert data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Exit")
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            student_num = input("Enter student number to read: ")
            read_data(student_num)
        elif choice == '2':
            student_num = input("Enter student number: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender (M/F): ")
            department_name = input("Enter department name: ")
            insert_data(student_num, name, age, gender, department_name)
        elif choice == '3':
            student_num = input("Enter student number: ")
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_gender = input("Enter new gender (M/F): ")
            new_department_name = input("Enter new department name: ")
            update_data(student_num, new_name, new_age, new_gender, new_department_name)
        elif choice == '4':
            student_num = input("Enter student number to delete: ")
            delete_data(student_num)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose a number between 1-5.")

if __name__ == "__main__":
    main_menu()
