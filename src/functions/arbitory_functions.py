

def advance_junaid(name, roll, *marks, area="GB", school="GBPS"):

    total_subjects = len(marks)
    total_marks = len(marks)*100
    gained_marks = 0
    is_passed = False

    for subject_marks in marks:
        gained_marks += subject_marks

    if gained_marks >= total_marks/2:
        is_passed = True

    print("area  : ", area)
    print("school: ", school)
    print("roll  : ", roll)
    print("name  : ", name)
    print("marks : ", marks)

    print("Total Subjects    :", total_subjects)
    print("total marks       :", total_marks)
    print("Obtained marks    :", gained_marks)
    print("Is Passed         :", is_passed)

    print("---------------------")

