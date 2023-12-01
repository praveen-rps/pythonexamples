import requests

def send_data_to_spring_boot_api(data):
    # Replace the URL with the actual endpoint of your Spring Boot REST API
    api_url = 'http://localhost:8081/notes/create'

    try:
        # Make a POST request to the Spring Boot REST API with the provided data
        response = requests.post(api_url, json=data)

        # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
            print("Data sent successfully.")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example data to send to the Spring Boot API
    data_to_send = {
        "pid": 1004,
        "author": "John Doe",
        "title": "salesforce",
        "description": "best admin tool for the hrs"
    }

    send_data_to_spring_boot_api(data_to_send)
