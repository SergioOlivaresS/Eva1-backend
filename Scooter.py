from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter(Tecnologia, Transporte):
    def __init__(self, marca, voltaje, aro, velocidad, peso, precio, eficiencia, costoDespachoBase):
        Tecnologia.__init__(self, voltaje, precio, eficiencia, marca)
        Transporte.__init__(self, costoDespachoBase)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso

    def get_aro(self):
        return self.__aro

    def set_aro(self, aro):
        self.__aro = aro

    def get_velocidad(self):
        return self.__velocidad

    def set_velocidad(self, velocidad):
        self.__velocidad = velocidad

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def costoPorKg(self):
        return 300

    def calcularDescuento(self):
        descuento_eficiencia = super().calcularDescuentos()
        return descuento_eficiencia

    def __str__(self):
        cadena = super().__str__()  
        cadena += f'Aro: {self.__aro}\n'
        cadena += f'Velocidad: {self.__velocidad} km/h\n'
        cadena += f'Peso: {self.__peso} kg\n'
        cadena += f'Costo de Despacho: ${self.calcularDespacho(self.__peso)}\n' 
        return cadena