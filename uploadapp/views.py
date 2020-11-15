from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


# Funkcja wprowadza plik do formularza squadra_app/forms za pomocą POST.
# Jeśli ktoś kliknie "Submit" to wysyłany jest POST i wtedy wchodzi do tego pierwszego ifa i przekazuje plik
# jeśli nie to wyświetla normalną stronę.
# Formularz przekazuje dane do modelu bazy danych.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render(request, 'squadra_app/app_page.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request, 'uploadapp/upload.html', {'form': form})


