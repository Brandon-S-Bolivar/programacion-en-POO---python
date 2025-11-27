from Modelo_botella_plastico import *
from Modelo_botella_vidrio import Botella_vidrio


#-------------------------------------------------
Botella_plastico_1 = Botella_plastico("Plastico PET")
Botella_plastico_1.Definir_datos_plasti("blanco","no","rosca","fria/caliente","1000 ml","cilindrica","deportiva","coca-cola")



#-------------------------------------------------
Botella_vidrio_1 = Botella_vidrio("Vidrio reciclado")
Botella_vidrio_1.Definir_datos_vidrio("manual","bebidas","si","corcho","fria/caliente","750 ml","cilindrica","clasico","vino")

#-------------------------------------------------
Modelo_botella_1 = Botella("Aluminio")
Modelo_botella_1.Contener_liquido("500 ml")
Modelo_botella_1.forma_botella("cilindrica")
Modelo_botella_1.diseño_botella("moderno")
Modelo_botella_1.Grabados_botella("pepsi")

#---------------------imprimir----------------------------

Modelo_botella_1.imprimir_info()
Botella_plastico_1.imprimir_info()
Botella_vidrio_1.imprimir_info()