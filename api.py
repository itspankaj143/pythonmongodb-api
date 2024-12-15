# import requests
# import random

# def fetch_random_user():
#     url = "https://jsonplaceholder.typicode.com/users"
#     # response = requests.get(url)
#     # data = response.json()

#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Checks for HTTP errors.
#         data = response.json()

#         if data:
#             # Select a random user from the list
#             random_user = random.choice(data[0])
#             # Extract only the name and email
#             user_info = {
#                 "name": random_user["name"],
#                 "email": random_user["email"],
#                 "username": random_user["username"],
#                 # "address": random_user["address"]
#                 "address": {
#                     "street": random_user["address"]["street"],
#                     "suite": random_user["address"]["suite"],
#                     "city": random_user["address"]["city"],
#                     "zipcode": random_user["address"]["zipcode"],
#                     "geo": {
#                         "lat": random_user["address"]["geo"]["lat"],
#                         "lng": random_user["address"]["geo"]["lng"]
#                     }
#                 }
#             }
#             return user_info
#         else:
#             return "No data found"
#     except requests.RequestException as err:
#         # Handles all requests-related exceptions
#         return f"An error occurred: {err}"
#     except Exception as e:
#         # General catch-all for other unexpected issues
#         return f"An unexpected error occurred: {e}"

# # Example usage
# random_user = fetch_random_user()
# print(random_user)
import requests
import random

def fetch_random_user():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Checks for HTTP errors.
        data = response.json()
        if data:
            # Select a random user from the list
            random_user = random.choice(data)
            return random_user  # Return the complete user object
        else:
            return "No data found"
    except requests.RequestException as err:
        # Handles all requests-related exceptions
        return f"An error occurred: {err}"
    except Exception as e:
        # General catch-all for other unexpected issues
        return f"An unexpected error occurred: {e}"

# Example usage
user_info = fetch_random_user()
print(user_info)
