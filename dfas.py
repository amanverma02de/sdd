import os
import csv
from pathlib import Path

def create_dummy_csv_files(directory, num_files):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    for i in range(num_files):
        file_name = f"energy_data_{i+1}.csv"
        file_path = directory / file_name

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Energy Consumption"])
            for j in range(10):
                writer.writerow([f"2022-01-{j+1} 00:00:00", f"{j*10} kWh"])

    print(f"Created {num_files} dummy CSV files in {directory}")


if __name__ == "__main__":
    directory = "dummy_data"
    num_files = 5
    create_dummy_csv_files(directory, num_files)
