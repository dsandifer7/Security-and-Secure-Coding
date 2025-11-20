from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Student
from .converter import StudentSerializer
# Create your views here.
@api_view(['GET'])
def getstudents(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students, many=True)
    return Response(serializer.data)

