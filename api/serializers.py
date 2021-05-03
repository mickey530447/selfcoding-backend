from rest_framework import serializers
from api.models import User, Problem, SolveStatus, Topic, Challenge, Class,Enrolment, Participant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

        extra_kwargs = {'password': {
            'write_only': True,
            'required' : True
        }}
    
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

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

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('__all__')