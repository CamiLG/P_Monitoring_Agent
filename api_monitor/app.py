from flask import Flask, request, jsonify
from datetime import datetime
from csv_writer import save_to_csv
from csv_reader import get_csv_by_ip
from models import SystemInfo
from database import Session, init_db

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Get ip address from monitoring agent
        ip_address = request.remote_addr

        datetime_str = datetime.now().strftime("%Y-%m-%d")

        # Save the data to a CSV file with the IP address 
        save_to_csv(data, ip_address, datetime_str) 
        
        # Save the data to the database
        session = Session()
        info = SystemInfo(
            timestamp=data.get("timestamp"),
            ip_address=ip_address,
            processor=data.get("processor"),
            os_name=data.get("os_name"),
            os_version=data.get("os_version"),
            running_processes=str(data.get("running_processes")),
            logged_in_users=str(data.get("logged_in_users"))
        )

        session.add(info)
        session.commit()
        session.close()

        return jsonify({"message": "Data received successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/data/<ip_address>', methods=['GET'])
def get_data(ip_address):
    """Get data for a specific IP address."""
    ip_address = ip_address.strip() # Get the IP address from the URL 
    if not ip_address:
        return jsonify({"error": "IP address is required"}), 400
    data = get_csv_by_ip(ip_address)
    if not data:
        return jsonify({"error": f"No data found for this IP address: {ip_address}"}), 404
    return jsonify(data), 200

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok"}), 200
    
init_db() # Initialize the database

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
