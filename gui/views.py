# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    app_details = models.ApplicationModel.objects.get(id=1)
    context = { 'app_details' : app_details, }
    return render(request, 'gui/index.html', context)