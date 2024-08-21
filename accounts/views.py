from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import *
from django.contrib.auth import authenticate
from accounts.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


# Create your views here.

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            user_data = UserDetailsSerializer(user).data
            return Response(
                {"message": "Login Success", "data": user_data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"errorcode": 404, "error": "Email or Password is not Valid"},
                status=status.HTTP_404_NOT_FOUND,
            )


class UserListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        search_string = request.GET.get("first_name")
        user_data = User.objects.filter(first_name__istartswith=search_string)
        print(user_data.query)
        serializer = UsersListSerializer(user_data, many=True)
        context = {"data": serializer.data, "tital_count": user_data.count()}
        return Response(context, status=status.HTTP_200_OK)


class UserRegistrationView(APIView):
    #renderer_classes = [UserRenderer]
    #permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = serializer.data
        user_data.pop("password")
        user_data.update({"id": user.pk})
        return Response(
            {"msg": "Registration Successful", "data": user_data},
            status=status.HTTP_201_CREATED,
        )
