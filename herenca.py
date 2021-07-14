class Persona:
    _siguiente = 0
    def __init__(self, nombre ="Invitado", activo=True):
        Persona._siguiente = Persona._siguiente + 1
        self.__codigo  = Persona._siguiente
        self.__nombre = __nombre_Mayuscula(nomb)
        self.activo = activo
#prvado con gion bajo
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,cod):
        self.__codigo = cod
    
    def siguiente(self):
        Persona._siguiente = Persona._siguiente + 1
        return Persona._siguiente

    def __nombre_Mayuscula(self, nomb):
        return self.nomb.upper()

    def mostrar_datos(self):
        return "Codigo:{} - Nombre:{} -Activo:{}".format(self.codigo, self.nombre, self.activo)

class Empleado(Persona):
    def __init__(self,)

per1 = Persona()
print(per1.codigo)
