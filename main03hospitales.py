import os
from services import service03oraclehospitales as services

# Funciones por pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrarHospitales():
    print("--- Listado de Hospitales--- ")
    lista = service.getHospitales()
    for h in lista:
        print(f"Id: {h.idHosp} - Nombre: {h.nombreHosp} - Direccion: {h.direccionHosp} - Telefono: {h.telefonoHosp} - Camas: {h.camasHosp}")

# Creamos nuestro servicio de oracle
service = services.ServiceHospitales()

limpiar_pantalla()
while True:
    mostrarHospitales()
    print("\n----- Menu Hospitales -----")
    print("1.Insertar Hospital.")
    print("2.Actualizar Hospital.")
    print("3.Eliminar Hospital.")
    print("0.Salir")
    print("---------------------------")
    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        print("--- Insertar Hospital ---")
        id = int(input("Id: "))
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")
        camas = int(input("Nº de Camas: "))
        service.insertarHospital(id, nombre, direccion, telefono, camas,)
        limpiar_pantalla()
        print("-------------------------------")
        print("-   Insertado Correctamente   -")
        print("-------------------------------")

    elif opcion == 2:
        print("--- Actualizar Hospital ---")
        id = int(input("Id Hospital a Actualizar: "))
        nombre = input("Nombre: ")
        direccion = input("Direccion: ")
        telefono = input("Telefono: ")
        camas = int(input("Nº de Camas: "))
        service.updateHospital(id, nombre, direccion, telefono, camas)
        limpiar_pantalla()
        print("---------------------------------")
        print("-   Actualizado correctamente   -")
        print("---------------------------------")

    elif opcion == 3:
        print("--- Eliminar Hospital ---")
        id = int(input("Id del Hospital: "))
        service.deleteHospital(id)
        limpiar_pantalla()
        print("------------------------------------")
        print("- Hospital eliminado correctamente -")
        print("------------------------------------")

    elif opcion == 0:
        break
    
    else:
        print("No existe esa opcion.")

print("Fin de Programa")
