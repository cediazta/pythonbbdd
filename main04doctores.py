import os
from services import service04sqldoctores as services

# FUNCIONES POR PANTALLA
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def verDoctores():
    print("---------- Doctores ----------")
    doctores = service.mostrarDoctor()
    for i in doctores:
        print(f"Cod. Hospital: {i.idHosp} - Nº Doctor: {i.idDoct} - Apellido: {i.apellidoDoct} - Especialidad: {i.especialidadDoct} - Salario: {i.salarioDoct}")
    print("------------------------------")

# SERVICIO ORACLE
service = services.ServiceDoctores()
limpiar_pantalla()
while True:
    print("----- Menu Doctores -----")
    print("- 1.Mostrar Doctores.   -")
    print("- 2.Añadir Doctor.      -")
    print("- 3.Modificar Doctor.   -")
    print("- 4.Eliminar Doctor.    -")
    print("- 0.Salir.              -")
    print("-------------------------")
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        verDoctores()

    elif opcion == 2:
        verDoctores()
        print("----- Añadir Doctor -----")
        idHosp = int(input("Cod. Hospital: "))
        apeDoct = input("Apellido: ").capitalize()
        espDoct = input("Especialidad: ").capitalize()
        salDoc = int(input("Salario: "))
        service.añadirDoctor(idHosp, apeDoct, espDoct, salDoc)
        limpiar_pantalla()
        print("--------------------------------")
        print("- Doctor Añadido Correctamente -")
        print("--------------------------------")

    elif opcion == 3:
        verDoctores()
        print("----- Modificar Doctor -----")
        idDoct = int(input("Nº Doctor: "))
        idHosp = int(input("Cod. Hospital: "))
        apeDoct = input("Apellido: ").capitalize()
        espDoct = input("Especialidad: ").capitalize()
        salDoc = int(input("Salario: "))
        service.modificarDoctor(idHosp, idDoct, apeDoct, espDoct, salDoc)
        limpiar_pantalla()
        print("------------------------------------")
        print("- Doctor Actualizado Correctamente -")
        print("------------------------------------")
    elif opcion == 4:
        verDoctores()
        print("----- Eliminar Doctor -----")
        idDoct = int(input("Nº Doctor: "))
        service.deleteDoctor(idDoct)
        limpiar_pantalla()
        print("----------------------------------")
        print("- Doctor Eliminado Correctamente -")
        print("----------------------------------")

    elif opcion == 0:
        break

    else:
        print("No existe esa opcion.")

print("Fin de Programa")


