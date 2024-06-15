from sentence_transformers import SentenceTransformer, util

# Cargar el modelo pre-entrenado
model = SentenceTransformer('all-MiniLM-L6-v1')

# Oraciones de ejemplo
sentences = [
    "cantidad de estudiantes de la carrera de de la universidad nacional siglo xx",
    "quiero ver todas las carreras de la universidad nacional siglo xx",
    "todos los estudiantes aprobados o reprobados de la carrera de la universidad",
    "visualizar todos los estudiante y asignaturas unsxx",
    "quiero ver los estudiantes activos desactivos aprobados reprobado en toda la universidad nacion siglo xx",
]

# Consulta de búsqueda
query = "quiero ver los estudiantes activos desactivos aprobados reprobado en toda la universidad nacion siglo xx",


# Codificar la consulta
query_embedding = model.encode(query)

# Calcular la similitud coseno entre la consulta y todas las oraciones
results = []
for sentence in sentences:
    sentence_embedding = model.encode(sentence)
    cosine_score = util.cos_sim(query_embedding, sentence_embedding)
    results.append((cosine_score.item()))

print(results)
# Ordenar las oraciones según la similitud
#sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

# Imprimir los resultados ordenados
#for sentence, score in sorted_results:
#    print(f"Similitud: {score} - Oración: '{sentence}'")
import datetime

array_personalizado = {}

inicio_anio = 2015
fin_anio = 2029

for anio in range(inicio_anio, fin_anio + 1):
    array_personalizado[anio] = [5, 0, 0, 0, 0, 0]

print(array_personalizado[2015][0])
arr = {}
for car in range(17):
    ##enviamos el id de la carrera y el plan de estudio
    arr[car] = {}
    for anio in range(5):
        arr[car][anio] = [5,7]

print(arr[1][2][1])
