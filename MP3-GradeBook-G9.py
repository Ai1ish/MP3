#Primary variables for data:
students    = {} 
categories  = {}   
assignments = {}   
grades      = {}   

next_student_id    = 1
next_category_id   = 1
next_assignment_id = 1

#Grades/Calculations:
def letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def category_average(student_id, category_id):
    total = 0
    count = 0
    for aid, a in assignments.items():
        if a["category_id"] == category_id:
            if (student_id, aid) in grades:
                max_pts = a.get("max_points", 100)
                total += (grades[(student_id, aid)] / max_pts) * 100
                count += 1
    if count == 0:
        return None
    return total / count

def final_grade(student_id):
    weighted_sum   = 0
    covered_weight = 0
    for cid, cat in categories.items():
        avg = category_average(student_id, cid)
        if avg is not None:
            weighted_sum   += avg * cat["weight"]
            covered_weight += cat["weight"]
    if covered_weight == 0:
        return None
    return weighted_sum / covered_weight

#Main Opt. 1:
def add_student():
    global next_student_id
    print("\n-------------- Add Student --------------")
    name = input("Enter student name: ")
    if name == "":
        print("Name cannot be empty.")
        return
    students[next_student_id] = name
    print("Student added! ID:", next_student_id, "\nName:", name)
    next_student_id += 1

def view_students():
    print("\n-------------- Student List --------------")
    if len(students) == 0:
        print("No students yet.")
        return
    for sid, name in students.items():
        print("ID:", sid, " Name:", name)

def remove_student():
    print("\n------------- Remove Student -------------")
    view_students()
    sid = input("Enter student ID to remove: ")
    if not sid.isdigit():
        print("Enter a valid number.")
        return
    sid = int(sid)
    if sid not in students:
        print("Student not found.")
        return
    print("Removed:", students[sid])
    del students[sid]
    for key in list(grades.keys()):
        if key[0] == sid:
            del grades[key]

def manage_students():
    while True:
        print("\n------------ Manage Students -----------")
        print("1. Add Student")
        print("2. View Student List")
        print("3. Remove Student")
        print("0. Back")

        match input("Enter option: "):
            case "1": add_student()
            case "2": view_students()
            case "3": remove_student()
            case "0": break
            case _: print("Invalid option.")

#Main Opt. 2:
def view_categories():
    print("\n--------------- Categories ---------------")
    if len(categories) == 0:
        print("No categories yet.")
        return
    for cid, cat in categories.items():
        print("ID:", cid, " Name:", cat["name"], " Weight:", cat["weight"], "%")

def add_category():
    global next_category_id
    print("\n-------------- Add Category --------------")
    name = input("Category name (e.g. Homework): ")
    if name == "":
        print("Name cannot be empty.")
        return
    weight = input("Weight in % (e.g. 30): ")
    if not weight.replace(".", "", 1).isdigit():
        print("Enter a valid number.")
        return
    categories[next_category_id] = {"name": name, "weight": float(weight)}
    print("Category added! ID:", next_category_id, " Name:", name, " Weight:", weight, "%")
    next_category_id += 1

def edit_category_weight():
    print("\n---------- Edit Category Weight ----------")
    view_categories()
    cid = input("Enter category ID: ")
    if not cid.isdigit():
        print("Enter a valid number.")
        return
    cid = int(cid)
    if cid not in categories:
        print("Category not found.")
        return
    new_weight = input("New weight in %: ")
    if not new_weight.replace(".", "", 1).isdigit():
        print("Please enter a valid number.")
        return
    categories[cid]["weight"] = float(new_weight)
    print("Weight updated!")

def view_assignments():
    print("\n--------------- Assignments --------------")
    if len(assignments) == 0:
        print("No assignments yet.")
        return
    for aid, a in assignments.items():
        cat_name = categories[a["category_id"]]["name"]
        print("ID:", aid, " Name:", a["name"], " Category:", cat_name, " Max Points:", a.get("max_points", 100))

def add_assignment():
    global next_assignment_id
    print("\n------------- Add Assignment -------------")
    if len(categories) == 0:
        print("No categories yet. Add a category first.")
        return
    view_categories()
    cid = input("Enter category ID: ")
    if not cid.isdigit():
        print("Enter a valid number.")
        return
    cid = int(cid)
    if cid not in categories:
        print("Category not found.")
        return
    name = input("Assignment name (e.g. HW 1): ")
    if name == "":
        print("Name cannot be empty.")
        return
    max_points = input("Max points (press Enter for default 100): ")
    if max_points == "":
        max_points = 100.0
    elif not max_points.replace(".", "", 1).isdigit():
        print("Invalid number, defaulting to 100.")
        max_points = 100.0
    else:
        max_points = float(max_points)
    assignments[next_assignment_id] = {"name": name, "category_id": cid, "max_points": max_points}
    print("Assignment added! ID:", next_assignment_id, " Name:", name, " Max Points:", max_points)
    next_assignment_id += 1

def remove_assignment():
    print("\n----------- Remove Assignment ------------")
    view_assignments()
    aid = input("Enter assignment ID to remove: ")
    if not aid.isdigit():
        print("Please enter a valid number.")
        return
    aid = int(aid)
    if aid not in assignments:
        print("Assignment not found.")
        return
    print("Removed:", assignments[aid]["name"])
    del assignments[aid]
    for key in list(grades.keys()):
        if key[1] == aid:
            del grades[key]

def manage_categories():
    while True:
        print("\n--- Manage Categories and Assignments  ---")
        print("1. View Categories")
        print("2. Add Category")
        print("3. Edit Category Weight")
        print("4. Add Assignment")
        print("5. View Assignments")
        print("6. Remove Assignment")
        print("0. Back")

        match input("Enter option: "):
            case "1": view_categories()
            case "2": add_category()
            case "3": edit_category_weight()
            case "4": add_assignment()
            case "5": view_assignments()
            case "6": remove_assignment()
            case "0": break
            case _: print("Invalid option.")

#Main Opt. 3:
def enter_grades():
    print("\n------- Enter Grades for a Student -------")
    if len(students) == 0:
        print("No students yet.")
        return
    if len(assignments) == 0:
        print("No assignments yet.")
        return

    view_students()
    sid = input("Enter student ID: ")
    if not sid.isdigit():
        print("Enter a valid number.")
        return
    sid = int(sid)
    if sid not in students:
        print("Student not found.")
        return

    print("\nEntering grades for:", students[sid])
    print("(Press Enter to skip an assignment)")

    for cid, cat in categories.items():
        print("\n[", cat["name"], "-", cat["weight"], "% ]")
        for aid, a in assignments.items():
            if a["category_id"] == cid:
                max_pts = a.get("max_points", 100)
                current = grades.get((sid, aid))
                if current is not None:
                    print(" ", a["name"], f"(current: {current}/{max_pts})")
                else:
                    print(" ", a["name"], f"(out of {max_pts})")
                score = input(f"  Score (0-{max_pts}): ")
                if score == "":
                    continue
                if not score.replace(".", "", 1).isdigit():
                    print("  Invalid score, skipped.")
                    continue
                score = float(score)
                if score < 0 or score > max_pts:
                    print(f"  Score out of range (0-{max_pts}), skipped.")
                    continue
                grades[(sid, aid)] = score
    final = final_grade(sid)
    if final is not None:
        print("\nGrades saved! Final grade:", round(final, 2), "-", letter_grade(final))
    else:
        print("\nGrades saved!")

def edit_grade():
    print("\n-------------- Edit a Grade --------------")
    if len(students) == 0:
        print("No students yet.")
        return

    view_students()
    sid = input("Enter student ID: ")
    if not sid.isdigit():
        print("Enter a valid number.")
        return
    sid = int(sid)
    if sid not in students:
        print("Student not found.")
        return

    view_categories()
    cid = input("Enter category ID: ")
    if not cid.isdigit():
        print("Enter a valid number.")
        return
    cid = int(cid)
    if cid not in categories:
        print("Category not found.")
        return

    print("\nAssignments in", categories[cid]["name"])
    found = False
    for aid, a in assignments.items():
        if a["category_id"] == cid:
            max_pts = a.get("max_points", 100)
            current = grades.get((sid, aid))
            if current is not None:
                print("ID:", aid, " Name:", a["name"], f" Grade: {current}/{max_pts}")
            else:
                print("ID:", aid, " Name:", a["name"], f" Grade: Not graded (out of {max_pts})")
            found = True
    if not found:
        print("No assignments in this category.")
        return

    aid = input("Enter assignment ID: ")
    if not aid.isdigit():
        print("Enter a valid number.")
        return
    aid = int(aid)
    if aid not in assignments:
        print("Assignment not found.")
        return
    if assignments[aid]["category_id"] != cid:
        print("Assignment does not belong to that category.")
        return

    max_pts = assignments[aid].get("max_points", 100)
    score = input(f"New score (0-{max_pts}): ")
    if not score.replace(".", "", 1).isdigit():
        print("Invalid score.")
        return
    score = float(score)
    if score < 0 or score > max_pts:
        print(f"Score out of range (0-{max_pts}).")
        return
    grades[(sid, aid)] = score
    print("Grade updated!")

def view_grade_sheet():
    print("\n--------------- Grade Sheet --------------")
    if len(students) == 0:
        print("No students yet.")
        return
    if len(assignments) == 0:
        print("No assignments yet.")
        return

    for sid, name in students.items():
        print("\nStudent:", name, "(ID:", str(sid) + ")")
        for cid, cat in categories.items():
            avg = category_average(sid, cid)
            if avg is not None:
                print(" ", cat["name"], "avg:", round(avg, 2))
            else:
                print(" ", cat["name"], "avg: No grades yet")
            for aid, a in assignments.items():
                if a["category_id"] == cid:
                    max_pts = a.get("max_points", 100)
                    g = grades.get((sid, aid))
                    if g is not None:
                        print("   -", a["name"] + ":", f"{g}/{max_pts}")
                    else:
                        print("   -", a["name"] + ": Not graded")
        final = final_grade(sid)
        if final is not None:
            print(" Final:", round(final, 2), "-", letter_grade(final))
        else:
            print(" Final: No grades yet")

def manage_grades():
    while True:
        print("\n------------- Manage Grades --------------")
        print("1. Enter Grades for a Student")
        print("2. Edit a Grade")
        print("3. View Grade Sheet")
        print("0. Back")

        match input("Enter option: "):
            case "1": enter_grades()
            case "2": edit_grade()
            case "3": view_grade_sheet()
            case "0": break
            case _: print("Invalid option.")

#Main Opt. 4:
def view_grade_statistics():
    print("\n------------ Grade Statistics ------------")
    
    if len(students) == 0:
        print("No students yet.")
        return

    totals = []

    for sid, name in students.items():
        final = final_grade(sid)

        if final is not None:
            totals.append(final)
            print("ID:", sid,
                  "| Name:", name,
                  "| Final Grade:", round(final, 2),
                  "| Letter Grade:", letter_grade(final))
        else:
            print("ID:", sid,
                  "| Name:", name,
                  "| Final Grade: No grades yet")

    if len(totals) == 0:
        print("\nNo grades available for statistics.")
        return

    highest = max(totals)
    lowest  = min(totals)
    average = sum(totals) / len(totals)

    print("\nOverall Statistics")
    print("Highest Grade :", round(highest, 2))
    print("Lowest Grade  :", round(lowest, 2))
    print("Class Average :", round(average, 2))

#Main Opt. 5:
def generate_report_card():
    print("\n---------- Generate Report Card ----------")

    if len(students) == 0:
        print("No students yet.")
        return

    print("1. One Student")
    print("2. All Students")

    option = input("Enter option: ")

    if option == "1":
        view_students()

        sid = input("Enter student ID: ")

        if not sid.isdigit():
            print("Enter a valid number.")
            return

        sid = int(sid)

        if sid not in students:
            print("Student not found.")
            return

        print("\n════════ REPORT CARD ════════")
        print("Student ID :", sid)
        print("Student Name :", students[sid])

        for cid, cat in categories.items():
            print("\n", cat["name"], "-", cat["weight"], "%")

            for aid, a in assignments.items():
                if a["category_id"] == cid:
                    g = grades.get((sid, aid))

                    if g is not None:
                        print(" -", a["name"] + ":", g)
                    else:
                        print(" -", a["name"] + ": Not graded")

            avg = category_average(sid, cid)

            if avg is not None:
                print(" Category Average:", round(avg, 2))
            else:
                print(" Category Average: No grades yet")

        final = final_grade(sid)

        if final is not None:
            print("\nFinal Grade :", round(final, 2))
            print("Letter Grade:", letter_grade(final))
        else:
            print("\nFinal Grade : No grades yet")

        print("═════════════════════════════")

    elif option == "2":

        for sid, name in students.items():

            print("\n════════ REPORT CARD ════════")
            print("Student ID :", sid)
            print("Student Name :", name)

            for cid, cat in categories.items():
                print("\n", cat["name"], "-", cat["weight"], "%")

                for aid, a in assignments.items():
                    if a["category_id"] == cid:
                        g = grades.get((sid, aid))

                        if g is not None:
                            print(" -", a["name"] + ":", g)
                        else:
                            print(" -", a["name"] + ": Not graded")

                avg = category_average(sid, cid)

                if avg is not None:
                    print(" Category Average:", round(avg, 2))
                else:
                    print(" Category Average: No grades yet")

            final = final_grade(sid)

            if final is not None:
                print("\nFinal Grade :", round(final, 2))
                print("Letter Grade:", letter_grade(final))
            else:
                print("\nFinal Grade : No grades yet")

            print("═════════════════════════════")

    else:
        print("Invalid option.")

# Main Menu:
def main():
    while True:
        print("══════════════════════════════════════════\n" \
              "            Gradebook Manager             \n" \
              "══════════════════════════════════════════\n")
        print("1. Manage Students")
        print("2. Manage Categories and Assignments")
        print("3. Manage Grades")
        print("4. View Grade Statistics")
        print("5. Generate Report Card")
        print("0. Exit")

        match input("Enter option: "):
            case "1": manage_students()
            case "2": manage_categories()
            case "3": manage_grades()
            case "4": view_grade_statistics()
            case "5": generate_report_card()
            case "0":
                print("Thanks. Program exiting...")
                break
            case _: print("Invalid option.")

main()