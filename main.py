from Consola import Consola
from Tv import Tv
from Bicicleta import Bicicleta
from Scooter import Scooter


productos = []



def registrarTv():
    marca = input("Ingrese la marca del TV: ")
    voltaje = int(input("Ingrese el voltaje del TV: "))
    precio = float(input("Ingrese el precio del TV: "))
    eficiencia = input("Ingrese la eficiencia del TV (A/B/C/D/E/F): ")
    tamanio = float(input("Ingrese el tamaño del TV en pulgadas: "))
    tv = Tv(marca, voltaje, precio, eficiencia, tamanio)
    productos.append(tv)
    print("TV registrado exitosamente.")

def registrarConsola():
    nombreConsola = input("Ingrese el nombre de la Consola: ")
    version = input("Ingrese la versión de la Consola: ")
    marca = input("Ingrese la marca de la Consola: ")
    voltaje = int(input("Ingrese el voltaje de la Consola: "))
    precio = float(input("Ingrese el precio de la Consola: "))
    eficiencia = input("Ingrese la eficiencia de la Consola (A/B/C/D/E/F): ")
    consola = Consola(nombreConsola, version, marca, voltaje, precio, eficiencia)
    productos.append(consola)
    print("Consola registrada exitosamente.")


def registrarScooter():
    marca = input("Ingrese la marca del Scooter: ")
    voltaje = int(input("Ingrese el voltaje del Scooter: "))
    aro = float(input("Ingrese el aro del Scooter: "))
    velocidad = int(input("Ingrese la velocidad del Scooter en km/h: "))
    peso = float(input("Ingrese el peso del Scooter en kg: "))
    precio = float(input("Ingrese el precio del Scooter: "))
    eficiencia = input("Ingrese la eficiencia del Scooter (A/B/C/D/E/F): ")
    scooter = Scooter(marca, voltaje, aro, velocidad, peso, precio, eficiencia, 4000)
    productos.append(scooter)
    print("Scooter registrado exitosamente.")

def registrarbicicleta():
    aro = float(input("Ingrese el aro de la Bicicleta: "))
    peso = float(input("Ingrese el peso de la Bicicleta en kg: "))
    precio = float(input("Ingrese el precio de la Bicicleta: "))
    marca = input("Ingrese la marca de la Bicicleta: ")
    bicicleta = Bicicleta(aro, peso, precio, marca, 4000) 
    productos.append(bicicleta)
    print("Bicicleta registrada exitosamente.")


def cotizarTv():
    for producto in productos:
        if isinstance(producto, Tv):
            descuento = producto.calcularDescuentos()
            precio_descuento = producto.get_precio() * (1 - descuento)
            print(producto)
            print(f"Descuento Aplicado: {descuento * 100}%")
            print(f"Precio Total con Descuento: ${precio_descuento}")
        
def cotizarConsola():
    for producto in productos:
        if isinstance(producto, Consola):
            descuento = producto.calcularDescuento()
            precio_descuento = producto.get_precio() * (1 - descuento)
            print(producto)
            print(f"Descuento Aplicado: {descuento * 100}%")
            print(f"Precio Total con Descuento: ${precio_descuento}")


def menu():
    print("\nMenu SuperMercado:")
    print("1. Registrar TV")
    print("2. Registrar Consola")
    print("3. Registrar Scooter")
    print("4. Registrar Bicicleta")
    print("5. Cotizar TV")
    print("6. Cotizar Consola")
    print("7. Cotizar Scooter")
    print("8. Cotizar Bicicleta")
    print("9. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrarTv()

    elif opcion == "2":
        registrarConsola()

    elif opcion == "3":
        registrarScooter()

    elif opcion == "4":
        registrarbicicleta()

    elif opcion == "5":
        cotizarTv()

    elif opcion == "6":
        cotizarConsola()

    elif opcion == "7":
        pass
    elif opcion == "8":     
        pass
    elif opcion == "9":
        print("\nSaliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")





#def cotizarScooter():
#   for producto in productos:
#           if isinstance(producto, Scooter):
 #               descuento = producto.calcularDescuentos()
  #              costo_despacho = producto.calcularDespacho(producto.get_peso())
   #             precio_descuento = producto.get_precio() * (1 - descuento)
    #            precio_total = precio_descuento + costo_despacho
     #           print(producto)
      #          print(f"Descuento Aplicado: {descuento * 100}%")
       #         print(f"Costo de Despacho: ${costo_despacho}")
        #        print(f"Precio Total con Descuento y Despacho: ${precio_total}")

#def cotizarBicicleta():
#    for producto in productos:
 #           if isinstance(producto, Bicicleta):
  #              costo_despacho = producto.calcularDespacho(producto.get_peso())
   #             precio_total = producto.get_precio() + costo_despacho
    #            print(producto)
     #           print(f"Costo de Despacho: ${costo_despacho}")
      #          print(f"Precio Total con Despacho: ${precio_total}")
