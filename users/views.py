from django.conf import settings
from django.shortcuts import render
from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import LoginSerializer, UserSerializer, RegisterSerializer
import jwt
# Create your views here.
User = get_user_model()


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully!"
        })


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied(detail='Unauthorized')

        if not user_to_login.check_password(password):
            raise PermissionDenied(detail='Unauthorized')

        expiry_time = datetime.now() + timedelta(days=7)
        token = jwt.encode({
            'sub': user_to_login.id,
            'exp': int(expiry_time.strftime('%s'))
        },
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        return Response({
            'token': token,
            'message': f'Welcome back {username}'
        }, status=status.HTTP_200_OK)
