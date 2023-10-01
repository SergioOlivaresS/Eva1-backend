from Consola import Consola
from Tv import Tv
from Bicicleta import Bicicleta
from Scooter import Scooter

productos = []

def validarNumero(mensaje):
    while True:
        try:
            valor = int(input(f'Ingrese {mensaje}: '))
            break
        except ValueError:
            print('Debe ingresar un número entero válido.')

    return valor

def validarFloat(mensaje):
    while True:
        try:
            valor = float(input(f'Ingrese {mensaje}'))
            break
        except ValueError:
            print('Debe ingresar un número flotante válido.')

    return valor

def registrarTv():
    print("Usted esta registrando una televisión\n")
    marca = input("Ingrese la marca del TV: ")
    voltaje = validarNumero("el voltaje del TV: ")
    precio = validarFloat("el precio del TV: ")
    eficiencia = input("Ingrese la eficiencia del TV (A/B/C/D/E/F): ").upper()
    tamanio = validarFloat("el tamaño del TV en pulgadas: ")
    tv = Tv(voltaje, precio, eficiencia,marca, tamanio)
    productos.append(tv)
    print("TV registrado exitosamente.")

def registrarConsola():
    nombreConsola = input("Ingrese el nombre de la Consola: ")
    version = input("Ingrese la versión de la Consola: ").lower()
    marca = input("Ingrese la marca de la Consola: ")
    voltaje = validarNumero("el voltaje de la Consola: ")
    precio = validarFloat("el precio de la Consola: ")
    eficiencia = input("Ingrese la eficiencia de la Consola (A/B/C/D/E/F): ").upper()
    consola = Consola(nombreConsola, version, marca, voltaje, precio, eficiencia)
    productos.append(consola)
    print("Consola registrada exitosamente.")

def registrarScooter():
    marca = input("Ingrese la marca del Scooter: ")
    voltaje = validarNumero("el voltaje del Scooter: ")
    aro = validarFloat("el aro del Scooter: ")
    velocidad = validarNumero("la velocidad del Scooter en km/h: ")
    peso = validarFloat("el peso del Scooter en kg: ")
    precio = validarFloat("el precio del Scooter: ")
    eficiencia = input("Ingrese la eficiencia del Scooter (A/B/C/D/E/F): ").upper()
    scooter = Scooter(marca, voltaje, aro, velocidad, peso, precio, eficiencia, 4000)
    productos.append(scooter)
    print("Scooter registrado exitosamente.")

def registrarBicicleta():
    aro = validarFloat("el aro de la Bicicleta: ")
    peso = validarFloat("el peso de la Bicicleta en kg: ")
    precio = validarFloat("el precio de la Bicicleta: ")
    marca = input("Ingrese la marca de la Bicicleta: ")
    bicicleta = Bicicleta(aro, peso, precio, marca, 4000)
    productos.append(bicicleta)
    print("Bicicleta registrada exitosamente.")


def cotizarTv():
    print("Esta cotizando televisiones\n")
    for producto in productos:
        if isinstance(producto, Tv):
            descuento = producto.calcularDescuentos()
            precio_descuento = producto.get_precio() * (1 - descuento)
            print(producto)
            print(f"Descuento Aplicado: {descuento * 100}%")
            print(f"Precio Final: ${precio_descuento}\n")
        
def cotizarConsola():
    for producto in productos:
        if isinstance(producto, Consola):
            descuento = producto.calcularDescuento()
            descuento_redondeado = round(descuento * 100, 2)
            precio_descuento = producto.get_precio() * (1 - descuento)
            print(producto)
            print(f"Descuento Aplicado: {descuento_redondeado}%")
            print(f"Precio Total con Descuento: ${precio_descuento}\n")


def cotizarScooter():
    print("Esta cotizando scooters\n")
    for producto in productos:
           if isinstance(producto, Scooter):
                descuento = producto.calcularDescuentos()
                costo_despacho = producto.calcularDespacho(producto.get_peso())
                precio_descuento = producto.get_precio() * (1 - descuento)
                precio_total = precio_descuento + costo_despacho
                print(producto)
                print(f"Descuento de: {descuento * 100}%")
                print(f"Costo de Despacho: ${costo_despacho}")
                print(f"Producto total con despacho: ${precio_total}\n")

def cotizarBicicleta():
    print("Esta cotizando bicicletas\n")
    for producto in productos:
            if isinstance(producto, Bicicleta):
                costo_despacho = producto.calcularDespacho(producto.get_peso())
                precio_total = producto.get_precio() + costo_despacho
                print(producto)
                print(f"Costo de Despacho: ${costo_despacho}")
                print(f"Precio total con despacho: ${precio_total}\n")


def menu_principal():
    print("\nBienvenido que desea realizar:\n")
    print("1. Registrar Productos")
    print("2. Cotizar Productos")
    print("3. Salir")

def menu_registrar():
    print("\nOpciones de Registro:")
    print("1. Registrar TV")
    print("2. Registrar Consola")
    print("3. Registrar Scooter")
    print("4. Registrar Bicicleta")
    print("5. Volver al Menú Principal")

def menu_cotizar():
    print("\nOpciones de Cotización:")
    print("1. Cotizar TV")
    print("2. Cotizar Consola")
    print("3. Cotizar Scooter")
    print("4. Cotizar Bicicleta")
    print("5. Volver al Menú Principal")

while True:
    menu_principal()
    opcion_principal = input("Seleccione una opción: ")

    if opcion_principal == "1":
        while True:
            menu_registrar()
            opcion_registrar = input("Seleccione una opción de registro: ")
            if opcion_registrar == "1":
                registrarTv()
            elif opcion_registrar == "2":
                registrarConsola()
            elif opcion_registrar == "3":
                registrarScooter()
            elif opcion_registrar == "4":
                registrarBicicleta()
            elif opcion_registrar == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    elif opcion_principal == "2":
        while True:
            menu_cotizar()
            opcion_cotizar = input("Seleccione una opción de cotización: ")
            if opcion_cotizar == "1":
                cotizarTv()
            elif opcion_cotizar == "2":
                cotizarConsola()
            elif opcion_cotizar == "3":
                cotizarScooter()
            elif opcion_cotizar == "4":
                cotizarBicicleta()
            elif opcion_cotizar == "5":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    elif opcion_principal == "3":
        print("\nSaliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")