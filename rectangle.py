        
class Rectangle():
    def __init__(self,number,langeur,largeur,perimetre,air):
        self.number = number
        self.langeur = langeur
        self.largeur = largeur 
        self.perimetre = perimetre
        self.air = air


    def info(self):
        print("le rectangle {}, a une langeur de {} et une l'argeur de {} et un perimetre de {} et un air de {}".format(self.number,self.langeur,self.largeur,self.perimetre, self.air))








class Rectangle():
    def __init__(self):
        self.number = 1
        self.langeur = 12
        self.largeur = 53 
        self.perimetre = 130
        self.air = 636


    def info(self):
        print("le rectangle {}, a une langeur de {} et une l'argeur de {} et un perimetre de {} et un air de {}".format(self.number,self.langeur,self.largeur,self.perimetre, self.air))

obj = Rectangle()
obj.info()
