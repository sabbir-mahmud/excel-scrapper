from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("file", views.ExcelFileViewSet, basename="Excel-File")
router.register("students", views.StudentViewSet, basename="students")

urlpatterns = [
    path('', include(router.urls)),
]
