import requests

def send_data_to_api(data, api_url):
    try:
        response = requests.post(api_url, json=data)
        return response.status_code, response.text
    except Exception as e:
        return "Error", str(e)
