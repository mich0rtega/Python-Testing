class Persona:
    def __init__(self, id: int, nombre: str, direccion: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

   
    def actualizar_datos(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Cliente(Persona):
    def __init__(self, id, nombre, direccion, telefono, tipo):
        super().__init__(id, nombre, direccion, telefono)
        self.tipo = tipo
        self.animales = []

    

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, animal):
        self.animales.remove(animal)

class Empleado(Persona):
    def __init__(self, id, nombre, direccion, telefono, puesto, salario):
        super().__init__(id, nombre, direccion, telefono)
        self.puesto = puesto
        self.salario = salario

   

    def atender_cita(self, cita):
        print("Estoy atendiendo cita")

class Veterinaria:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
        self.clientes = []
        self.empleados = []
        self.citas = []
        self.servicios = []


    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def agregar_empleado(self, empleado: Empleado):
        self.empleados.append(empleado)

    def programar_cita(self, cita):
        self.citas.append(cita)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

class Servicio:
    def __init__(self, id, nombre, descripcion, costo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo



    def actualizar_costo(self, costo: float):
        self.costo = costo

class Cita:
    def __init__(self, id, fecha, id_cliente, id_animal, id_empleado, id_servicio):
        self.id = id
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.id_animal = id_animal
        self.id_empleado = id_empleado
        self.id_servicio = id_servicio



    def confirmar(self):
        print("Cita confirmada")

    def cancelar(self):
        print("Cita cancelada")

class Animal:
    def __init__(self, id, nombre, raza, edad, id_cliente):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.id_cliente = id_cliente
        self.consultas = []
        self.vacunas = []

   


class Consulta:
    def __init__(self, duracion):
        self.duracion = duracion

    def realizar_consulta(self):
        print("Se realizo consulta")

class Vacuna:
    def __init__(self, tipo):
        self.tipo = tipo


    def administrar_vacuna(self):
        print("se administro vacunas")
