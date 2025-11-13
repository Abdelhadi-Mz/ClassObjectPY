from datetime import datetime


class JournalTaches:
    def __enter__(self):
        self._f=open("journal.txt","a",encoding="utf-8")
        return self
    def enregistrer(self, tach: str):
        time=datetime.now().isoformat()
        self._f.write(f"{time}  {tach}\n")
    def __exit__(self, exc_type,exc,tb):
        self._f.close()