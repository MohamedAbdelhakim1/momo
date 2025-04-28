from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import   PhotoSerializer, RegisterSerializer
from .models import   Photo, Register 
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
import requests

import os
from django.core.files.base import ContentFile
from rest_framework import viewsets
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .models import food

app = FastAPI()

@api_view(['GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint': '/back/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes',
        },
        {
            'Endpoint': '/back/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object',
        },
        {
            'Endpoint': '/back/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Create new notes',
        },
        {
            'Endpoint': '/back/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing note with data',
        },
        {
            'Endpoint': '/back/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note',
        }
    ]
    return Response(routes)



@api_view(['GET'])
def getRegisters(request):
    registers = Register.objects.all()
    serializer = RegisterSerializer(registers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRegister(request, pk):
    register = Register.objects.get(id=pk)
    serializer = RegisterSerializer(register, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createRegister(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateRegister(request, pk):
    register = Register.objects.get(id=pk)
    serializer = RegisterSerializer(register, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteRegister(request, pk):
    register = Register.objects.get(id=pk)
    register.delete()
    return Response('Register was deleted')
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-uploaded_at')
    serializer_class = PhotoSerializer


import requests
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
                value_part = line.split('**')[-1].split(':')[-1].strip()
                if element == "Calories":
                    value = ''.join(filter(str.isdigit, value_part))  # Keep only digits
                else:
                    first_token = value_part.split()[0]
                    value = ''.join(filter(lambda c: c.isdigit() or c == '.', first_token))  # Keep digits and decimal point
                nutrition_data[element] = value
                break
    
    return nutrition_data

def send_image_to_backend(file_path):
    url = "https://1mb1-nutritionguide.hf.space/predictNUT"
    with open(file_path, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post(url, files=files)
        response_data = response.json()
        nutrationinformation=nutrition_data(response_data.get('Nutrition_info', ''))
    if response.status_code == 200:
        
        # Save the response data into the food model
        food_instance = food(
            namefood=response_data.get('Predicted_label', 'Unknown'),
            Calories=float(nutrationinformation.get('Calories', 0.00)),
            Protein=float(nutrationinformation.get('Protein', 0.00)),
            Carbohydrates=float(nutrationinformation.get('Carbohydrates', 0.00)),
            Dietary_Fiber=float(nutrationinformation.get('Dietary Fiber', 0.00)),
            Sugars=float(nutrationinformation.get('Sugars', 0.00)),
            Fat=float(nutrationinformation.get('Fat', 0.00)),
            Sodium=float(nutrationinformation.get('Sodium', 0.00)),
            Potassium=float(nutrationinformation.get('Potassium', 0.00)),
            health=response_data.get('Information', ''),
            recipy=response_data.get('Recipes', '')
        )
        food_instance.save()
        return response_data
    else:
        raise Exception(f"Failed to send image. Status Code: {response.status_code}, Response: {response.text}")


@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        file_name = default_storage.save(f"media/api/{file.name}", ContentFile(file.read()))
        file_path = default_storage.path(file_name)  # Get the full file path

        try:
            response_data = send_image_to_backend(file_path)  # Send the saved file to the backend function
            return JsonResponse({
                "message": "File uploaded successfully",
                "file_path": file_name,
                "response_data": response_data
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

@app.get("/get-image/{filename}")
def get_image(filename: str):
    file_path = f"media/api/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}

# class ImageUploadView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = ImageUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             file = serializer.validated_data['file']
#             # Save the file or process it as needed
#             file_path = f'media/uploads/{file.name}'
#             with open(file_path, 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)
#             return Response({'message': 'File uploaded successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



