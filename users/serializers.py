from rest_framework import serializers

from users.models import User



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',
                  'last_name', 'email', 'profile_image')

    def create(self, data):
        user = User.objects.create_user(
            data['username'], password=data['password'], first_name=data['first_name'], last_name=data[
                'last_name'], email=data['email'], profile_image=data['profile_image']
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
