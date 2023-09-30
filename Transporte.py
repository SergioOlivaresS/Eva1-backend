class Transporte:
    def __init__(self, costoDespachoBase):
        self.__costoDespachoBase = costoDespachoBase

    def calcularDespacho(self, peso):
        costo_despacho = self.__costoDespachoBase + (peso * self.costoPorKg())
        return costo_despacho
