class Article:
    def __init__(self, reference,designation, prix_ht, stock):
        self.reference=reference
        self.designation=designation
        self.prix_ht=prix_ht
        self.stock=stock
    def valeur_stock(self) -> float:
        return self.stock*self.prix_ht
    def __str__(self):
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht} EUR HT"

