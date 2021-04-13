from django.shortcuts import render,HttpResponse
from api.models import Role, User, Problem, SolveStatus, Topic, Challenge
from .serializers import RoleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def role_list(request):
    #get all roles
    if request.method == 'GET':
        roles = Role.objects.all()
        serialier = RoleSerializer(roles, many=True)
        return JsonResponse(serialier.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialier = RoleSerializer(data = data)
        if serialier.is_valid():
            serialier.save()
            return JsonResponse(serialier.data, status = 201)
        return JsonResponse(serialier.error, status = 400)

@csrf_exempt
def role_detail(request, pk):
    try:
        role = Role.objects.get(pk = pk)

    except Role.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RoleSerializer(role, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status = 400)
    elif request.method == 'DELETE':
        role.delete()
        return HttpResponse(status = 204)
    