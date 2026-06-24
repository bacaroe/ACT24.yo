from funciones import *
from os import system

while True:
    try:
        system("pause")
        system("cls")
        print(""" 
========== MENÚ DE GESTIÓN GREMIAL ==========
1. Registrar Personaje
2. Buscar Personaje por Nombre
3. Eliminar Personaje
4. Subir de Nivel a un Personaje
5. Calcular Estadísticas Generales
6. Mostrar Lista de Miembros
7. Salir del Sistema
=============================================""")
        opcion = int(input("Seleccione : "))

        match opcion:
            case 1:
                nombre = input("Ingrese ombre : ").title()
                clase = input("Ingrese Clase : ").title()
                nivel = int(input("Ingrese nivel : "))
                agregar(nombre, clase, nivel)
            case 2:
                nombre = input("Ingrese nombre : ").title()
                mostrar(nombre)
            case 3:
                nombre_eliminar = input("Ingrese nombre del personaje que desea borrar : ")
                eliminar(nombre_eliminar)
            case 4: 
                nombre_subir = input("Ingrese el personaje que desea subir de nivel : ")
                SubirNivel(nombre_subir)
            case 5: pass
            case 6: listar()
            case 7: break
            case _: print("No válido")
    except Exception as e:
        print(f"Error {e}")