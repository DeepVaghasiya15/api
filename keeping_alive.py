import time
import requests

# URL of your Flask app
url = 'https://api-9bea.onrender.com'

def keep_alive():
    while True:
        try:
            # Make a GET request to keep the server alive
            response = requests.get(url)
            if response.status_code == 200:
                print("Successfully pinged the server.")
            else:
                print(f"Failed to ping the server. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        # Wait for 10 minutes before sending the next request
        time.sleep(60)

# keep_alive()