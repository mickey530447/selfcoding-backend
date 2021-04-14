from django.shortcuts import render,HttpResponse
from api.models import Role, User, Problem, SolveStatus, Topic, Challenge
from .serializers import RoleSerializer, UserSerializer, ProblemSerializer, SolveStatusSerializer, TopicSerializer, ChallengeSerializer
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import APIView
# from rest_framework import generics
# from rest_framework import mixins
from rest_framework import viewsets
# from django.shortcuts import get_object_or_404


class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

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
    serializer_class = TopicSerializer
    queryset = Challenge.objects.all()



'''

class RoleList(generics.GenericAPIView, mixins.ListModelMixin,
                mixins.CreateModelMixin):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class RoleDetail(generics.GenericAPIView, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    lookup_field = 'id'

    def get(self,request, id):
        return self.retrieve(request, id=id)

    def put (self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)
'''

'''
    def get_object(self, id):
        try:
            return Role.objects.get(id = id)

        except Role.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        role = self.get_object(id)
        serialier = RoleSerializer(role)
        return Response(serialier.data)

    def put(self, request, id):
        role = self.get_object(id)
        serializer = RoleSerializer(role, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        role = self.get_object(id)
        role.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
'''

'''

@api_view(['GET','POST'])
def role_list(request):
    #get all roles
    if request.method == 'GET':
        roles = Role.objects.all()
        serialier = RoleSerializer(roles, many=True)
        return Response(serialier.data)
    
    elif request.method == 'POST':
        serialier = RoleSerializer(data = request.data)
        if serialier.is_valid():
            serialier.save()
            return Response(serialier.data, status = status.HTTP_201_CREATED)
        return Response(serialier.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def role_detail(request, pk):
    try:
        role = Role.objects.get(pk = pk)

    except Role.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RoleSerializer(role, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        role.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

'''


    