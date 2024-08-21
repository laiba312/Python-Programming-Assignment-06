def manage_student_database():
    # Initialize an empty list to store student names
    student_names = []
    student_tuples = []

    # Input loop
    while True:
        student = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        
        if student.lower() == 'stop':
            break
        
        if student in student_names:
            print("This name is already in the list.")
        else:
            student_names.append(student)
            student_tuples.append((len(student_tuples) + 1, student))
    
    # Print the complete list of student tuples
    print("\nComplete List of Students (Tuples):")
    print(student_tuples)
    
    # Print each student's ID and name individually
    print("\nList of Students with IDs:")
    for id, name in student_tuples:
        print(f"ID: {id}, Name: {name}")
    
    # Calculate and display additional information
    total_students = len(student_tuples)
    total_length = sum(len(name) for _, name in student_tuples)
    longest_name = max(student_tuples, key=lambda x: len(x[1]))[1] if student_tuples else "None"
    shortest_name = min(student_tuples, key=lambda x: len(x[1]))[1] if student_tuples else "None"
    
    print(f"\nTotal number of students: {total_students}")
    print(f"Total length of all student names combined: {total_length}")
    print(f"The student with the longest name is: {longest_name}")
    print(f"The student with the shortest name is: {shortest_name}")

# Call the function to execute the student database management
manage_student_database()
