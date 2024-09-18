from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Welcome

def welcome(request):
    users = Welcome.objects.all().values()

    template = loader.get_template('hello.html')
    context = {
        'users' : users,
    }
    return HttpResponse(template.render(context, request))