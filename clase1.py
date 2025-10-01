class Empleado:
    def __init__(self):
        self.nombre=input("ingrese el nombre del empleado:")
        self.sueldo=float(input("ingrese el sueldo:"))

    def imprimir(self):
        print("nombre:",self.nombre)
        print("sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print ("Debe pagar impuestos")
        else:
            print("No paga impuestos")

    def cambiar_nombre(self):
        self.nombre = input("Ingrese el nuevo nombre: ")

    def cambiar_sueldo(self):
        self.sueldo =(input("Ingrese el nuevo sueldo: "))
        print("Sueldo anterior:", self.nombre, "Nuevo sueldo:", self.sueldo)

    def clasificarcion_sueldo(self):
        if self.sueldo < 2000:
            print("El sueldo es bajo")
        elif 2000 <= self.sueldo <= 5000:
            print("El sueldo es medio")
        else:
            print("El sueldo es alto")

empleado1 = None  

while True:
    print("\n--- MENÚ ---")
    print("1. Crear empleado")
    print("2. Imprimir datos")
    print("3. Verificar si paga impuestos")
    print("4. Cambiar nombre")
    print("5. Cambiar sueldo")
    print("6. Clasificación del sueldo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        empleado1 = Empleado()
    elif opcion == "2":
        if empleado1:
            empleado1.imprimir()
        else:
            print(" Primero ingresar un empleado")
    elif opcion == "3":
        if empleado1:
            empleado1.paga_impuestos()
        else:
            print("Primero ingresar un empleado")
    elif opcion == "4":
        if empleado1:
            empleado1.cambiar_nombre()
        else:
            print("Primero ingresar un empleado")
    elif opcion == "5":
        if empleado1:
            empleado1.cambiar_sueldo()
        else:
            print("Primero ingresar un empleado")
    elif opcion == "6":
        if empleado1:
            empleado1.clasificacion_sueldo()
        else:
            print("Primero ingresar un empleado")
    elif opcion == "7":
        print("Salió del menú")
        break

    else:
        print("Selecciona otra opción")
