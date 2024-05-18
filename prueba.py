

from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.metrics import jaccard_distance

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Definir la lista de pares
pares = [
#0
["todo todos cual cuanto cuantos cantidad estudiante estudiantes carrera",["SELECT c.nombre_carrera, COUNT(*) AS total_estudiantes FROM carrera AS c INNER JOIN estudiante AS e ON c.cod_carrera = e.cod_carrera WHERE c.nombre_carrera like '%{}%';"]],
    # Desactivos estudiantess por carrera y activos y detalle
#1
["activo activos todo todos cantidad estudiante estudiantes carrera quienes quien descripcion detalle  quiero  obten obtenemelo",["SELECT nombre_carrera,nombre_es,ap_es,am_es,ci,pais_es,departamento,provincia,ciudad,region,sexo FROM carrera AS c INNER JOIN estudiante AS e ON c.cod_carrera = e.cod_carrera WHERE e.estado = 'activo' and c.nombre_carrera like '%{}%'"]],
#2
["desactivo desactivos todo todos cantidad estudiante estudiantes carrera quienes quien descripcion detalle  quiero  obten obtenemelo",["SELECT nombre_carrera,nombre_es,ap_es,am_es,ci,pais_es,departamento,provincia,ciudad,region,sexo FROM carrera AS c INNER JOIN estudiante AS e ON c.cod_carrera = e.cod_carrera WHERE e.estado = 'desactivo' and c.nombre_carrera like '%{}%' "]],
#3
["activo activos todo todos cantidad estudiante estudiantes carrera quienes quien descripcion detalle delimitado quiero limitado delimitamelo limitamelo obten obtenemelo",["SELECT nombre_carrera,nombre_es,ap_es,am_es,ci,pais_es,departamento,provincia,ciudad,region,sexo FROM carrera AS c INNER JOIN estudiante AS e ON c.cod_carrera = e.cod_carrera WHERE e.estado = 'activo' and c.nombre_carrera like '%{}%' limit {};"]],
#4
["desactivo desactivos todo todos cantidad estudiante estudiantes carrera quienes quien descripcion detalle delimitado quiero limitado delimitamelo limitamelo obten obtenemelo",["SELECT nombre_carrera,nombre_es,ap_es,am_es,ci,pais_es,departamento,provincia,ciudad,region,sexo FROM carrera AS c INNER JOIN estudiante AS e ON c.cod_carrera = e.cod_carrera WHERE e.estado = 'desactivo' and c.nombre_carrera like '%{}%' limit {};"]],
#5
["cuales cual carrera unsxx universidad nacional siglo xx",["select *from carrera;"]],
#6
["cuales cual carrera direccion infomacion dato datos lugar",["select *from carrera where nombre_carrera like '%{}%';"]],
]


# Función para preprocesar y tokenizar el texto
def preprocess_text(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text.lower())

    stop_words = set(stopwords.words('spanish'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    return lemmatized_tokens

# Función para calcular la similitud palabra por palabra
def calculate_similarity_word_by_word(user_tokens, query_tokens):
    common_words = set(user_tokens) & set(query_tokens)
    return len(common_words)

def buscar(texto):
    max_similarity = -1
    response_index = -1
    response = ""

    # Tokenizar el texto del usuario
    user_tokens = preprocess_text(texto)

    # Recorremos los pares de consultas
    for i, (input_phrase, responses) in enumerate(pares):
        query_tokens = preprocess_text(input_phrase)
        similarity = calculate_similarity_word_by_word(user_tokens, query_tokens)

        # Si la similitud es mayor, actualiza la respuesta y el índice
        if similarity > max_similarity:
            max_similarity = similarity
            response = responses[0]  # Asumimos que la consulta genérica está en la posición 0 del array de respuestas
            response_index = i
    carreras_encontradas = obtener_carreras_nombre(texto);
    primera_carrera = carreras_encontradas.pop(0)
    print("la carrera es ",primera_carrera)
    response = response.format(primera_carrera)
    return response, response_index

# Ejemplo de uso
user_query = "direccion  bioquimica"
respuesta, indice = buscar(user_query)
print("Respuesta:", respuesta)
print("Índice de la consulta seleccionada:", indice)
