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
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from . import views
from .views import Lesson_view, WordView
from .views import update_password


# urls.py



urlpatterns = [
    path('',views.index),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('update_password/', update_password, name='update_password'),
    path('lessons/', Lesson_view.as_view(), name='lesson_list_create'),
    path('lessons/<int:pk>/', Lesson_view.as_view(), name='lesson_detail'),
    path('words/', WordView.as_view(), name='word_list_create'),
    path('words/<int:pk>/', WordView.as_view(), name='word_detail'),
    # The query parameter (lesson_id) is passed in the URL as follows:
    # /words/?lesson_id=<lesson_id>
]
