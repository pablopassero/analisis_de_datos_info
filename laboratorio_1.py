import json

class Venta:
    def __init__(self, id_venta, fecha, cliente, productos, cantidad_total, precio_total, vendedor, hora=None):
        self.__id_venta = id_venta
        self.__fecha = fecha   
        self.__cliente = cliente
        self.__productos = productos
        self.__cantidad_total = self.validar_cantidad_total(cantidad_total)
        self.__precio_total = self.validar_precio_total(precio_total)
        self.__vendedor = vendedor
        self.__hora = hora

    @property 
    def id_venta(self):
        return self.__id_venta

    @property 
    def cliente(self):
        return self.__cliente.capitalize()

    @property 
    def fecha(self):
        return self.__fecha

    @property 
    def productos(self):
        return self.__productos

    @property 
    def cantidad_total(self):
        return self.__cantidad_total
    
    @property 
    def precio_total(self):
        return self.__precio_total
    
    @property 
    def vendedor(self):
        return self.__vendedor.capitalize()
    
    @property 
    def hora(self):
        return self.__hora

    @precio_total.setter
    def precio_total(self, nuevo_precio_total):
        self.__precio_total = self.validar_precio_total(nuevo_precio_total)

    @cantidad_total.setter
    def cantidad_total(self, nueva_cantidad_total):
        self.__cantidad_total = self.validar_cantidad_total(nueva_cantidad_total)

    def validar_precio_total(self, precio_total):
        try:
            if precio_total is None:
                raise ValueError('El precio no puede ser None.')
            precio_num = float(precio_total)
            if precio_num < 0:
                raise ValueError('El precio debe ser un número positivo.')
            return precio_num
        except ValueError as ve:
            raise ValueError(f'Error en precio_total: {ve}')
        except TypeError:
            raise ValueError('El precio debe ser un número.')

    def validar_cantidad_total(self, cantidad_total):
        try:
            if cantidad_total is None:
                raise ValueError('La cantidad no puede ser None.')
            cantidad_num = int(cantidad_total)
            if cantidad_num < 0:
                raise ValueError('La cantidad debe ser un número entero positivo.')
            return cantidad_num
        except ValueError as ve:
            raise ValueError(f'Error en cantidad_total: {ve}')
        except TypeError:
            raise ValueError('La cantidad debe ser un número entero.')

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "fecha": self.fecha,
            "cliente": self.cliente,
            "productos": self.productos,
            "cantidad_total": self.cantidad_total,
            "precio_total": self.precio_total,
            "vendedor": self.vendedor,
            "hora": self.hora,
        }

    def __str__(self):
        return f"La venta: {self.id_venta} ha sido realizada con éxito por el vendedor {self.vendedor} a las {self.hora} con fecha {self.fecha} por un total de {self.precio_total}"

class VentaOnline(Venta):
    def __init__(self, id_venta, fecha, cliente, productos, cantidad_total, precio_total, vendedor, metodo_pago, estado_envio, hora=None):
        super().__init__(id_venta, fecha, cliente, productos, cantidad_total, precio_total, vendedor, hora)
        self.__metodo_pago = self.validar_metodo_pago(metodo_pago)
        self.__estado_envio = self.validar_estado_envio(estado_envio)

    @property
    def metodo_pago(self):
        return self.__metodo_pago

    @metodo_pago.setter
    def metodo_pago(self, nuevo_metodo_pago):
        self.__metodo_pago = self.validar_metodo_pago(nuevo_metodo_pago)

    @property
    def estado_envio(self):
        return self.__estado_envio

    @estado_envio.setter
    def estado_envio(self, nuevo_estado_envio):
        self.__estado_envio = self.validar_estado_envio(nuevo_estado_envio)

    def validar_metodo_pago(self, metodo_pago):
        metodos_validos = ['tarjeta', 'mercado pago', 'transferencia']
        if metodo_pago not in metodos_validos:
            raise ValueError(f'Método de pago inválido. Los métodos válidos son: {", ".join(metodos_validos)}.')
        return metodo_pago

    def validar_estado_envio(self, estado_envio):
        estados_validos = ['pendiente', 'enviado', 'entregado']
        if estado_envio not in estados_validos:
            raise ValueError(f'Estado de envío inválido. Los estados válidos son: {", ".join(estados_validos)}.')
        return estado_envio

    def to_dict(self):
        data = super().to_dict()
        data['metodo_pago'] = self.metodo_pago
        data['estado_envio'] = self.estado_envio
        return data

    def __str__(self):
        return f'{super().__str__()} - Método de pago utilizado: {self.metodo_pago}, Estado del envío: {self.estado_envio}'

class VentaLocal(Venta):
    def __init__(self, id_venta, fecha, cliente, productos, cantidad_total, precio_total, vendedor, ubicacion_tienda, tipo_pago, hora=None):
        super().__init__(id_venta, fecha, cliente, productos, cantidad_total, precio_total, vendedor, hora)
        self.__ubicacion_tienda = self.validar_ubicacion_tienda(ubicacion_tienda)
        self.__tipo_pago = self.validar_tipo_pago(tipo_pago)

    @property
    def ubicacion_tienda(self):
        return self.__ubicacion_tienda

    @ubicacion_tienda.setter
    def ubicacion_tienda(self, nueva_ubicacion_tienda):
        self.__ubicacion_tienda = self.validar_ubicacion_tienda(nueva_ubicacion_tienda)

    @property
    def tipo_pago(self):
        return self.__tipo_pago

    @tipo_pago.setter
    def tipo_pago(self, nuevo_tipo_pago):
        self.__tipo_pago = self.validar_tipo_pago(nuevo_tipo_pago)

    def validar_ubicacion_tienda(self, ubicacion_tienda):
        if not isinstance(ubicacion_tienda, str) or not ubicacion_tienda.strip():
            raise ValueError('La ubicación de la tienda debe ser una cadena no vacía.')
        return ubicacion_tienda.strip()

    def validar_tipo_pago(self, tipo_pago):
        tipos_validos = ['efectivo', 'tarjeta', 'transferencia']
        if tipo_pago not in tipos_validos:
            raise ValueError(f'Tipo de pago inválido. Los tipos válidos son: {", ".join(tipos_validos)}.')
        return tipo_pago

    def to_dict(self):
        data = super().to_dict()
        data['ubicacion_tienda'] = self.ubicacion_tienda
        data['tipo_pago'] = self.tipo_pago
        return data

    def __str__(self):
        return f'{super().__str__()} - Ubicación de la tienda: {self.ubicacion_tienda}, Tipo de pago: {self.tipo_pago}'

class GestionVentas:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file: 
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos
        
    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_venta(self, venta):
        try:
            datos = self.leer_datos()
            id_venta = venta.id_venta
            if not str(id_venta) in datos.keys():
                datos[id_venta] = venta.to_dict()
                self.guardar_datos(datos)
                print(f"Venta {id_venta} creada correctamente.")
            else:
                print(f"Ya existe una venta con ID '{id_venta}'.")
        except ValueError as ve:
            print(f'Error en los datos de la venta: {ve}')
        except IOError as ioe:
            print(f'Error de IO al crear venta: {ioe}')
        except Exception as error:
            print(f'Error inesperado al crear venta: {error}')    

    def leer_venta(self, id_venta):
        try:
            datos = self.leer_datos()
            if str(id_venta) in datos:
                venta_data = datos[str(id_venta)]
                if 'metodo_pago' in venta_data and 'estado_envio' in venta_data:
                    venta = VentaOnline(**venta_data)
                elif 'ubicacion_tienda' in venta_data and 'tipo_pago' in venta_data:
                    venta = VentaLocal(**venta_data)
                else:
                    venta = Venta(**venta_data)
                print(f'Venta encontrada con ID {id_venta}:')
                print(venta)
            else:
                print(f'No se encontró una venta con ID {id_venta}.')
        except Exception as e:
            print(f'Error al leer venta: {e}')

    def actualizar_venta(self, id_venta, nuevo_precio_total, nueva_cantidad_total, nuevos_productos):
        try:
            datos = self.leer_datos()
            if str(id_venta) in datos:
                datos[str(id_venta)]['precio_total'] = nuevo_precio_total
                datos[str(id_venta)]['cantidad_total'] = nueva_cantidad_total
                datos[str(id_venta)]['productos'] = nuevos_productos
                self.guardar_datos(datos)
                print(f'Datos actualizados para la venta ID: {id_venta}')
            else:
                print(f'No se encontró una venta con ID: {id_venta}')
        except Exception as e:
            print(f'Error al actualizar la venta: {e}')      

    def eliminar_venta(self, id_venta):
        try:
            datos = self.leer_datos()
            if str(id_venta) in datos.keys():
                del datos[str(id_venta)]
                self.guardar_datos(datos)
                print(f'Venta ID: {id_venta} eliminada correctamente')
            else:
                print(f'No se encontró una venta con ID: {id_venta}')
        except Exception as e:
            print(f'Error al eliminar la venta: {e}')

    def mostrar_todas_las_ventas(self):
        try:
            datos = self.leer_datos()
            if datos:
                print('=============== Listado completo de Ventas ==============')
                for venta_id, venta_data in datos.items():
                    print(f"ID Venta: {venta_id}")
                    print(f"  Cliente: {venta_data['cliente']}")
                    print(f"  Productos: {venta_data['productos']}")
                    print(f"  Cantidad Total: {venta_data['cantidad_total']}")
                    print(f"  Precio Total: {venta_data['precio_total']}")
                    if 'metodo_pago' in venta_data:
                        print(f"  Método de Pago: {venta_data['metodo_pago']}")
                    if 'estado_envio' in venta_data:
                        print(f"  Estado de Envío: {venta_data['estado_envio']}")
                    if 'ubicacion_tienda' in venta_data:
                        print(f"  Ubicación de la Tienda: {venta_data['ubicacion_tienda']}")
                    if 'tipo_pago' in venta_data:
                        print(f"  Tipo de Pago: {venta_data['tipo_pago']}")
                    print('---------------------------------------------------------')
                print('=========================================================')
            else:
                print('No hay ventas registradas.')
        except Exception as e:
            print(f'Error al mostrar todas las ventas: {e}')