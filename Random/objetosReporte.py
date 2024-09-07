from clasesReporte import *


signos_vitales1 = SignosVitales(37.0, 120, 80, 75)
signos_vitales2 = SignosVitales(38.1, 110, 91, 68)
historial_clinico1 = HistorialClinico(["Paciente en alta"], "Fractura de alto grado")
historial_clinico2 = HistorialClinico(["Paciente en observación"], "Fiebre svera")

paciente1 = Paciente("Sebastian Vazquez", 50, "M", "B", 1.70, 75, "No", 101, "Fractura", signos_vitales1, 1, historial_clinico1)
paciente2 = Paciente("Alejandra Luna", 46, "F", "A", 1.63, 60, "Polen", 55, "Fiebre", signos_vitales2, 2, historial_clinico2)

medico1 = Medico("Dr Juan Perez", 45, "M", "A+", 1.80, 80, "No", "Cardiología", 200, "Cuidados Intensivos")
medico2 = Medico("Dra Maria Lopez", 38, "F", "O-", 1.65, 60, "No", "Internista", 201, "Medicina Interna")

enfermero1 = Enfermero("Sara Lopez", 30, "F", "B-", 1.70, 65, "No", "12345", "Neonatos", "matutino", 1)
enfermero2 = Enfermero("Julian Martinez", 45, "M", "O+", 1.75, 70, "No", "54321", "Pediatría", "vespertino", 2)

print("\nPaciente 1:")
imprimir_paciente(paciente1)
print("\nPaciente 2:")
imprimir_paciente(paciente2)

print("\nMédico 1:")
imprimir_medico(medico1)
print("\nMédico 2:")
imprimir_medico(medico2)

print("\nEnfermero 1:")
imprimir_enfermero(enfermero1)
print("\nEnfermero 2:")
imprimir_enfermero(enfermero2)
