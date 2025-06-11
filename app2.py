# import requests

# url = "http://192.168.1.17:8000/ask_chat"
# data = {"message": "HI"}

# response = requests.post(url, json=data)

# print("Response status code:", response.status_code)
# print("Response body:", response.text)

# import requests

# url = "http://127.0.0.1:8000/food/create1/"
# headers = {
#     "Content-Type": "application/json"
# }

# data = {
#     "user": 20,  # Use the correct user ID or omit if nullable
#     "namefood": "momo",
#     "nut_info": "**Protein**: 20\n**Fat**: 10\n**Calories**: 350\n**Vitamin C**: 40%",
#     "health": "Rich in lean protein and antioxidants.",
#     "recipy": "Grill the chicken, chop vegetables, and toss with olive oil dressing."
# }

# response = requests.post(url, json=data, headers=headers)

# print("Status Code:", response.status_code)
# # print("Response JSON:", response.json())
# import requests

# # Replace with the path to your test image
# image_path = "api\\x.jpeg"

# # Replace with the actual user ID you want to test with
# user_id = "20"

# url = "https://mmm12212.pythonanywhere.com/send_image"

# with open(image_path, 'rb') as image_file:
#     files = {
#         'file': (image_path, image_file, 'image/jpeg')
#     }
#     data = {
#         'user_id': user_id
#     }

#     response = requests.post(url, files=files, data=data)

#     try:
#         response.raise_for_status()
#         print("✅ Success:", response.json())
#     except requests.exceptions.HTTPError as err:
#         print("❌ HTTP Error:", err)
#         print("Response content:", response.text)
#     except Exception as e:
#         print("❌ Error:", e)
import requests

url = "https://mmm12212.pythonanywhere.com/ask_chat"
payload = {
    "user_id": 20,
    "message": "What's a good diet plan for athletes?"
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())