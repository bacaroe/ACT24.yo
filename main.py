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
            case 1: pass
            case 2: pass
            case 3: pass
            case 4: pass
            case 5: pass
            case 6: pass
            case 7: break
            case _: print("No válido")
    except Exception as e:
        print(f"Error {e}")