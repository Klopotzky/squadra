# Biblioteka, która służy do zarządzania plikami.
# Sama wpisuje odpowiednie dane do bazy i używa biblioteki SqFileStoreSys do fizycznego zarządzania plikami

from editor.models import Katalog, Pliki
from django.core.files.storage import Storage
from editor.library.SqFileStoreSys import SqFileStoreSys


class SqFileDb:
    def __init__(self):
        self.file = None
        try:
            self.mydir = Katalog.objects.get(pk=1)
            self.basepath = self.mydir
            S = Storage
            self.M = SqFileStoreSys(S)
        except Exception as e:
            try:
                Katalog.objects.create(nazwa="Glowny")
            except Exception as ex:
                print(ex)
            print(e)

    def open_file(self, filename):
        self.file = Pliki.objects.get(id_katalogu=self.mydir, nazwa=filename).sciezka
        return self.M.open_file(self.file)

    def save_file(self, text):
        return self.M.save_file(text)

    def new_file(self, filename):
        self.file = Pliki.objects.get(id_katalogu=self.mydir, nazwa=filename).sciezka
        self.M.new_file(self.file)

    def close(self):
        self.M.close()

    # def exists(self, name):
    #     return Path(name).exists()

    def listdir(self):
        K = Katalog.objects.values_list('nazwa', flat=True).filter(id_kat_nad=self.mydir)
        P = Pliki.objects.values_list('nazwa', flat=True).filter(id_katalogu=self.mydir)
        return P, K

    def updir(self, dir):
        self.mydir = Katalog.objects.get(nazwa=dir)

    def downdir(self):
        if self.mydir == self.basepath:
            pass
        else:
            self.mydir = self.mydir.id_kat_nad

    def basedir(self):
        self.mydir = self.basepath

    def get_dir(self):
        return self.mydir

    def zip_files(self, files):
        return self.M.zip_files(files)
