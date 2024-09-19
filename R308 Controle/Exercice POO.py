# ===
# Exercice 1
# ===

class Produit:
    def __init__(self,description,PU):
        self.description=description
        self.PU=PU

    def valeurStock(self,qte):
        Prix=self.PU
        return Prix*qte

# ====
# Exercice 2
# ===

class Armoire:
    def __init__(self):
        self.prod=[]
    
    def ajouter(self,refProduit,qte):
        res=[refProduit,qte]
        if len(self.prod)==0:
            self.prod.append(res)
        else:
            flag=0                                                  #flag sert à savoir si l'élément a déjà été ajouté
            for elt in self.prod:
                if elt[0].description==refProduit.description:      #comparaison pour savoir s'il est déjà dans l'armoire
                    elt[1]=elt[1]+qte
                    flag=1
            if flag==0:
                self.prod.append(res)
        print(self.prod)

    def valeur(self):
        tot=0
        for elt in self.prod:                                       #pour chaque éléments présents dans l'armoire, on rappelle la méthode valeurStock
            res=elt[0].valeurStock(elt[1])
            tot=tot+res
        return tot


# ===
# Exercice 3
# ===

def tester():                                                       #fonction qui essaie les différentes méthodes plus haut
    Mannequin=Produit("mannequin",14)
    print("Valeur de 2 mannequins :",Mannequin.valeurStock(2))
    Armoire1=Armoire()
    Armoire1.ajouter(Mannequin,2)
    print("Ajout de 2 mannequins à l'armoire")

    PC=Produit("PC",150)
    Armoire1.ajouter(PC,7)
    print("Ajout de 7 PC de 150€ chacun à l'armoire")
    Armoire1.ajouter(Mannequin,3)
    print("Ajout de 3 mannequins de plus")

    print("Valeur totale de l'armoire :" ,Armoire1.valeur())

# ===
# Exercice 4
# ===

class Vrac(Produit):                                                #Vrac hérite de Produit
    def __init__(self,description,PU,unite):
        super().__init__(description,PU)
        self.unite=unite

    def valeurStock(self,qte):                                      #on redéfinit valeurStock pour les Vrac
        Prix=self.PU
        res=(Prix*qte)/self.unite                                   #produit en croix
        return res

# ===
# Exercice 5
# ===

def tester_fin():
    Mannequin=Produit("mannequin",14)
    print("Valeur de 2 mannequins :",Mannequin.valeurStock(2))
    Armoire1=Armoire()
    Armoire1.ajouter(Mannequin,2)
    print("Ajout de 2 mannequins à l'armoire")

    PC=Produit("PC",150)
    Armoire1.ajouter(PC,7)
    print("Ajout de 7 PC de 150€ chacun à l'armoire")
    Armoire1.ajouter(Mannequin,3)
    print("Ajout de 3 mannequins de plus")

    Farine=Vrac("Farine",15,5)
    Armoire1.ajouter(Farine,2)

    Farine.valeurStock(2)

    print("Valeur totale de l'armoire :" ,Armoire1.valeur())

tester_fin()