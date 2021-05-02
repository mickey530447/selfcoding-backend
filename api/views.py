from django.shortcuts import render,HttpResponse
from api.models import User, Problem, SolveStatus, Topic, Challenge, Class,Enrolment
from .serializers import UserSerializer, ProblemSerializer, SolveStatusSerializer, TopicSerializer, ChallengeSerializer, ClassSerializer, EnrolmentSerializer
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view
from django.http.response import JsonResponse
import json
from rest_framework import status

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
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

class ChallengeViewSet(viewsets.ModelViewSet):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()

class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

class EnrolmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrolmentSerializer
    queryset = Enrolment.objects.all()

class LoginViewSet(viewsets.ViewSet):
    """Check email and password and return Authtoken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().as_view()(request = request._request)

@api_view(['POST'])

def get_user_by_email(request):
    receive_json_data = json.loads(request.body.decode('utf-8'))
    email = receive_json_data["email"]
    u = User.objects.filter(email=email)
    if not u:
        return JsonResponse({'check':'false'}, status = status.HTTP_200_OK)
    else:
        user = u.get()
        user_serialier = UserSerializer(user)
        return JsonResponse(user_serialier.data)