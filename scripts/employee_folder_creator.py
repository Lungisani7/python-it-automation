import csv
import os

BASE_DIR = "generated_employee_folders"
CSV_FILE = "sample_data/employees.csv"

def create_employee_folders():
    os.makedirs(BASE_DIR, exist_ok=True)

    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            full_name = row["full_name"].strip()
            department = row["department"].strip()
            folder_name = f"{full_name}_{department}".replace(" ", "_")
            folder_path = os.path.join(BASE_DIR, folder_name)

            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_path}")

if __name__ == "__main__":
    create_employee_folders()
