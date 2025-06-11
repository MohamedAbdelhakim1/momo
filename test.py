from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn
import shutil
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "This is My Nutrionguid App FAST"}

def nutrition_data(nutrition_info):
    nutrition_data = {}

    nutrition_elements = [
        "Calories", "Protein", "Carbohydrates", "Dietary Fiber",
        "Sugars", "Fat", "Sodium", "Potassium"
    ]

    lines = nutrition_info.split('\n')

    for line in lines:
        if not line.strip():
            continue

        for element in nutrition_elements:
            if element in line:
                value_part = line.split('')[-1].split(':')[-1].strip()
                if element == "Calories":
                    value = ''.join(filter(str.isdigit, value_part))  # Keep only digits
                else:
                    first_token = value_part.split()[0]
                    value = ''.join(filter(lambda c: c.isdigit() or c == '.', first_token))  # Keep digits and decimal point

                # Use "Dietary_Fiber" as key instead of "Dietary Fiber"
                key = "Dietary_Fiber" if element == "Dietary Fiber" else element
                nutrition_data[key] = value
                break

    return nutrition_data

def send_information_back(food_data, nutrition_data):
    url = "https://momo66.pythonanywhere.com/food/create/"
    payload = {
        "namefood": food_data["Predicted_label"],
        "Calories": float(nutrition_data["Calories"]),
        "Protein": float(nutrition_data["Protein"]),
        "Carbohydrates": float(nutrition_data["Carbohydrates"]),
        "Dietary_Fiber": float(nutrition_data["Dietary_Fiber"]),
        "Sugars": float(nutrition_data["Sugars"]),
        "Fat": float(nutrition_data["Fat"]),
        "Sodium": float(nutrition_data["Sodium"]),
        "Potassium": float(nutrition_data["Potassium"]),
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


@app.post("/send_image")
async def predict_image_and_nutrition(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        
        file_location = f"./media/api/{file.filename}"
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Send the image to the external endpoint
        with open(file_location, "rb") as image_file:
            files = {"file": (file.filename, image_file, file.content_type)}
            response = requests.post("https://1mb1-nutritionguide.hf.space/predictNUT", files=files)
            data= response.json()
            # print(data)
            nutritoio_inform= nutrition_data(data['Nutrition_info'])
            # print(nutritoio_inform)
            send_information_back(data,nutritoio_inform)
        # Return the response from the external endpoint
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"An error occurred: {str(e)}"}
        )
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("te:app", host="0.0.0.0", port=8000, reload=True)