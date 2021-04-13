from rest_framework import serializers
from api.models import Role, User, Problem, SolveStatus, Topic, Challenge

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('__all__')