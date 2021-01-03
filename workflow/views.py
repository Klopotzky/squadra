from django.http import HttpResponseRedirect
from django.shortcuts import render
from workflow.models import Board, User, Project
import datetime


def board_basic(request):
    cards = Board.objects.values('id', 'title', 'position')

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
                creation_time=datetime.datetime.now(),
                modification_timee=datetime.datetime.now()).save()

        back = request.POST.get('back', '/workflow')
        return HttpResponseRedirect(back)
    back = request.POST.get('back', '/workflow')
    return HttpResponseRedirect(back, )


def issue_details(request):
    if request.is_ajax():
        issue_id = request.GET.get('issue-id', None)
        details = Board.objects.get(pk=issue_id)

        context = {
            'details': details,
        }

        return render(request, 'user/workflow/issue_details.html', context)
    back = request.POST.get('back', '/workflow')
    return HttpResponseRedirect(back)
