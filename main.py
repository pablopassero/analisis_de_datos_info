import os
import platform

from laboratorio_1 import (
    Venta,
    VentaOnline,
    VentaLocal,
    GestionVentas
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú de Gestión de Ventas ==========")
    print('1. Agregar Venta Online')
    print('2. Agregar Venta Local')
    print('3. Actualizar Venta')
    print('4. Eliminar Venta')
    print('5. Mostrar todas las Ventas')

def agregar_venta(gestion, tipo_venta):
    try:
        id_venta = input('Ingrese número de venta: ')
        fecha = input('Ingrese fecha de venta en formato dd/mm/aaaa: ')
        cliente = input('Ingrese nombre de cliente o usuario: ')
        productos = input('Ingrese producto/s vendido/s: ')
        cantidad_total = int(input('Ingrese cantidad total de artículos: '))
        precio_total = float(input('Ingrese el precio total: '))
        vendedor = input('Ingrese nombre de vendedor/a: ')
        hora = input('Ingrese hora de venta (opcional, presione Enter para omitir): ')

        if tipo_venta == '1':  # Venta Online
            metodo_pago = input('Ingrese método de pago: ')
            estado_envio = input('Ingrese estado de envío: ')
            venta = VentaOnline(id_venta, fecha, cliente, productos, cantidad_total, precio_total, vendedor, metodo_pago, estado_envio, hora)
        elif tipo_venta == '2':  # Venta Local
            ubicacion_tienda = input('Ingrese ubicación de la tienda: ')
            tipo_pago = input('Ingrese tipo de pago: ')
            venta = VentaLocal(id_venta, fecha, cliente, productos, cantidad_total, precio_total, vendedor, ubicacion_tienda, tipo_pago, hora)
        else:
            print('Tipo de venta no válido.')
            return

        gestion.crear_venta(venta)

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_venta_por_ID(gestion):
    id_venta = input('Ingrese el ID de la venta a buscar: ')
    gestion.leer_venta(id_venta)
    input('Presione enter para continuar...')

def actualizar_venta_por_ID(gestion):
    try:
        id_venta = input('Ingrese el ID de la venta para actualizar los datos: ')
        nuevo_precio_total = float(input('Ingrese el nuevo precio total: '))
        nueva_cantidad_total = int(input('Ingrese la nueva cantidad total: '))
        nuevos_productos = input('Ingrese los nuevos productos vendidos: ')
        gestion.actualizar_venta(id_venta, nuevo_precio_total, nueva_cantidad_total, nuevos_productos)
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')
    input('Presione enter para continuar...')

def eliminar_venta_por_ID(gestion):
    try:
        id_venta = input('Ingrese el ID de la venta a eliminar: ')
        gestion.eliminar_venta(id_venta)
    except Exception as e:
        print(f'Error al eliminar la venta: {e}')
    input('Presione enter para continuar...')

def mostrar_todas_las_ventas(gestion):
    gestion.mostrar_todas_las_ventas()
    input('Presione enter para continuar...')

if __name__ == "__main__":
    archivo_ventas = 'ventas_db.json'
    gestion_ventas = GestionVentas(archivo_ventas)

    while True:
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_venta(gestion_ventas, opcion)
        elif opcion == '3':
            actualizar_venta_por_ID(gestion_ventas)
        elif opcion == '4':
            eliminar_venta_por_ID(gestion_ventas)
        elif opcion == '5':
            mostrar_todas_las_ventas(gestion_ventas)
        elif opcion == '6':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-6)')
