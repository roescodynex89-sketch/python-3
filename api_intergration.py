import requests

# ১. API এর URL (আমরা একটি ফ্রি ফেক API ব্যবহার করছি)
BASE_URL = "https://typicode.com"


# --- ক. GET Request (ডাটা নিয়ে আসা) ---
def get_post_data(post_id: int) -> None:
    response = requests.get(f"{BASE_URL}/{post_id}")
    
    if response.status_code == 200:
        # response.json() অটোমেটিক JSON-কে পাইথন ডিকশনারি বানিয়ে দেয়
        data = response.json() 
        print("--- GET Success ---")
        print(f"Title: {data['title']}\n")
    else:
        print("Failed to fetch data")


# --- খ. POST Request (নতুন ডাটা পাঠানো) ---
def create_new_post(title: str, body: str) -> None:
    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }
    
    # json= প্যারামিটার দিলে requests লাইব্রেরি নিজেই ডিকশনারিকে JSON বানিয়ে পাঠায়
    response = requests.post(BASE_URL, json=payload)
    
    if response.status_code == 201: # 201 মানে Created
        print("--- POST Success ---")
        print("Server Response:", response.json())
    else:
        print("Failed to send data")


# ফাংশনগুলো রান করে দেখা
get_post_data(1)
create_new_post("Learning API Integration", "It is very straightforward in Python!")