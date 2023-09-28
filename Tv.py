from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, voltaje, precio, eficiencia,marca, tamanio):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamanio = tamanio

    def get_tamanio(self):
        return self.__tamanio

    def set_tamanio(self, tamanio):
        self.__tamanio = tamanio

    def calcularDescuento(self):
        descuento_eficiencia = super().calcularDescuentos()
        return descuento_eficiencia

    def __str__(self):
        cadena = super().__str__()
        cadena += f'Tamaño: {self.__tamanio} pulgadas\n'
        return cadena