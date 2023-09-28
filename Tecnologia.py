class Tecnologia:
    def __init__(self, voltaje, precio, eficiencia, marca):
        self.__marca = marca
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_voltaje(self):
        return self.__voltaje

    def set_voltaje(self, voltaje):
        self.__voltaje = voltaje

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_eficiencia(self):
        return self.__eficiencia

    def set_eficiencia(self, eficiencia):
        self.__eficiencia = eficiencia

    def calcularDescuentos(self):
        if self.__eficiencia in ["A", "B"]:
            return 0.5
        elif self.__eficiencia in ["C", "D"]:
            return 0.3
        elif self.__eficiencia in ["E", "F"]:
            return 0.1
        else:
            return 0

    def __str__(self):
        cadena = f'Marca: {self.__marca} \n'
        cadena += f'Voltaje: {self.__voltaje} \n'
        cadena += f'Precio: ${self.__precio} \n'
        cadena += f'Eficiencia: {self.__eficiencia} \n'
        return cadena