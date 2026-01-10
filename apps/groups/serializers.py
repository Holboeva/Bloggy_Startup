from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    members_count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ["id", "name", "description", "owner", "members_count", "is_private"]

    def get_members_count(self, obj):
        return obj.members.count()
