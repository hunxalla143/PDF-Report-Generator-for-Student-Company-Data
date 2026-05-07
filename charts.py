import matplotlib.pyplot as plt
import os


def create_student_chart(data):

    try:

        # Create assets folder
        os.makedirs("assets", exist_ok=True)

        names = []
        marks = []

        # Extract student data
        for item in data:

            names.append(item['name'])
            marks.append(int(item['marks']))

        # Create chart
        plt.figure(figsize=(6, 4))

        plt.bar(names, marks)

        plt.xlabel("Students")
        plt.ylabel("Marks")
        plt.title("Student Performance")

        plt.tight_layout()

        # Save chart
        plt.savefig("assets/chart.png")

        plt.close()

        print("Chart generated successfully.")

    except Exception as e:
        print(f"Error creating chart: {e}")