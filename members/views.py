from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Members

def members(request):
    users = Members.objects.all().values()

    template = loader.get_template('Members.html')
    context = {
        'users' : users,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    user = Members.objects.get(id = id)
    template = loader.get_template('details.html')
    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Members.objects.all().order_by('name', '-age')
    template = loader.get_template('template.html')
    context = {
    'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def addnew(request):
    if request.method == "POST":
        nm = request.POST['Name']
        ph = request.POST['Age']
        obj = Members(Name=nm, Age=ag)
        obj.save()
        return HttpResponse("<h2>Record Added Successfully")
    return render(request, "myform.html")