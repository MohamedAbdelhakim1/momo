# import requests
# url = "http://127.0.0.1:8000/upload-image/"
# # url = "https://1mb1-nutritionguide.hf.space/predictNUT"
# image_path = r"api\x.jpeg"
# with open(image_path, 'rb') as image_file:
#     files = {'file': image_file}
#     print("File opened successfully")
#     response = requests.post(url, files=files)
# if response.status_code == 200:
#     json_response = response.json()
#     print("Statusssssssss Code:", json_response)
# else:
#     print("Failed to send image")
#     print("Status Code:", response)
#     print("Response:", response.text)
   
import requests

# url = "http://momo66.pythonanywhere.com/chat/create"
url = "http://192.168.1.19:8000/ask_chat"
data = {"message": "hi"}

response = requests.post(url, json=data)
print(response)  # Or response.text if it's not JSON
print(response.json())  # Or response.text if it's not JSON
