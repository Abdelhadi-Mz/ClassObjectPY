from contact import Contact
class Carnet:
    def __init__(self):
        self._contacts=[]
    def ajouter(self, contact: Contact):
        self._contacts.append(contact)
    def rechercher(self, fragment ):
        resultats=[]
        for a in self._contacts:
            if fragment.lower() in a.nom.lower():
                resultats.append(a)
        return resultats
        
    def afficher_tous(self):
        for a in self._contacts:
            print(a.nom, a.phone_number,a.email)

        
