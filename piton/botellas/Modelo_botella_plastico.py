from Modelo_botella import Botella

class Botella_plastico(Botella):
    def __init__(self,Material_2):
        super.__init__(Material_2)
        self.tinte=""
        self.Reutilizable=""
        self.cierre=""
        self.resistencia=""
        
    def Definir_datosr(self,tinte_1,reutilizable_1,cierre_1,resistencia_1):
        self.tinte=tinte_1
        self.Reutilizable=reutilizable_1
        self.cierre=cierre_1
        self.resistencia=resistencia_1
        
    def imprimir_info(self):
        super().imprimir_info()
        print(f"el tinte es: {self.tinte} \n es reutilizable: {self.Reutilizable} \n con un cierre: {self.cierre} \n resistencia de liquido: {self.resistencia}")