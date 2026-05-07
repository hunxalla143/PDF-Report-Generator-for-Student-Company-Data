import csv
import json


def load_csv(file_path):
    data = []

    try:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

        print("CSV data loaded successfully.")

    except FileNotFoundError:
        print("Error: CSV file not found.")

    except Exception as e:
         print(f"Error loading CSV: {e}")

    return data



def load_json(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print("JSON data loaded successfully.")
        return data

    except FileNotFoundError:
        print("Error: JSON file not found.")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")

    except Exception as e:
        print(f"Error loading JSON: {e}")

    return []