from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_on_date = models.DateTimeField('date published')
    security_id = models.IntegerField(default=0)
