from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


class CustomAuthTokenSerializer(AuthTokenSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs['user']
        if not user.is_active:
            raise serializers.ValidationError("User is not active to obtain the token")
        if user.is_suspended:
            raise serializers.ValidationError("Your account has been suspended")

        if user.is_locked:
            raise serializers.ValidationError("Your account has been Locked, Contact Support")
        return attrs

    def create(self, validated_data): pass
    def update(self, instance, validated_data): pass
