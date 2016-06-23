from django.db import models

# Create your models here.


class UploadFile(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
