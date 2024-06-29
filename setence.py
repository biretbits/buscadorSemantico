from sentence_transformers import SentenceTransformer, util
import mysql.connector
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

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



# Configuración de la conexión a MySQL
config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'tu_base_de_datos'
}

# Conectar a la base de datos MySQL
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

try:
    # Ejemplo de consulta
    consulta = "Ingeniería de Software"

    # Calcular el embedding de la consulta (usando sentence-transformers si es necesario)
    # Aquí se simula con un embedding ficticio para la consulta
    embedding_consulta = np.random.rand(768)  # Simulación de un embedding

    # Consulta SQL para obtener los embeddings de las asignaturas
    query = "SELECT codigo_asignatura, embedding_asignatura FROM asignaturas"

    # Ejecutar la consulta
    cursor.execute(query)

    # Inicializar listas para almacenar los embeddings y códigos de asignatura
    embeddings = []
    codigos = []

    # Obtener todos los embeddings y códigos de asignatura
    for row in cursor.fetchall():
        codigos.append(row[0])
        embeddings.append(np.frombuffer(row[1], dtype=np.float32))  # Convertir el blob a un array numpy

    # Convertir la lista de embeddings a un array numpy para calcular similitudes
    embeddings = np.array(embeddings)

    # Calcular las similitudes coseno entre la consulta y todos los embeddings de las asignaturas
    similitudes = cosine_similarity([embedding_consulta], embeddings)

    # Encontrar el índice del máximo coseno
    indice_max_coseno = similitudes.argmax()

    # Obtener el máximo coseno, el nombre y el código de la asignatura correspondiente
    max_coseno = similitudes[0, indice_max_coseno]
    codigo_asignatura = codigos[indice_max_coseno]

    # Mostrar resultados
    print(f"Asignatura más relevante (código): {codigo_asignatura}")
    print(f"Coseno máximo: {max_coseno}")

finally:
    # Cerrar cursor y conexión
    cursor.close()
    conn.close()
