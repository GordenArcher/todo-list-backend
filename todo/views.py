from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TodoTable
from .serializers import TodoSerializer, TodoTableUserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
def register(request):

    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    password2 = request.data.get('password2')

    if password == password2:
        if User.objects.filter(username=username).exists():
            return Response({"error":f"{username} already exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({"error":f"{email} already exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            todo_entry = TodoTable.objects.create(user=user)

            serializer = TodoTableUserSerializer(todo_entry)

            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                "success": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        
    else:
        return Response({"error":"password does not match"}, status=status.HTTP_400_BAD_REQUEST)    




@api_view(['POST'])
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'success': 'Login successful',
            'token': token.key,
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error":"Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_todo(request):
    if request.method == 'POST':
        todo_input = request.data.get("todo", None)

        print("Todo Input:", todo_input) 

        if not todo_input:
            return Response({"error": "Todo input cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        send_todo = TodoTable.objects.create(todo=todo_input, user=request.user)

        serializer = TodoSerializer(send_todo)

        return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getTodo(request):
    alltodo = TodoTable.objects.filter(user=request.user)
    serializer = TodoSerializer(alltodo, many=True)

    return Response(serializer.data)