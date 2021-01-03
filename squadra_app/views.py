# TODO: możliwość usuwania plików

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import TekstForm, UploadFileForm
from squadra_app.models import Katalog, Pliki
from squadra_app.library.SqFileDb import SqFileDb
import os, zipfile, io

K = SqFileDb()


# Widok wyświetla edytor tekstu przy pomocy formularza
# Instalacja ckeditor jest tu (tylko instalacja): https://django-ckeditor.readthedocs.io/en/latest/
# Można zmieniać dowolnie wygląd edytora, ale informacji o tym trzeba szukać w dokumentacji
# https://ckeditor.com/docs/ckeditor4/latest/guide/index.html
def app_page(request):
    pliki, katalogi = K.listdir()

    form = TekstForm(request.POST)
    context = {
        'form': form,
        'pliki': pliki,
        'katalogi': katalogi,
    }

    return render(request, 'user/squadra_app/app_page.html', context)


# Zapisuje tekst znajdujący się w edytorze w otwartym pliku
# Jeśli udało się cokolwiek pobrać to widok odsyła z powrotem JSONa z "true".
def ajax_html_text(request):
    html_text = request.GET.get('text', None)
    len_file = K.save_file(html_text)
    data = {
        'is_taken': len_file > 0
    }
    return JsonResponse(data)


# Widok ajax, który odpowiada za wyświetlanie plików znajdujących się w systemie plików
def ajax_storage_content(request):
    if request.is_ajax():
        next_dict = request.GET.get('next_dict', None)
        direct = request.GET.get('direct', None)

        print("direct ", direct)
        print("request", request)
        print("next", next_dict)

        if direct == "up":
            K.updir(next_dict)
        elif direct == "down":
            K.downdir()
        else:
            print("Nieznany argument w ajax_storage_content")

    pliki, katalogi = K.listdir()

    # Dodatkowo stworzenie formularza do dodawania pliku
    form = UploadFileForm()

    context = {
        'pliki': pliki,
        'katalogi': katalogi,
        'form': form,
    }
    return render(request, 'user/squadra_app/storage.html', context)


# Widok ajax który obsługuje otwieranie plików
def ajax_open_file(request):
    filename = request.GET.get('open_file_name', None)
    file = K.open_file(filename)
    data = {"content": file.read_text()}
    return JsonResponse(data)


def new_file(request):
    if request.method == 'POST':
        kat = Katalog.objects.get(pk=K.get_dir().id)
        Pliki.objects.create(
            id_katalogu=kat,
            format=os.path.splitext(request.POST['fname'])[1],
            nazwa=request.POST['fname'],
            sciezka="pliki/" + request.POST['fname']).save()

        K.new_file(request.POST['fname'])

        data = {'is_create': True}

    else:
        data = {'is_create': False}
    return JsonResponse(data)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.FILES)
        if form.is_valid():
            kat = Katalog.objects.get(pk=K.get_dir().id)
            Pliki.objects.create(
                id_katalogu=kat,
                format=os.path.splitext(request.FILES['filename'].name)[1],
                nazwa=request.FILES['filename'].name,
                sciezka=request.FILES['filename']).save()

            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def new_dir(request):
    if request.method == 'POST':
        kat = Katalog.objects.get(pk=K.get_dir().id)
        Katalog.objects.create(
            id_kat_nad=kat,
            nazwa=request.POST['dname']).save()

        data = {'is_create': True}

    else:
        data = {'is_create': False}
    return JsonResponse(data)


def export_file(request):
    filenames = request.GET.getlist('export_fname', None)
    # zip, name = K.zip_files(filenames)

    in_memory = io.BytesIO()
    zip = zipfile.ZipFile(in_memory, "a")
    for file in filenames:
        with open("C:\\Users\\Adrian\\Desktop\\Studia\\Squadra materiały\\squadra 26.11\\squadra\\pliki\\" + file,
                  'rb') as f:
            data = f.read()
            print("data ", data)

        zip.writestr(file, data)
    print("zip ", zip.filelist)
    print("zip filename ", zip.filename)
    zip.close()
    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = "attachment; filename=two_files.zip"
    print("in memory ", in_memory)
    in_memory.seek(0)
    print("in memory seek ", in_memory.read())
    in_memory.seek(0)
    response.write(in_memory.read())

    return response
