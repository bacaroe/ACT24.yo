
#Colección para alamacenar temporalmente los personajes
personajes = []

def buscar(nombre):
    for i in range(len(personajes)):
        if personajes[i]["nombre"]==nombre:
            return i #retornamos la posición donde está 
    return -1 #Si el personaje no se encuentra es -1

def agregar(nombre,clase,nivel):
    #Validar datos  
    if len(nombre.strip())==0 or len(nombre.strip())>20:
        print("Nombre no válido")
        return 
    elif buscar(nombre)>=0:
        print("Nombre ya existe")
        return
    elif clase not in ("Guerrero", "Mago", "Picaro"):
        print("Clase no válida, debe ser Guerrero, Mago o Pícaro")
        return  
    elif nivel<=0 or nivel>50:
        print("El nivel debe estar entre 1 y 50")
        return
    #Registar personaje en la lista
    rango = "Recluta"
    if nivel>=30: rango = "Élite"
    pj = {"nombre":nombre,"clase":clase,"nivel":nivel,"rango":rango}
    personajes.append(pj)
    print("Personaje registrado")

def mostrar(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        print(f"Personaje encontrado : {personajes[posicion]}")
    else:
        print("Nombre no existe")
    
def listar():
    if len(personajes)>0:
        print(f"{"N°":<3}.-{"nombre":<20} {"Clase":<10} {"Nivel":<4} {"Rango":<10}")
        for i in range(len(personajes)):
            print(f"{i+1:<3}.-{personajes[i]["nombre"]:<20} {personajes[i]["clase"]:<10} {personajes[i]["nivel"]:<4} {personajes[i]["rango"]:<10}")
    else: 
        print("No hay personajes registrados")

def eliminar(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        validacion = input(f"¿Desea eliminar el personaje {nombre}? (S/N) ")
        if validacion=="S":
            personajes.pop(posicion)
            print("Personaje removido")
        else: 
            print("Proceso cancelado con éxito")
    else:
        print("Error, el personaje no pertenece al Gremio")

def SubirNivel(nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        nivel = personajes[posicion]["nivel"]
        if nivel<50:
            personajes[posicion]["nivel"] = nivel +1
            print("Nivel Aumentado")
            if nivel>=30: 
               personajes[posicion]["rango"] = "Élite"
        else:
             print("Ya ha alcanzado el nivel máximo")
    else:
        print("No se ha encontrado ningún personaje con ese nombre")

def estadisticas():
    sumaniveles = 0
    guerreros = 0
    magos = 0
    picaros = 0
    for pj in personajes:
        sumaniveles += pj["nivel"] #Sumar niveles
        match pj["clase"]:
            case "Guerrero": guerreros+=1
            case "Mago": magos+=1
            case "Pícaro": picaros+=1
    promedio = (sumaniveles/len(personajes)  ,1)
    print(f""" 
    Nivel promedio del gremio : {promedio}
    Cantidad Guerreros : {guerreros}
    Cantidad Magos     : {magos}
    Cantidad Pícaros   : {picaros}
    """)
