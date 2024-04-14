def get_subjects():
    num_subjects = int(input("Fadlan Gali Tirada Madoyinka Aad Rabto : "))
    subjects = []
    for i in range(num_subjects):
        subject_name = input(f"Geli Magaca Madada {i + 1}: ")
        subjects.append(subject_name)
    return subjects

def get_students():
    num_students = int(input("Fadlan Gali Tirada Ardada: "))
    students = []
    for i in range(num_students):
        student_name = input(f"Gali Magaca Ardaga {i + 1}: ")
        students.append(student_name)
    return students

def enter_scores(subjects, students):
    scores = {}
    for student in students:
        scores[student] = {}
        for subject in subjects:
            score = float(input(f"Enter {student}'s score for {subject}: "))
            scores[student][subject] = score
    return scores

def display_scores(scores):
    print("\n--- Exam Scores ---")
    for student, subject_scores in scores.items():
        print(f"\n{student}'s Scores:")
        for subject, score in subject_scores.items():
            print(f"{subject}: {score}")

def main():
    print("Welcome!")

    subjects = get_subjects()
    students = get_students()
    exam_scores = enter_scores(subjects, students)
    display_scores(exam_scores)


main()
