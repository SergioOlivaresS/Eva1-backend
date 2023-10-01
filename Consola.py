from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, nombreConsola, version, marca, voltaje, precio, eficiencia):
        super().__init__(voltaje, precio, eficiencia,marca)
        self.__nombreConsola = nombreConsola
        self.__version = version

    def get_nombreConsola(self):
        return self.__nombreConsola
    def set_nombreConsola(self, nombreConsola):
        self.__nombreConsola = nombreConsola

    def get_version(self):
        return self.__version
    def set_version(self, version):
        self.__version = version

    def calcularDescuento(self):
        descuento_eficiencia = super().calcularDescuentos()
        descuento_total = descuento_eficiencia
        if "lite" in self.__version:
            descuento_total += 0.05  
        return descuento_total

    def __str__(self):
        cadena = super().__str__()
        cadena += f'Nombre de la Consola: {self.__nombreConsola} \n' 
        cadena += f'Versión: {self.__version} \n'
        return cadena