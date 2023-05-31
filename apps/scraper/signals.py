import pandas as pd
from django.db.models.signals import post_save

from .models import ExcelFile, Student


def scraper(sender, instance, created, **kwargs):
    if created:
        file = instance.excel.path
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            name = row['name'],
            roll = row['roll'],
            className = row['class']

            print(type(name))
            print(type(roll))
            print(type(className))

            Student.objects.create(
                name=name[0],
                roll=roll[0],
                className=className
            )


post_save.connect(scraper, sender=ExcelFile)
