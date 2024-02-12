"""
URL configuration for french_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import necessary Django and third-party modules
from rest_framework_simplejwt.views import TokenObtainPairView # JWT token obtain pair view for login
from django.urls import path  # Function to define URL patterns
from . import views # Import views from the current application
from .views import Lesson_view, WordView  # Import specific class-based views
from .views import update_password # Import the password update view function


# Define URL patterns for the application
urlpatterns = [
    path('',views.index),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # URL for obtaining JWT tokens
    path('update_password/', update_password, name='update_password'),  # URL for updating user password
    
    # URLs for lesson-related operations
    path('lessons/', Lesson_view.as_view(), name='lesson_list_create'), # List all lessons or create a new lesson
    path('lessons/<int:pk>/', Lesson_view.as_view(), name='lesson_detail'), # Retrieve, update, or delete a specific lesson by ID

    # URLs for word-related operations
    path('words/', WordView.as_view(), name='word_list_create'), # List all words or create a new word
    path('words/<int:pk>/', WordView.as_view(), name='word_detail'), # Retrieve, update, or delete a specific word by ID
    # The query parameter (lesson_id) is passed in the URL as follows:
    # /words/?lesson_id=<lesson_id>
]

"""
Note on URL patterns:
- Function views are mapped directly to a URL pattern using the `path` function.
- Class-based views are referenced using the `.as_view()` method to instantiate the view.
- The `<int:pk>` syntax in some URL patterns captures an integer parameter (named 'pk' here, short for 'primary key') from the URL and passes it to the view.
"""