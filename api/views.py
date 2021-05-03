from django.shortcuts import render,HttpResponse
from api.models import User, Problem, SolveStatus, Topic, Challenge, Class,Enrolment, Participant
from .serializers import UserSerializer, ProblemSerializer, SolveStatusSerializer, TopicSerializer, ChallengeSerializer, ClassSerializer, EnrolmentSerializer, ParticipantSerializer
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view
from django.http.response import JsonResponse
import json
from rest_framework import status
import copy, requests, time

URL = f"https://api.jdoodle.com/v1/execute"
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
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

class ChallengeViewSet(viewsets.ModelViewSet):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()

class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

class EnrolmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrolmentSerializer
    queryset = Enrolment.objects.all()

class ParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()

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
        return JsonResponse(status = status.HTTP_401_UNAUTHORIZED)
    else:
        user = u.get()
        user_serialier = UserSerializer(user)
        return JsonResponse(user_serialier.data)

@api_view(['POST'])

def get_all_solved_status(request):
    receive_json_data = json.loads(request.body.decode('utf-8'))
    user_id = receive_json_data["id"]
    problist = Problem.objects.all()
    solveStt = SolveStatus.objects.all()
    temp = copy.copy(problist)
    for item in temp:
        check = solveStt.filter(problem=item.id,user=user_id)
        if check:
            item.solve = True

    serializer = ProblemSerializer(temp, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])

def get_topics_by_params(request):
    topics = Topic.objects.all()
    receive_json_data = json.loads(request.body.decode('utf-8'))


    try:
        user_id = receive_json_data["user"]
        topics = topics.filter(user = user_id)
    except:
        print("No param user")
    try:
        isVerified = receive_json_data["isVerified"]
        topics = topics.filter(isVerified = isVerified)
    except:
        print("No param isVerified")
    
    serializer = TopicSerializer(topics, many = True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['POST'])

def compile_code(request):
    receive_json_data = json.loads(request.body.decode('utf-8'))
    script = receive_json_data["script"]

    r = requests.get(url = URL, data = {'script' :script,'language': 'nodejs','versionIndex': '3','clientId': 'cd12de35bb91b50d95423b7f37bddde1','clientSecret':'e9521ce97ee8c077cd9152d03c952a2ed5364fdf9e038e25614282154ffb19b7'})

    data = r.json()
    return JsonResponse({'output': data['output'].strip()})

@api_view(['PUT'])

def modifyuserexp(request):
    receive_json_data = json.loads(request.body.decode('utf-8'))
    email = receive_json_data["email"]
    exp = receive_json_data["exp"]
    u = User.objects.get(email = email)
    u.exp = exp
    u.save()
    return JsonResponse({},status=status.HTTP_200_OK)

@api_view(['POST'])

def modifyVerifiedTopic(request):
    receive_json_data = json.loads(request.body.decode('utf-8'))
    topic_id = receive_json_data["topic_id"]
    isVerified = receive_json_data["isVerified"]
    topic = Topic.objects.get(id = topic_id)
    topic.isVerified = isVerified
    topic.save()
    return JsonResponse({},status = status.HTTP_200_OK)