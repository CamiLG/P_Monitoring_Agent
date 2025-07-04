import schedule
import time
from collector import collect_data
from sender import send_data_to_api


# This is a simple monitoring agent that collects availability data from a server and send it to an API.

API_URL = "https://api:5050/api/data" #Replace with the corresponding API URL

def job():
    """Job to collect data and send it to the API."""
    data = collect_data()
    if data:
        response = send_data_to_api(API_URL, data)
        if response:
            print("Data sent successfully.")
        else:
            print("Failed to send data.")
    else:
        print("No data collected.")

def main():
    """Main function to schedule the job."""
    schedule.every().day.at("00:00").do(job)  # Schedule the job to run daily at midnight
    # schedule.every(1).minutes.do(job) # Uncomment for testing every minute
    print("Monitoring agent started. Waiting for the scheduled time...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Sleep for a while to avoid busy waiting

if __name__ == "__main__":
    main()