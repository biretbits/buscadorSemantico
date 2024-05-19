import spacy
from spacy.matcher import Matcher

# Cargar el modelo en español
nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

patterns = {
    "ver_carreras": [
        {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
        {"LEMMA": {"IN": ["carrera"]}, "OP": "?"},
        {"LEMMA": {"IN": ["cual"]}, "OP": "?"},
        {"LEMMA": {"IN": ["unsxx"]}, "OP": "?"},
        {"LEMMA": {"IN": ["ingenieria"]}, "OP": "?"},
        {"LEMMA": {"IN": ["datos","informacion","detalle"]}, "OP": "?"},
    ],
    "SHOW_FAILED_STUDENTS": [
        {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
        {"LEMMA": {"IN": ["estudiante", "alumno"]}},
        {"LEMMA": {"IN": ["aplazar", "reprobar",""]}},
        {"LEMMA": {"IN": ["carrera", "grado"]}, "OP": "?"},
        {"LOWER": {"IN": ["mecánica", "ingeniería mecánica"]}, "OP": "?"}
    ],
    "SHOW_PASSED_STUDENTS": [
        {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
        {"LEMMA": {"IN": ["estudiante", "alumno"]}},
        {"LEMMA": "aprobar", "OP": "?"},
        {"LOWER": {"IN": ["mecánica", "ingeniería mecánica"]}, "OP": "?"}
    ],
    "estudiante carrera activos": [
        {"LEMMA": {"IN": ["mostrar", "ver", "visualizar"]}, "OP": "?"},
        {"LEMMA": {"IN": ["estudiante", "alumno"]}},
    {"LEMMA": {"IN": ["aplazar", "reprobar",""]}},
        {"LEMMA": "activo"},
        {"LEMMA": {"IN": ["carrera", "grado"]}},
        {"LOWER": {"IN": ["mecánica", "ingeniería mecánica"]}, "OP": "?"}
    ]
}


# Añadir patrones al matcher con sus etiquetas correspondientes
for intent, pattern in patterns.items():
    matcher.add(intent, [pattern])

# Texto de ejemplo
text = "carrera de informatica"

# Procesar el texto
doc = nlp(text)
matches = matcher(doc)

# Determinar la intención del usuario
intention = None
for match_id, start, end in matches:
    match_id_str = nlp.vocab.strings[match_id]
    matched_span = doc[start:end]
    intention = match_id_str  # Guardar la intención correspondiente
    print(f"Coincidencia: {matched_span.text}, Intención: {intention}")

if intention:
    print(f"La intención del usuario es: {intention}")
else:
    print("No se pudo determinar la intención del usuario.")
