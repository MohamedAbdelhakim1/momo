from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import   RegisterSerializer
from .models import   Register
from .serializers import *
import requests
from .serializers import Food1Serializer ,ChatSerializer
from .models import Food1 ,Chat
from datetime import datetime, timedelta
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/registers/',
            'method': 'GET',
            'body': None,
            'description': 'Get all user registers',
        },
        {
            'Endpoint': '/registers/create/',
            'method': 'POST',
            'body': {
                "name": "string",
                "email": "string",
                "password": "string",
                "phone": "string",
                "gender": "string",
                "height": "decimal",
                "weight": "decimal",
                "disease": "string",
                "age": "integer"
            },
            'description': 'Create a new user register',
        },
        {
            'Endpoint': '/registers/<str:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Get a specific user register by ID',
        },
        {
            'Endpoint': '/registers/<str:pk>/update/',
            'method': 'PUT',
            'body': {
                "name": "string",
                "email": "string",
                "password": "string",
                "phone": "string",
                "gender": "string",
                "height": "decimal",
                "weight": "decimal",
                "disease": "string",
                "age": "integer"
            },
            'description': 'Update a user register',
        },
        {
            'Endpoint': '/registers/<str:pk>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete a user register',
        },
        {
            'Endpoint': '/foods/',
            'method': 'GET',
            'body': None,
            'description': 'Get all Food1 entries',
        },
        {
            'Endpoint': '/food/create1/',
            'method': 'POST',
            'body': {
                "user_id": "integer (user id)",
                "namefood": "string",
                "nut_info": "string",
                "health": "string",
                "recipy": "string"
            },
            'description': 'Create a new Food1 entry',
        },
        {
            'Endpoint': '/food/<str:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Get a specific Food1 entry by ID',
        },
        {
            'Endpoint': '/food/<str:pk>/update/',
            'method': 'PUT',
            'body': {
                "user_id": "integer (user id)",
                "namefood": "string",
                "nut_info": "string",
                "health": "string",
                "recipy": "string"
            },
            'description': 'Update a Food1 entry',
        },
        {
            'Endpoint': '/food/<str:pk>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete a Food1 entry',
        },
        {
            'Endpoint': '/fooddate/<str:date>/?range=day|week|month&user_id=<user_id>',
            'method': 'GET',
            'body': None,
            'description': 'Get Food1 entries filtered by date and optional user',
        },
        {
            'Endpoint': '/chat/',
            'method': 'GET',
            'body': None,
            'description': 'Get all chat messages',
        },
        {
            'Endpoint': '/chat/create/',
            'method': 'POST',
            'body': {
                "user_id": "integer (user id)",
                "usermessage": "string",
                "botmessage": "string"
            },
            'description': 'Create a chat message',
        },
        {
            'Endpoint': '/chat/<str:pk>/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete a chat message',
        },
        {
            'Endpoint': '/food/create/',
            'method': 'POST',
            'body': {
                "namefood": "string",
                "Calories": "decimal",
                "Protein": "decimal",
                "Carbohydrates": "decimal",
                "Dietary_Fiber": "decimal",
                "Sugars": "decimal",
                "Fat": "decimal",
                "Sodium": "decimal",
                "Potassium": "decimal",
                "health": "string",
                "recipy": "string"
            },
            'description': 'Create a Food entry (nutrition info from image)',
        },
        {
            'Endpoint': '/api-token-auth/',
            'method': 'POST',
            'body': {
                "username": "string",
                "password": "string"
            },
            'description': 'Obtain auth token by providing username and password',
        },
        {
            'Endpoint': '/upload_image/',
            'method': 'POST',
            'body': {
                "file": "image file"
            },
            'description': 'Upload an image and get nutrition info processed',
        },
        {
            'Endpoint': '/get-image/<filename>/',
            'method': 'GET',
            'body': None,
            'description': 'Retrieve an uploaded image by filename',
        },
    ]
    return Response(routes)

#--- user ---
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

#--- chat ---
@api_view(['GET'])
def getchat(request):
    chat = Chat.objects.all()
    serializer = ChatSerializer(chat, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createchat(request):
    serializer = ChatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteChat(request, pk):
    chat = Chat.objects.get(id=pk)
    chat.delete()
    return Response('Register was deleted')
#--- food ---
@api_view(['GET'])
def getFood1s(request):
    food1 = Food1.objects.all()
    serializer = Food1Serializer(food1, many=True)
    return Response(serializer.data)

def getFood1(request, pk):
    food1 = Food1.objects.get(id=pk)
    serializer = Food1Serializer(food1, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getFood1date(request, date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        range_type = request.GET.get('range', 'day')  # default is 'day'
        user_id = request.GET.get('user_id')  # Get user ID from query params

        # Determine date range
        if range_type == 'week':
            start_date = date_obj - timedelta(days=6)
            end_date = date_obj
        elif range_type == 'month':
            start_date = date_obj - timedelta(days=29)
            end_date = date_obj
        else:  # exact day
            start_date = end_date = date_obj

        # Build base queryset
        food1_queryset = Food1.objects.filter(created_at__range=(start_date, end_date))

        # If user_id is provided, filter by it
        if user_id:
            food1_queryset = food1_queryset.filter(user_id=user_id)

        serializer = Food1Serializer(food1_queryset, many=True)
        return Response(serializer.data)

    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)
@api_view(['POST'])
def createFood1(request):
    serializer = Food1Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateFood1(request, pk):
    food1 = Food1.objects.get(id=pk)
    serializer = Food1Serializer(food1, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteFood1(request, pk):
    food1 = Food1.objects.get(id=pk)
    food1.delete()
    return Response('Register was deleted')



