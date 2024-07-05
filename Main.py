import globales
import Ventas
import os
import Estadistica


def menu_estadistica():
    while True:
        os.system("cls")
        print("========= MENU ESTADISTICA =========")
        print("1. Venta más alta")
        print("2. Venta más baja")
        print("3. Promedio de Ventas")
        print("4. Media Geometrica")
        print("5. Volver al menú anterior")

        opcion = globales.seleccionar_opcion(5)
        if opcion == 1:
            print("1. Venta más alta")
            Estadistica.venta_mas_alta()
        elif opcion == 2:
            print("2. Venta más baja")
            Estadistica.venta_mas_alta()
        elif opcion == 3:
            print("3. Promedio de Ventas")
            Estadistica.promedio_venta()
        elif opcion == 4:
            print("4. Media Geometrica")
            Estadistica.media_geometrica()
        elif opcion == 5:
            return








def Menu():
    while True:
        os.system("cls")
        print("========= MENU =========")
        print("1. Asignar Ventas Aleatorias")
        print("2. Ver Estadísticas")
        print("3. Salir")
        
        opcion = globales.seleccionar_opcion(3)
        if opcion == 1:
            
            Ventas.Precargar_Ventas()
        elif opcion == 2:
            
            menu_estadistica()
        elif opcion == 3:
            return

        

Menu()
