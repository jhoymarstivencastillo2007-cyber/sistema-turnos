CAPACIDAD = 5

cola = []


def encolar(nombre, motivo):
    if len(cola) >= CAPACIDAD:
        print("\nLa cola está llena. No se puede agregar otro estudiante.")
        return

    estudiante = {
        "nombre": nombre,
        "motivo": motivo
    }

    cola.append(estudiante)
    print(f"\n{nombre} fue agregado a la cola.")


def desencolar():
    if len(cola) == 0:
        print("\nLa cola está vacía. No hay estudiantes para atender.")
        return

    estudiante = cola.pop(0)

    print(
        f"\nAtendiendo a: {estudiante['nombre']} "
        f"- Motivo: {estudiante['motivo']}"
    )


def mostrar_cola():
    if len(cola) == 0:
        print("\nLa cola está vacía.")
        return

    print("\n===== ESTUDIANTES EN ESPERA =====")

    for posicion, estudiante in enumerate(cola):
        print(
            f"{posicion + 1}. {estudiante['nombre']} "
            f"- {estudiante['motivo']}"
        )


def menu():
    while True:
        print("\n===== SISTEMA DE TURNOS =====")
        print("1. Agregar estudiante")
        print("2. Atender estudiante")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            motivo = input("Motivo de la atención: ")
            encolar(nombre, motivo)

        elif opcion == "2":
            desencolar()

        elif opcion == "3":
            mostrar_cola()

        elif opcion == "4":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


menu()