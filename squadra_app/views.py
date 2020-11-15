from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import TekstForm
from uploadapp.models import File
from django.core.files.storage import Storage
from squadra.our_library.file_storage_system import MyStorage

S = Storage
M = MyStorage(S)


# Widok wyświetla edytor tekstu przy pomocy formularza
# Instalacja ckeditor jest tu (tylko instalacja): https://django-ckeditor.readthedocs.io/en/latest/
# Można zmieniać dowolnie wygląd edytora, ale informacji o tym trzeba szukać w dokumentacji
# https://ckeditor.com/docs/ckeditor4/latest/guide/index.html
def app_page(request):
    # print(M.open("urls.py"))
    M.basedir()
    pliki, katalogi = M.listdir()
    # cdir = ''
    # print(pliki)
    # print(katalogi)
    # M.close()
    form = TekstForm(request.POST)
    context = {
        'form': form,
        'pliki': pliki,
        'katalogi': katalogi,
    }
    # if form.is_valid():
    #    form.save(request)
    #    return redirect('app_page')

    return render(request, 'squadra_app/app_page.html', context)


# Widok chwyta GET wysłane ze stony app_page.html za pomocą ajax.
# Zapisuje tekst znajdujący się w edytorze w otwartym pliku
# Jeśli udało się cokolwiek pobrać to widok odsyła z powrotem JSONa z "true".
def ajax_html_text(request):
    html_text = request.GET.get('text', None)
    len_file = M._save(html_text)
    # d = open("pliki/test_ajax.html", "w+")
    # d.write(html_text)
    # File.title = "test_ajax.html"
    # File.file = d
    # d.close()
    data = {
        'is_taken': len_file > 0
    }
    print(M.get_path())
    return JsonResponse(data)


# Widok ajax, który odpowiada za wyświetlanie plików znajdujących się w systemie plików
def ajax_storage_content(request):
    next_dict = request.GET.get('next_dict', None)
    direct = request.GET.get('direct', None)
    if direct == "up":
        M.updir(next_dict)
    elif direct == "down":
        M.downdir()
    else:
        print("Nieznany argument w ajax_storage_content")
    pliki, katalogi = M.listdir()
    context = {
        'pliki': pliki,
        'katalogi': katalogi,
    }
    print(M.get_path())
    return render(request, 'squadra_app/modal_body.html', context)


# Widok ajax który obsługuje otwieranie plików
def ajax_open_file(request):
    file_name = request.GET.get('open_file_name', None)
    M.updir(file_name)
    file = M._open()
    M.downdir()
    data = {"content": file.read_text()}
    return JsonResponse(data)


def ajax_crete_new_file(request):
    file_name = request.GET.get('new_file_name', None)
