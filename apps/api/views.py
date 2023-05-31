from django.shortcuts import render
from rest_framework import viewsets

from apps.api.serializers import ExcelFileSerializer, StudentSerializer
from apps.scraper.models import ExcelFile, Student


class ExcelFileViewSet(viewsets.ModelViewSet):
    queryset = ExcelFile.objects.all()
    serializer_class = ExcelFileSerializer
    permission_classes = []


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = []
