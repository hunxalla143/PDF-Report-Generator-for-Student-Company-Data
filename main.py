from data_loader import load_csv, load_json
from pdf_generator import generate_pdf
from charts import create_student_chart
from security import protect_pdf
from utils import generate_filename


# ==========================================
# MANUAL DATA ENTRY
# ==========================================

def add_manual_data():

    data = []

    print("\n===== ADD DATA =====")

    report_choice = input(
        "Enter report type (student/company): "
    ).lower()

    try:
        total = int(input("How many entries do you want to add? "))

    except ValueError:
        print("Invalid number.")
        return [], ""

    for i in range(total):

        print(f"\nEnter data for record {i + 1}")

        name = input("Name: ")
        user_id = input("ID: ")
        email = input("Email: ")

        # ==========================================
        # STUDENT REPORT
        # ==========================================

        if report_choice == 'student':

            course = input("Course: ")
            marks = input("Marks: ")
            attendance = input("Attendance: ")

            data.append({
                'name': name,
                'id': user_id,
                'email': email,
                'course': course,
                'marks': marks,
                'attendance': attendance
            })

        # ==========================================
        # COMPANY REPORT
        # ==========================================

        elif report_choice == 'company':

            role = input("Role: ")
            performance = input("Performance: ")

            data.append({
                'name': name,
                'id': user_id,
                'email': email,
                'role': role,
                'performance': performance
            })

        else:
            print("Invalid report type.")
            return [], ""

    return data, report_choice


# ==========================================
# MAIN MENU
# ==========================================

def menu():

    data = []
    report_type = ""

    while True:

        print("\n========== PDF REPORT GENERATOR ==========")
        print("1. Add Data")
        print("2. Load CSV Data")
        print("3. Load JSON Data")
        print("4. Generate PDF")
        print("5. Password Protect PDF")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # ==========================================
        # ADD DATA
        # ==========================================

        if choice == '1':

            try:
                data, report_type = add_manual_data()

                if data:
                    print("Data added successfully.")

            except Exception as e:
                print(f"Error adding data: {e}")

        # ==========================================
        # LOAD CSV DATA
        # ==========================================

        elif choice == '2':

            try:
                path = input("Enter CSV file path: ")

                data = load_csv(path)

                if data:
                    report_type = input(
                        "Enter report type (Student/Company): "
                    )

                    print("CSV data loaded successfully.")

            except Exception as e:
                print(f"Error loading CSV: {e}")

        # ==========================================
        # LOAD JSON DATA
        # ==========================================

        elif choice == '3':

            try:
                path = input("Enter JSON file path: ")

                data = load_json(path)

                if data:
                    report_type = input(
                        "Enter report type (Student/Company): "
                    )

                    print("JSON data loaded successfully.")

            except Exception as e:
                print(f"Error loading JSON: {e}")

        # ==========================================
        # GENERATE PDF
        # ==========================================

        elif choice == '4':

            if not data:
                print("No data available.")
                continue

            try:

                # STUDENT REPORT CHART
                if report_type.lower() == 'student':
                    create_student_chart(data)

                # UNIQUE FILE NAME
                filename = generate_filename(
                    report_type.lower() + "_report"
                )

                # GENERATE PDF
                pdf_path = generate_pdf(
                    data,
                    report_type,
                    filename
                )

                print(f"PDF generated successfully: {pdf_path}")

            except Exception as e:
                print(f"Error generating PDF: {e}")

        # ==========================================
        # PASSWORD PROTECT PDF
        # ==========================================

        elif choice == '5':

            try:
                input_pdf = input("Enter PDF path: ")

                output_pdf = input(
                    "Enter protected PDF filename: "
                )

                password = input("Enter password: ")

                protect_pdf(
                    input_pdf,
                    output_pdf,
                    password
                )

            except Exception as e:
                print(f"Error protecting PDF: {e}")

        # ==========================================
        # EXIT
        # ==========================================

        elif choice == '6':

            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == '__main__':
    menu()