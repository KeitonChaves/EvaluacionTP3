import globales
import random

def Precargar_Ventas():
    try:
        trabajadores = globales.leer_archivo_json('Empleados.json')
        ventas = globales.leer_archivo_json('Ventas.json')

        for i in range(10):
            trabajador = random.choice(trabajadores)["trabajador"]
            venta = random.randint(1500000,5000000)

            nueva_venta = {"trabajador": trabajador, "ventas": venta}
            ventas.append(nueva_venta)

        globales.guardar_archivo_json("Ventas.json", ventas)
        input("Precarga de Ventas completada, presione enter para continuar...")
    except:
        print("Error 404")
