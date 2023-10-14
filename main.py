class Araba ():
    def __init__ (self,model,marka):
        self.model=model
        self.marka=marka
    def arabaBilgi(self):
        print("araba modeli:",self.model,"\n","araba markası:",self.marka)
        return
        
      
class kamyon(Araba):
    def __init__(self,model,marka,renk):
        Araba.__init__(self,model,marka)
        self.renk=renk
       
k1=kamyon(2016,"nissan","gri")
k1.arabaBilgi()
   