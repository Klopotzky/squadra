from django.shortcuts import render

from .forms import ProjectForm
from .forms import new_project_form
from addProject.models import Project
from django.contrib.auth.models import User



def NewProjectView(request):
    print("New projekt111")
    form = new_project_form()
    if request.method == 'POST':
        form = new_project_form(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            obj = Project.objects.create(project_name=request.POST['project_name'])
            obj.project_creator = user
            obj.save()
            print('zapisane')

    context = {'form': form}
    return render(request, 'user/projects.html', context)


def ProjectAdd(request):
    name = request.user.username
    print('s', name)
    form = ProjectForm()
    if request.method == 'POST':
        print(request.POST)
        print(request.user.last_name)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'user/header.html', context)

def ProjectList(request):
    return render(request, 'user/projects.html')

# def addProject(request):
#     displayname = User.objects.all()
#     return render(request, 'addProject/createProject.html', {"displayusername": displayname})

