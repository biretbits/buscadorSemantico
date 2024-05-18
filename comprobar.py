import spacy
import unicodedata
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def eliminar_tildes(texto):
    # Utilizamos la librería unicodedata para eliminar las tildes
    texto_nfd = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(c for c in texto_nfd if not unicodedata.combining(c))
    return texto_sin_tildes

def obtener_carreras_nombre(texto):
    # Cargar el modelo pre-entrenado en español
    nlp = spacy.load("es_core_news_sm")

    carreras_keywords = ["informatica", "mecanica automotriz", "minas", "electromecanica",
     "mecanica","agronomia","enfermeria","bioquimica","bio quimica","electro mecanica","civil","medicina",
     "minas topografia","derecho","contaduria","contaduria publica","comunicacion social","ciencias de la educacion"
     ,"laboratorio clinico","odontologia","odonto","infor"]
    carreras_encontradas = []
    # Convertir el texto a minúsculas y eliminar tildes
    texto_normalizado = eliminar_tildes(texto.lower())

    # Procesar el texto con el modelo de Spacy
    doc = nlp(texto_normalizado)
    # Verificar si hay entidades de tipo MISC en el texto
    for ent in doc.ents:
        if ent.label_ == "MISC":
            carreras_encontradas.append(ent.text)

    # Buscar palabras clave asociadas con carreras universitarias en el texto
    for carrera_keyword in carreras_keywords:
        if carrera_keyword in texto_normalizado:
            carreras_encontradas.append(carrera_keyword)

    return carreras_encontradas

def detectar_numeros_delimiter(texto):
    # Tokenizar el texto en palabras
    tokens = word_tokenize(texto)

    # Etiquetar partes del habla
    tagged_tokens = pos_tag(tokens)

    # Buscar tokens etiquetados como números (CD: cardinal numbers)
    numeros = [token[0] for token in tagged_tokens if token[1] == 'CD']

    return numeros
