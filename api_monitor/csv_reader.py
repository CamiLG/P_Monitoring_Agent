import os
import csv

def get_csv_by_ip(ip_address):
    """Get the CSV file path for a given IP address."""
    folder = "api_monitor/data" 
    data = []
    
    if not os.path.exists(folder):
        return data  # Return empty list if folder does not exist

    files = [f for f in os.listdir(folder) if f.startswith(f"{ip_address}_") and f.endswith('.csv')]

    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, mode='r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

    return data