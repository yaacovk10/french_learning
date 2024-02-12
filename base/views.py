from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import LessonSerializer
from .models import Lesson
from rest_framework import status
from .models import Word
from .serializers import WordSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Update user password
@api_view(['PUT'])
def update_password(request):
     # Extract username and new password from request data
    username = request.data.get('username')
    new_password = request.data.get('new_password')

     # Validate presence of required data
    if not username or not new_password:
        return Response({"error": "Username and new password are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch user and update password
        user = User.objects.get(username=username)
        user.password = make_password(new_password)
        user.save()
        return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)



# Custom TokenObtainPairSerializer to add additional claims to the JWT
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        token['password'] = user.password
        # ...


        return token

# API View for Lessons
class Lesson_view(APIView):
    # Retrieve a single lesson by pk or all lessons if pk is None
    def get(self, request, pk=None):
        if pk is not None:
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonSerializer(lesson)
            return Response(serializer.data)
        else:
            lessons = Lesson.objects.all()
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data)
    
    # Create a new lesson
    def post(self, request):
        serializer = LessonSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   # Update an existing lesson
    def put(self, request, pk):
        my_model = Lesson.objects.get(pk=pk)
        serializer = LessonSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   # Delete a lesson
    def delete(self, request, pk):
        my_model = Lesson.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# API View for Words
class WordView(APIView):

    # Retrieve words, optionally filtered by a lesson ID
    def get(self, request, pk=None):
        # Check if a lesson ID is provided in the query parameters
        lesson_id = request.query_params.get('lesson_id', None)
        
        if pk is not None:
            # Get a specific word
            word = Word.objects.get(pk=pk)
            serializer = WordSerializer(word)
            return Response(serializer.data)
        elif lesson_id is not None:
            # Get words of a specific lesson
            words = Word.objects.filter(lesson__id=lesson_id)
            serializer = WordSerializer(words, many=True)
            return Response(serializer.data)
        else:
            # Get all words
            words = Word.objects.all()
            serializer = WordSerializer(words, many=True)
            return Response(serializer.data)

    # Create a new word
    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update an existing word
    def put(self, request, pk):
        word = Word.objects.get(pk=pk)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a word
    def delete(self, request, pk):
        word = Word.objects.get(pk=pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)