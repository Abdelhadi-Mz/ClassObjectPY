class Contact:
    def __init__(self,nom,phone_number,email):
        self.nom=nom
        self.phone_number=phone_number
        self.email=email
    @property
    def initial(self):
        return self.nom[0].upper()
    