import os 
import csv

def save_to_csv(data, ip_address, datetime_str):
    """Save data to a CSV file with the IP address."""
    filename = f"{ip_address}_{datetime_str}.csv"

    # Create the directory if it does not exist
    folder = "api_monitor/data"
    os.makedirs(folder, exist_ok=True)

    filename = os.path.join(folder, f"{ip_address}_{datetime_str}.csv")

    file_exists = os.path.isfile(filename)

    # Flat Data from nested structures
    flat_data = {}
    for key, value in data.items():
        if isinstance(value, list):
            flat_data[key] = str(value)
        else:
            flat_data[key] = value
    
    # Write to CSV file
    with open(filename, mode='a', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=flat_data.keys())
        
        if not file_exists:
            writer.writeheader()

        writer.writerow(flat_data)