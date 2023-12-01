import requests

def fetch_data_from_spring_boot_api():
    # Replace the URL with the actual endpoint of your Spring Boot REST API
   # api_url = 'http://localhost:8081/notes/display'
    # api_url = 'https://fakestoreapi.com/users'
   #api_url = 'https://fakestoreapi.com/products'
    api_url = 'https://fakestoreapi.com/carts'

    try:
        # Make a GET request to the Spring Boot REST API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Display the retrieved data
            print("Data from Spring Boot REST API:")
            for item in data:
                print(item)

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_data_from_spring_boot_api()
