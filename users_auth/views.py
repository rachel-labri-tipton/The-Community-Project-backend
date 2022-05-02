from datetime import datetime, timedelta
from rest_framework import generics
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


# class ProfileView(generics.GenericAPIView):

#     permission_classes = (IsAuthenticated, )

#     def get(self, request):
#         serialized_user = UserProfileSerializer(request.user)
#         return Response(serialized_user.data, status=status.HTTP_200_OK)


# class ProfileDetailView(APIView):

#     permission_classes = (IsAuthenticated, )

#     def get_user(self, pk):
#         """ retrives user from db by its pk(id) or responds 404 not found """

#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise NotFound()

#     def get(self, _request, pk):
#         user = self.get_user(pk=pk)
#         serialized_user = UserProfileSerializer(user)
#         return Response(serialized_user.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         # user_to_edit = UserProfileEditSerializer(request.user)
#         user_to_edit = self.get_user(pk=pk)
#         edited_profile = UserProfileEditSerializer(
#             user_to_edit, data=request.data)
#         if edited_profile.is_valid():
#             edited_profile.save()
#             return Response({'message': 'Accepted Edit'},
#                             status=status.HTTP_202_ACCEPTED)
#         return Response(edited_profile.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
