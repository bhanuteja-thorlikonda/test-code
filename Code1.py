# Global variable used repeatedly
data = []

def add_student(name, age, grade):
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    data.append(student)
    print(f"Student {name} added.")

def display_students():
    print("\n--- Student List ---")
    for i, student in enumerate(data):
        print(f"{i + 1}. {student['name']} - Age: {student['age']}, Grade: {student['grade']}")
    print("--------------------")

def update_student(index, name=None, age=None, grade=None):
    if 0 <= index < len(data):
        if name:
            data[index]['name'] = name
        if age:
            data[index]['age'] = age
        if grade:
            data[index]['grade'] = grade
        print(f"Student at index {index + 1} updated.")
    else:
        print("Invalid student index.")

def delete_student(index):
    if 0 <= index < len(data):
        removed = data.pop(index)
        print(f"Removed student: {removed['name']}")
    else:
        print("Invalid student index.")

def search_student(name):
    print(f"\nSearching for students with name '{name}':")
    found = False
    for student in data:
        if student['name'].lower() == name.lower():
            print(student)
            found = True
    if not found:
        print("No student found.")

def average_age():
    if not data:
        print("No student data.")
        return
    total_age = sum(student['age'] for student in data)
    avg = total_age / len(data)
    print(f"\nAverage age of students: {avg:.2f}")

# Sample usage
add_student("Alice", 20, "A")
add_student("Bob", 21, "B")
add_student("Charlie", 22, "A")
display_students()
update_student(1, age=23)
delete_student(0)
search_student("Charlie")
average_age()
