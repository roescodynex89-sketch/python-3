import requests

# api :https://api.mydummyapi.com/comments/1
BASE_URL = "https://api.mydummyapi.com/comments/1"


#GET
def get_post_data(post_id: int) -> None:
    response = requests.get(f"{BASE_URL}/{post_id}")
    
    if response.status_code == 200:
        # response.json()  JSON DICT
        data = response.json() 
        print("--- GET Success ---")
        print(f"Title: {data['title']}\n")
    else:
        print("Failed to fetch data")


# ---  POST Request ---
def create_new_post(title: str, body: str) -> None:
    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }
    
    # json= When parameters are provided, the `requests` library automatically converts the dictionary into JSON and sends it.
    response = requests.post(BASE_URL, json=payload)
    
    if response.status_code == 201: # 201  Created
        print("--- POST Success ---")
        print("Server Response:", response.json())
    else:
        print("Failed to send data")


