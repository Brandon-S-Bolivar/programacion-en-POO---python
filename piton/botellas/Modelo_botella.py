class Botella:
    def __init__(self,Material_1):
        self.Material=Material_1
        self.Capacidad=""
        self.Forma=""
        self.Diseño=""
        self.Grabados=""
        
    def Contener_liquido(self,capacidad_1):
        self.Capacidad=capacidad_1
        
    def forma_botella(self,Forma_1):
        self.Forma=Forma_1
        
    def diseño_botella(self,Diseño_1):
        self.Diseño=Diseño_1
    
    def Grabados_botella(self,Grabados_1):
        self.Grabados=Grabados_1
        
    def imprimir_info(self):
        print("----------------------------------------------------------------------------------------")   
        print(f"el material es: {self.Material} \nla capacidad es: {self.Capacidad} \nla forma es: {self.Forma} \nel diseño es: {self.Diseño} \ncon el grabado: {self.Grabados}")