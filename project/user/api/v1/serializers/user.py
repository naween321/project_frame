from rest_framework import serializers

from django.contrib.auth import get_user_model

from project.commons.serializers import DynamicFieldsModelSerializer

User = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    username = serializers.UUIDField(format='hex', read_only=True)
    groups = serializers.SerializerMethodField()
    profile_picture = serializers.URLField(source='profile_picture_thumb')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'middle_name',
                  'last_name', 'is_active', 'is_suspended', 'time_zone', 'display_name', 'groups', 'last_activity',
                  'updated_at', 'profile_picture', 'contact_number')
        read_only_fields = 'username', 'display_name', 'email', 'last_activity', 'updated_at', \
                           'profile_picture'

    @staticmethod
    def validate_first_name(first_name):
        return first_name.title()

    @staticmethod
    def validate_middle_name(middle_name):
        if middle_name:
            return middle_name.title()
        return middle_name

    @staticmethod
    def validate_last_name(last_name):
        return last_name.title()

    @staticmethod
    def get_groups(obj):
        return obj.groups.all().values_list('name', flat=True)
