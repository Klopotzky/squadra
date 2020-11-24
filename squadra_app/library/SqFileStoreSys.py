from django.conf import settings
from pathlib import Path
from django.core.files.storage import Storage


# Klasa która służy do zarządzania naszym systemem plików. Jeśli chcesz dokonać jakiejkolwiek zmiany w systemie plików
# np. dodać plik, przesunąć plik, musisz to zrobić przez tą klasę.
class SqFileStoreSys(Storage):
    def __init__(self, option=None):
        self.file = None
        self.mypath = Path(settings.BASE_DIR) / "pliki"
        self.basepath = self.mypath
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS

    def open_file(self, filename):
        self.file = Path(str(settings.BASE_DIR) + "/" + str(filename))
        return self.file

    def save_file(self, text):
        return self.file.write_text(text)

    def new_file(self, filename):
        Path.touch(Path(str(settings.BASE_DIR) + "/" + str(filename)))

    def close(self):
        self.file.close()

    def path(self, name):
        return Path(self.mypath)

    def delete(self, name):
        ...

    def exists(self, name):
        return Path(name).exists()

    def listdir(self, path = ''):
        sciezka = Path(self.mypath / path)
        pliki = []
        katalogi = []
        for x in sciezka.iterdir():
            if x.is_file():
                pliki.append(x.name)
            elif x.is_dir():
                katalogi.append(x.name)
        return pliki, katalogi

    def size(self, name):
        return Path(name).stat().st_size

    # Funkcja powinna zwracać folder do ktorego tego pliki typu "name" trafiają
    # np. pliki z rozszerzeniem .py trafiają do jakiegos tam folderu
    def url(self, name):
        ...

    def updir(self, path):
        self.mypath = self.mypath / path

    def downdir(self):
        if self.mypath == self.basepath:
            pass
        else:
            self.mypath = self.mypath.parent

    def basedir(self):
        self.mypath = self.basepath

    def get_path(self):
        return self.mypath