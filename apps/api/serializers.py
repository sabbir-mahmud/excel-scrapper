from rest_framework.serializers import ModelSerializer

from apps.scraper.models import ExcelFile, Student


class ExcelFileSerializer(ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
