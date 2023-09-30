from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, aro, peso, precio, marca ,costoDespachoBase):
        super().__init__(costoDespachoBase)
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def get_aro(self):
        return self.__aro
    def set_aro(self, aro):
        self.__aro = aro

    def get_peso(self):
        return self.__peso
    def set_peso(self, peso):
        self.__peso = peso

    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio

    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca


    def costoPorKg(self):
        return 400

    def __str__(self):
        cadena = f'Aro: {self.__aro}\n'
        cadena += f'Peso: {self.__peso} kg\n'
        cadena += f'Precio: ${self.__precio}\n'
        cadena += f'Marca: {self.__marca}\n'
        return cadena