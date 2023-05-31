import os
from uuid import uuid4

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.settings import BASE_DIR


def file_upload_helper(instance, filename):

    return f"files/{instance.uuid}/{filename}"


class ExcelFile(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    excel = models.FileField(upload_to=file_upload_helper)

    def __str__(self) -> str:
        return str(self.excel)


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=10)
    className = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ['-id']


@receiver(pre_save, sender=ExcelFile)
def set_excelfile_id(sender, instance, **kwargs):
    if not instance.uuid:
        instance.uuid = uuid4().hex
