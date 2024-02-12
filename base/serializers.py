from rest_framework import serializers
from .models import Lesson
from .models import Word # Import the models to be serialized

"""
    A serializer for the Lesson model that converts instances of Lesson
    to and from JSON format. It includes all fields of the Lesson model.
    
    ModelSerializer is used because it automatically generates a set
    of fields and default implementations for the create() and update()
    methods based on the model.
"""
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


"""
    A serializer for the Word model similar to LessonSerializer. It handles
    conversion of Word instances to JSON format and vice versa, including
    all fields of the Word model.
    
    By using ModelSerializer, we leverage Django REST Framework's capabilities
    to simplify data serialization tasks, making it easier to perform CRUD
    operations via the API.
"""
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
