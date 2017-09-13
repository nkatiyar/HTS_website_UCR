import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from management.permissions import ReadOnly
from management.models import Sample, Project
from django.contrib.auth.models import User
from management.serializers import SampleSerializer, ProjectSerializer, UserSerializer
# from django.shortcuts import render
# from cerberus import Validator


@csrf_exempt
def test(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'status': 'fail'})
        data = json.loads(request.body.decode("utf-8"))
        res = JsonResponse({'status': 'success', 'name': data['name']})
        return res
    except KeyError:
        return JsonResponse({'status': 'fail', 'message': 'Missing field'})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error'})


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ReadOnly,)
