from rest_framework import serializers
from api.models import User, Problem, SolveStatus, Topic, Challenge, Class,Enrolment

# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('__all__')

class SolveStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolveStatus
        fields = ('__all__')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('__all__')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('__all__')

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('__all__')

class EnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolment
        fields = ('__all__')