import math
import globales

def venta_mas_alta():
    todas_las_ventas = globales.leer_archivo_json("Ventas.json")
    todos_los_trabajadores = globales.leer_archivo_json("Empleados.json")

    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['ventas'],reverse=True)

    for venta in ventas_ordenadas[:1]:
        nombre_trabajador = ""
        for trabajador in todos_los_trabajadores:
            if trabajador["trabajador"] == venta["trabajador"]:
                nombre_trabajador = trabajador["trabajador"]
        print(f"{nombre_trabajador} ${venta['ventas']}")
        input("Presione enter para continuar >>>>>")

def venta_mas_baja():
    todas_las_ventas = globales.leer_archivo_json("Ventas.json")
    todos_los_trabajadores = globales.leer_archivo_json("Empleados.json")

    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x['ventas'],reverse=False)

    for venta in ventas_ordenadas[:1]:
        nombre_trabajador = ""
        for trabajador in todos_los_trabajadores:
            if trabajador['trabajador'] == venta['trabajador']:
                nombre_trabajador = trabajador['trabajador']
        print(f"{nombre_trabajador} ${venta['ventas']}")
        input("Presione enter para continuar >>>>>")

def promedio_venta():
    todas_las_ventas = globales.leer_archivo_json("Ventas.json")
    suma = 0
    cantidad = 0
    for venta in todas_las_ventas[:1]:
        suma += venta["ventas"]
        cantidad += 1
    promedio = suma / cantidad
    print(promedio)
    input("Presione enter para continuar >>>>>")
    return promedio

def media_geometrica():
        todas_las_ventas = globales.leer_archivo_json("Ventas.json")
        suma = 0
        cantidad = 0
        for venta in todas_las_ventas:
            suma += int(math.log(venta["ventas"]))
            cantidad += 1
        media_g = int(math.exp(suma / cantidad))
        print(media_g)
        input("Presione enter para continuar >>>>>")
        return media_g