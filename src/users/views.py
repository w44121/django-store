from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegistrationSerializer, UserSerializer
from .models import User


class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SelfUserView(views.APIView):
    """
    Return current authorized user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class UserLogInView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'info': 'successfully login'}, status=status.HTTP_200_OK)
        return Response({'info': 'fail login'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(views.APIView):
    def get(self, request):
        logout(request)
        return Response({'info': 'successfully logout'}, status=status.HTTP_200_OK)
