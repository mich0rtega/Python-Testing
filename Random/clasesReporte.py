class Persona:
    def __init__(self, nombre, edad, sexo, tipo_sangre, altura, peso, alergias):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__tipo_sangre = tipo_sangre
        self.__altura = altura
        self.__peso = peso
        self.__alergias = alergias

    # Métodos del diagrama
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    # Métodos get y set 
    def getnombre(self):
        return self.__nombre

    def setnombre(self, nombre):
        self.__nombre = nombre

    def getedad(self):
        return self.__edad

    def setedad(self, edad):
        self.__edad = edad

    def getsexo(self):
        return self.__sexo

    def setsexo(self, sexo):
        self.__sexo = sexo

    def gettiposangre(self):
        return self.__tipo_sangre

    def settiposangre(self, tipo_sangre):
        self.__tipo_sangre = tipo_sangre

    def getaltura(self):
        return self.__altura

    def setaltura(self, altura):
        self.__altura = altura

    def getpeso(self):
        return self.__peso

    def setpeso(self, peso):
        self.__peso = peso

    def getalergias(self):
        return self.__alergias

    def setalergias(self, alergias):
        self.__alergias = alergias


class SignosVitales:
    def __init__(self, temperatura, presion_sistolica, presion_diastolica, pulso):
        self.__temperatura = temperatura
        self.__presion_sistolica = presion_sistolica
        self.__presion_diastolica = presion_diastolica
        self.__pulso = pulso
        
    #Métodos del diagrama
    def consultar_signosvitales(self):
        return {
            "temperatura": self.__temperatura,
            "presion_sistolica": self.__presion_sistolica,
            "presion_diastolica": self.__presion_diastolica,
            "pulso": self.__pulso
        }
        
    # Métodos get y set
    def gettemperatura(self):
        return self.__temperatura

    def settemperatura(self, temperatura):
        self.__temperatura = temperatura

    def getpresionsistolica(self):
        return self.__presion_sistolica

    def setpresionsistolica(self, presion_sistolica):
        self.__presion_sistolica = presion_sistolica

    def getpresiondiastolica(self):
        return self.__presion_diastolica

    def setpresiondiastolica(self, presion_diastolica):
        self.__presion_diastolica = presion_diastolica

    def getpulso(self):
        return self.__pulso

    def setpulso(self, pulso):
        self.__pulso = pulso


class Paciente(Persona):
    def __init__(self, nombre, edad, sexo, tipo_sangre, altura, peso, alergias, numero_cama, diagnostico, signos_vitales, id_paciente, historial_clinico):
        super().__init__(nombre, edad, sexo, tipo_sangre, altura, peso, alergias)
        self.__numero_cama = numero_cama
        self.__diagnostico = diagnostico
        self.__signos_vitales = signos_vitales
        self.__id_paciente = id_paciente
        self.__historial_clinico = historial_clinico

    # Métodos del diagrama
    def consultar_historial(self):
        return self.__historial_clinico

    def consultar_signosvitales(self):
        return self.__signos_vitales

    # Métodos get y set 
    def getnumerocama(self):
        return self.__numero_cama

    def setnumerocama(self, numero_cama):
        self.__numero_cama = numero_cama

    def getdiagnostico(self):
        return self.__diagnostico

    def setdiagnostico(self, diagnostico):
        self.__diagnostico = diagnostico

    def getidpaciente(self):
        return self.__id_paciente

    def setidpaciente(self, id_paciente):
        self.__id_paciente = id_paciente

    def getsignosvitales(self):
        return self.__signos_vitales

    def setsignosvitales(self, signos_vitales):
        self.__signos_vitales = signos_vitales


class HistorialClinico:
    def __init__(self, notas, diagnostico):
        self.__notas = notas
        self.__diagnostico = diagnostico

    # Métodos del diagrama
    def mostrar_historia(self):
        return {
            "notas": self.__notas,
            "diagnostico": self.__diagnostico
        }

    def agregar_nota(self, nueva_nota):
        self.__notas.append(nueva_nota)

    def actualizar_nota(self, indice, nueva_nota):
        if 0 <= indice < len(self.__notas):
            self.__notas[indice] = nueva_nota

    # Métodos get y set 
    def getnotas(self):
        return self.__notas

    def setnotas(self, notas):
        self.__notas = notas

    def setdiagnostico(self, diagnostico):
        self.__diagnostico = diagnostico

    def getdiagnostico(self):
        return self.__diagnostico


class Medico(Persona):
    def __init__(self, nombre, edad, sexo, tipo_sangre, altura, peso, alergias, especialidad, id_medico, area):
        super().__init__(nombre, edad, sexo, tipo_sangre, altura, peso, alergias)
        self.__especialidad = especialidad
        self.__id_medico = id_medico
        self.__area = area

    # Métodos del diagrama
    def realizar_diagnostico(self):
        return ''

    def recetar_medicamento(self):
        return ''

    # Métodos get y set 
    def getespecialidad(self):
        return self.__especialidad

    def setespecialidad(self, especialidad):
        self.__especialidad = especialidad

    def getidmedico(self):
        return self.__id_medico

    def setidmedico(self, id_medico):
        self.__id_medico = id_medico

    def getarea(self):
        return self.__area

    def setarea(self, area):
        self.__area = area


class Enfermero(Persona):
    def __init__(self, nombre, edad, sexo, tipo_sangre, altura, peso, alergias, registro, area, turno, id_enfermero):
        super().__init__(nombre, edad, sexo, tipo_sangre, altura, peso, alergias)
        self.__registro = registro
        self.__area = area
        self.__turno = turno
        self.__id_enfermero = id_enfermero

    # Métodos del diagrama
    def registrar_paciente(self):
        self.__registro = ''

    # Métodos get y set 
    def getregistro(self):
        return self.__registro

    def setregistro(self, registro):
        self.__registro = registro

    def getarea(self):
        return self.__area

    def setarea(self, area):
        self.__area = area

    def getturno(self):
        return self.__turno

    def setturno(self, turno):
        self.__turno = turno

    def getidenfermero(self):
        return self.__id_enfermero

    def setidenfermero(self, id_enfermero):
        self.__id_enfermero = id_enfermero

#Metodos para imprimir
def imprimir_signos_vitales(signos):
    print(f"Temperatura: {signos.gettemperatura()}\n Presión Sistólica: {signos.getpresionsistolica()}\nPresión Diastólica: {signos.getpresiondiastolica()}\nPulso: {signos.getpulso()}")
   
def imprimir_historial_clinico(historial):
    print(f"Notas: {historial.getnotas()}\n Diagnóstico: {historial.getdiagnostico()}")
    

def imprimir_persona(persona):
    print(f"Nombre: {persona.obtener_nombre()}\nEdad: {persona.getedad()}\nSexo: {persona.getsexo()}\nTipo de Sangre: {persona.gettiposangre()}\nAltura: {persona.getaltura()}\n Peso: {persona.getpeso()}\nAlergias: {persona.getalergias()}")

def imprimir_paciente(paciente):
    
    print(f"Número de Cama: {paciente.getnumerocama()}\n Diagnóstico: {paciente.getdiagnostico()}\nID Paciente: {paciente.getidpaciente()}")
    print("Signos Vitales:")
    imprimir_signos_vitales(paciente.getsignosvitales())
    print("Historial Clínico:")
    imprimir_historial_clinico(paciente.consultar_historial())

def imprimir_medico(medico):
    imprimir_persona(medico)
    print(f"Especialidad: {medico.getespecialidad()}\n ID Médico: {medico.getidmedico()}\nÁrea: {medico.getarea()}")

def imprimir_enfermero(enfermero):
    print(f"Registro: {enfermero.getregistro()}\nÁrea: {enfermero.getarea()}\nTurno: {enfermero.getturno()}\nID Enfermero: {enfermero.getidenfermero()}")

