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




# Create your views here.



@api_view(['GET'])
def index(req):
    return Response("test")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        token['password'] = user.password
        # ...


        return token


class Lesson_view(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonSerializer(lesson)
            return Response(serializer.data)
        else:
            lessons = Lesson.objects.all()
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        # usr =request.user
        # print(usr)
        serializer = LessonSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Lesson.objects.get(pk=pk)
        serializer = LessonSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Lesson.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class WordView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            word = Word.objects.get(pk=pk)
            serializer = WordSerializer(word)
            return Response(serializer.data)
        else:
            words = Word.objects.all()
            serializer = WordSerializer(words, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        word = Word.objects.get(pk=pk)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        word = Word.objects.get(pk=pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)