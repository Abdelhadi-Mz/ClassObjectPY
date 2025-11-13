from article import Article
def main():
    article1=Article("1000298Dre","frait",10.99,54)
    article2=Article("1000298Dre","egg",10.99,54)
    article3=Article("1000298Dre","milk",10.99,54)
    print(article1)
    print(article2)
    print(article3)
    articles=[article1,article2,article3]
    total = sum(a.valeur_stock() for a in articles)
    print(f"Valeur d’inventaire : {total:.2f} €")
