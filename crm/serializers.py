from rest_framework import serializers
from django.contrib.auth.models import User






class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate(self, attrs):
        # Ensure that username, email, password, and confirmation are provided
        if "username" not in attrs:
            raise serializers.ValidationError({
                "username": "Username not provided"
            })
        if "email" not in attrs:
            raise serializers.ValidationError({
                "email": "Email not provided"
            })
        if "password" not in attrs:
            raise serializers.ValidationError({
                "password": "Password not provided"
            })

        # Ensure that username and email are not already taken
        if len(User.objects.filter(email=attrs["email"])) > 0:
            raise serializers.ValidationError({
                "email": "Email already taken"
            })
        if len(User.objects.filter(username=attrs["username"])) > 0:
            raise serializers.ValidationError({
                "username": "Username already taken"
            })

        return attrs


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"]
        )

        # Must use set_password method to hash password
        user.set_password(validated_data["password"])

        user.save()
        return user


