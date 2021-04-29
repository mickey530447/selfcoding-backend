from django.shortcuts import render,HttpResponse
from api.models import User, Problem, SolveStatus, Topic, Challenge, Class,Enrolment
from .serializers import UserSerializer, ProblemSerializer, SolveStatusSerializer, TopicSerializer, ChallengeSerializer, ClassSerializer, EnrolmentSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProblemViewSet(viewsets.ModelViewSet):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()

class SolveStatusViewSet(viewsets.ModelViewSet):
    serializer_class = SolveStatusSerializer
    queryset = SolveStatus.objects.all()

class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

class ChallengeViewSet(viewsets.ModelViewSet):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()

class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

class EnrolmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrolmentSerializer
    queryset = Enrolment.objects.all()

