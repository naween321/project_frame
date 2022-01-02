from project.commons.serializers import DynamicFieldsModelSerializer
from ....models import File


class FileSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = File
        fields = 'uuid', 'created_at', 'updated_at', 'name', 'file'
        read_only_fields = ('uuid', 'created_at', 'updated_at', 'name')

    def create(self, validated_data):
        validated_data['name'] = validated_data['file'].name
        return super().create(validated_data)
