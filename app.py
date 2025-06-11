from flask import Flask, request, jsonify

from flask_cors import CORS

import shutil

import requests

import os



app = Flask(__name__)

# CORS(app, resources={r"/*": {"origins": ["http://192.168.1.15:8000"]}})
CORS(app) 


@app.route("/", methods=["GET"])

def read_root():

    return jsonify({"message": "This is My Nutritionguid App FLASK"})



def send_information_back(food_data):

    url = "https://momo66.pythonanywhere.com/food/create1/"

    payload = {

        "namefood": food_data["Predicted_label"],

        "nut_info": food_data["Nutrition_info"],

        "health": food_data["Information"],

        "recipy": food_data["Recipes"]

    }

    try:

        response = requests.post(url, json=payload)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        print(f"An error occurred: {e}")

        return None



@app.route("/send_image", methods=["POST"])

def predict_image_and_nutrition():

    try:

        if 'file' not in request.files:

            return jsonify({"error": "No file part"}), 400



        file = request.files['file']



        if file.filename == '':

            return jsonify({"error": "No selected file"}), 400



        file_path = f"./temp_{file.filename}"

        file.save(file_path)



        with open(file_path, "rb") as image_file:

            files = {"file": (file.filename, image_file, file.content_type)}

            response = requests.post("https://1mb1-nutritionguide.hf.space/predictNUT", files=files)

            data = response.json()

            print(data)

            print(type(data))

            send_information_back(data)



        os.remove(file_path)



        return jsonify(data), response.status_code



    except Exception as e:

        return jsonify({"error": f"An error occurred: {str(e)}"}), 500





@app.route("/uploadpdfs", methods=["POST"])

def upload_file():

    try:

        if 'file' not in request.files:

            return jsonify({"error": "No file part"}), 400



        file = request.files['file']



        if file.filename == '':

            return jsonify({"error": "No selected file"}), 400



        temp_dir = "temp_uploads"

        os.makedirs(temp_dir, exist_ok=True)

        file_path = os.path.join(temp_dir, file.filename)



        file.save(file_path)



        with open(file_path, "rb") as f:

            files = {"file": (file.filename, f, file.content_type)}

            response = requests.post("https://1mb1-chatbotgraduation.hf.space/uploadpdfs", files=files)



        os.remove(file_path)



        if response.status_code == 200:

            return jsonify(response.json()), 200

        else:

            return jsonify({"error": "Failed to upload file to the endpoint"}), response.status_code



    except Exception as e:

        return jsonify({"error": f"An error occurred: {str(e)}"}), 500





@app.route("/ask_chat", methods=["POST"])

def ask_chat():

    try:

        data = request.get_json()

        if not data or "message" not in data:

            return jsonify({"error": "Invalid input, 'message' is required"}), 400



        payload = {"message": data["message"]}

        response = requests.post("https://1mb1-chatbotgraduation.hf.space/askbot", json=payload)

        print(response.json())

        if response.status_code == 200:

            chat_response = response.json()



            # Send the message and response to the second endpoint

            second_payload = {
                
                "usermessage": data["message"],

                "botmessage": chat_response['answer']

            }

            second_response = requests.post("https://momo66.pythonanywhere.com/chat/create/", json=second_payload)



            if second_response.status_code == 200:

                return jsonify(chat_response), 200

            else:

                return jsonify({"error": "Failed to send data to the second endpoint"}), second_response.status_code

        else:

            return jsonify({"error": "Failed to get a response from the first endpoint"}), response.status_code



    except Exception as e:

        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    

# @app.route("/ask_chat", methods=["POST"])

# def ask_chat():

#     try:

#         data = request.get_json()

#         if not data or "message" not in data:

#             return jsonify({"error": "Invalid input, 'message' is required"}), 400



#         payload = {"message": data["message"]}

#         response = requests.post("https://1mb1-chatbotgraduation.hf.space/askbot", json=payload)



#         if response.status_code == 200:

#             return jsonify(response.json()), 200

#         else:

#             return jsonify({"error": "Failed to get a response from the endpoint"}), response.status_code



#     except Exception as e:

#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500



if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000, debug=True)