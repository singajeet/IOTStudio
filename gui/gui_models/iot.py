from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique = True)
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    security_id = models.ForeignKey('SecurityIdModel', models.SET_NULL, blank = True, null = True)

class SecurityIdModel(models.Model):
    OBJECT_TYPES = (
        ('-1', 'None'),
        ('00', 'User'),
        ('01', 'Group'),
        ('02', 'Role'),
        ('03', 'Capability')
    )
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255, unique = True)
    type = models.CharField(max_length=2, choices=OBJECT_TYPES, default='-1')
    value = models.CharField(max_length=255)
    created_on_date = models.DateTimeField(auto_now_add = True, editable = False)
    modified_on_date = models.DateTimeField(auto_now = True, editable = False)
    
    def __str__(self):
        return self.name