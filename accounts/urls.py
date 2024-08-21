from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('userlist/', UserListView.as_view(), name='userlist'),
]
