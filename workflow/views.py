from django.http import HttpResponseRedirect
from django.shortcuts import render
from workflow.models import Board
from django.contrib.auth.models import User
from addProject.models import Project, ProjectUser
from workflow.library.SqWorkflow import get_status
from django.utils import timezone


def board_basic(request):
    cards = Board.objects.values('id', 'title', 'position')
    print("cards ", cards)
    print("request.user.id = ", request.user.id)

    context = {
        'cards': cards,
    }
    return render(request, 'user/workflow/board.html', context)


def add_issue(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        project = Project.objects.get(project_name="Projekt Adriana")

        if len(request.POST['iname']) > 3:
            Board.objects.create(
                position=1,
                id_user=None,
                id_creator=user,
                id_project=project,
                title=request.POST['iname'],
                # creation_time=datetime.now(), from django.utils import timezone
                # modification_timee=datetime.now()).save()
                creation_time=timezone.now(),
                modification_timee=timezone.now()).save()
        back = request.POST.get('back', '/workflow')
        return HttpResponseRedirect(back)
    back = request.POST.get('back', '/workflow')
    return HttpResponseRedirect(back, )


def issue_details(request):
    if request.is_ajax():
        issue_id = request.GET.get('issue-id', None)
        details = Board.objects.get(pk=issue_id)
        creator = User.objects.values('first_name', 'last_name').filter(pk=details.id_creator.id)[0]
        project = Project.objects.get(project_name="Projekt Adriana")

        project_user = ProjectUser.objects.values('uzytkownik_id').filter(nazwa_projektu=project)
        users = []
        for pro_user in project_user:
            u = User.objects.values_list('id', 'username').filter(pk=pro_user['uzytkownik_id'])[0]
            users.append({'id': u[0], 'name': u[1]})

        priorities = ['Sredni', 'Wysoki']

        status = get_status(details.position)
        print("status ", status)

        print("to jest ot ", users)

        context = {
            'details': details,
            'creator': creator,
            'users': users,
            'issue_id': issue_id,
            'priorities': priorities,
            'status': status,
        }

        return render(request, 'user/workflow/issue_details.html', context)
    back = request.POST.get('back', '/workflow')
    return HttpResponseRedirect(back)


def issue_edit(request):
    if request.method == 'POST':
        issue = Board.objects.get(pk=request.POST['issue_id'])
        issue.title = request.POST['title']
        issue.id_user = User.objects.get(pk=request.POST['user'])
        issue.priority = request.POST['priority']
        issue.description = request.POST['description']
        issue.modification_timee = timezone.now()
        issue.save()

        # Board.objects.filter(pk=request.POST['issue_id']).update(id_creator=User.objects.get(id=request.POST['user']))

        print(request.POST)

    back = request.POST.get('back', '/workflow')
    return HttpResponseRedirect(back)
