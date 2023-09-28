class Transporte:
    CostoDespachoBase = 4000

    def calcularDespacho(self, peso):
        costo_despacho = self.CostoDespachoBase + (peso * self.costoPorKg())
        return costo_despacho

    def costoPorKg(self):
        pass

    def imprimirCaracteristicas(self):
        return f'Costo de Despacho: ${self.CostoDespachoBase}\n'