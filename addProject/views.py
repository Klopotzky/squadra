from django.shortcuts import render

from .forms import ProjectForm
from .forms import new_project_form
from .models import displayusername
from django.contrib.auth.models import User
from django.contrib.auth.models import User, auth

def NewProject (request):
    name=request.user.username
    print('ssss',name)
    form = new_project_form()
    if request.method == 'POST':
        print(request.POST)
        print(request.user.last_name)
        form = new_project_form(request.POST)
        if form.is_valid():
           
            form.save()

    context = {'form':form}
    return render(request, 'addProject/projectDetail.html', context)



def ProjectAdd(request):

    name=request.user.username
    print('s',name)
    form = ProjectForm()
    if request.method == 'POST':
        print(request.POST)
        print(request.user.last_name)
        form = ProjectForm(request.POST)
        if form.is_valid():
           
            form.save()

    context = {'form':form}
    return render(request, 'addProject/projectCreateProject1_add.html', context)
    
    
# def addProject(request):
#     displayname = User.objects.all()
#     return render(request, 'addProject/createProject.html', {"displayusername": displayname})