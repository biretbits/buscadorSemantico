

from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter
import spacy
from spacy.matcher import Matcher

# Cargar el modelo en español
nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

patterns = {
#patrones para obtener carrera y tambien poder obtener carrear por su nombre
"ver_carreras": [
    {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
    {"LEMMA": {"IN": ["carrera"]}},
    {"LEMMA": {"IN": ["cual","cuales"]}, "OP": "?"},
    {"LEMMA": {"IN": ["unsxx"]}, "OP": "?"},
    {"LEMMA": {"IN": ["ingenieria"]}, "OP": "?"},
    {"LEMMA": {"IN": ["datos","informacion","detalle"]}, "OP": "?"},
],
#patrones para obtener el total de estudiantes en la unsxx
"total_de_estudiantes": [
    {"LEMMA": {"IN": ["", "ver", "visualizar"]}, "OP": "?"},
    {"LEMMA": {"IN": ["total", "cantidad", "cuantos","numero"]}},
    {"LEMMA": {"IN": ["estudiante", "alumno"]}},
    {"LEMMA": {"IN": ["universidad", "unsxx"]}, "OP": "?"}
],
    "SHOW_FAILED_STUDENTS": [
        {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
        {"LEMMA": {"IN": ["estudiante", "alumno"]}},
        {"LEMMA": {"IN": ["aplazar", "reprobar",""]}},
        {"LEMMA": {"IN": ["carrera", "grado"]}, "OP": "?"},
        {"LOWER": {"IN": ["mecánica", "ingeniería mecánica"]}, "OP": "?"}
    ],

}





consultas_sql = {"ver_carreras":"select *from carrera",
"ver_carreras_nombre":"select *from carrera where nombre_carrera like '%{}%';",
"total_de_estudiantes":"SELECT COUNT(*) FROM estudiante;"
}




def buscar(texto):
    text = texto.lower()
    # Añadir patrones al matcher con sus etiquetas correspondientes
    for intent, pattern in patterns.items():
        matcher.add(intent, [pattern])
    # Procesar el texto
    doc = nlp(text)
    # Enviar los tokens SpaCy al matcher
    matches = matcher(doc)

    # Determinar la intención del usuario
    intencion = None
    for match_id, start, end in matches:
        match_id_str = nlp.vocab.strings[match_id]
        matched_span = doc[start:end]
        intencion = match_id_str  # Guardar la intención correspondiente
        #print(f"Coincidencia: {matched_span.texto}, Intención: {intencion}")
    response = ""
    nombre_posicion_sql = ""
    if intencion:
        if intencion == "ver_carreras":
            carreras_encontradas = obtener_carreras_nombre(text);
            if carreras_encontradas:
                # Obtener la primera carrera encontrada
                primera_carrera = carreras_encontradas.pop(0)
                nombre_posicion_sql = "ver_carreras_nombre"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql.format(primera_carrera)
            else:
                nombre_posicion_sql = "ver_carreras"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql

        if intencion == "total_de_estudiantes":
            nombre_posicion_sql = "total_de_estudiantes"
            sql = consultas_sql[nombre_posicion_sql]
            response = sql

        return response,nombre_posicion_sql
    else:
        return ("Lo siento, no tengo una respuesta para esa pregunta o puede argumentar un poco mas.")
