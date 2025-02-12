import os
import random

def load_students(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            students = [line.strip() for line in file.readlines()]
           # print(f"Loaded students from {file_path}: {students}")  # Debug print
            return students
    print(f"File {file_path} does not exist.")  # Debug print
    return []

def save_students(file_path, students):
    with open(file_path, 'w') as file:
        for student in students:
            file.write(student + '\n')

def choose_student():
    script_dir = os.path.dirname(__file__)
    not_answered_path = os.path.join(script_dir, 'student_not-answered.txt')
    answered_path = os.path.join(script_dir, 'student_answered.txt')
    
    students_not_answered = load_students(not_answered_path)
    students_answered = load_students(answered_path)
    
   # print(f"Students not answered: {students_not_answered}")
   # print(f"Students answered: {students_answered}")
    
    available_students = [student for student in students_not_answered if student not in students_answered]
    
   # print(f"Available students: {available_students}")
    
    if not available_students:
        print("No students available to choose.")
        return
    
    chosen_student = random.choice(available_students)
    print(f"Chosen student: {chosen_student}")
    
    students_answered.append(chosen_student)
    save_students(answered_path, students_answered)

def reset_list():
    open('student_answered.txt', 'w').close()
    print("Student answered list has been reset.")

def main():
    while True:
        print("\nMenu:")
        print("1. Choose a student")
        print("2. Reset list")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            choose_student()
        elif choice == '2':
            reset_list()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()