from sklearn.model_selection import train_test_split
from sympy import symbols, Not
from sklearn.metrics import accuracy_score

# Datos de ejemplo
estudiantes = [
    {"horas_estudio": 4, "asistencia_clases": 1, "paso_examen": True},
    {"horas_estudio": 1, "asistencia_clases": 0, "paso_examen": False},
    {"horas_estudio": 3, "asistencia_clases": 1, "paso_examen": True},
    {"horas_estudio": 2, "asistencia_clases": 1, "paso_examen": False},
    # Agregar más ejemplos
]

# Dividir los datos en entrenamiento y prueba
train_data, test_data = train_test_split(estudiantes, test_size=0.2, random_state=42)

# Inicializar símbolos
horas_estudio, asistencia_clases = symbols('horas_estudio asistencia_clases')

# Hipótesis iniciales
hypothesis = (horas_estudio > 2) & (asistencia_clases > 0)

# Aprender la regla utilizando FOIL
for estudiante in train_data:
    if estudiante["paso_examen"]:
        target = True
    else:
        target = Not(True)
    
    if not hypothesis.subs({horas_estudio: estudiante["horas_estudio"], asistencia_clases: estudiante["asistencia_clases"]}) == target:
        hypothesis = hypothesis | (horas_estudio == estudiante["horas_estudio"]) & (asistencia_clases == estudiante["asistencia_clases"])

# Evaluar la regla aprendida en los datos de prueba
predictions = [hypothesis.subs({horas_estudio: estudiante["horas_estudio"], asistencia_clases: estudiante["asistencia_clases"]}) for estudiante in test_data]

# Calcular la precisión de la regla en los datos de prueba
y_true = [estudiante["paso_examen"] for estudiante in test_data]
accuracy = accuracy_score(y_true, predictions)
print("Precisión de la regla FOIL en datos de prueba:", accuracy)
