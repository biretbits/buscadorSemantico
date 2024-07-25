import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Paso 1: Preparar las asignaturas y el texto del usuario
asignaturas = ["fisica i", "analisis y base de datos i", 
"fisica iii", "analisis de sistemas", "analisis y diseño de base de datos", 
"fisica ii", "taller de programacion", "sistemas operativos",
"informatica forense","fisica","informatica matricial"]
texto_usuario = "me puedes decir cuantos estudiantes desertores tiene la materia de fisica i y taller de programacion de la carrera de informatica pero tambien de la materia de sistemas operativos"

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_sm")
carreras_no_tomar = ["informatica",
    "mecanica automotriz","minas",'contaduria publica','conta','contaduria',"electromecanica","mecanica",
     'mecanica automotris',"agronomia",'agro',"enfermeria","bioquimica","bio quimica",'biofar',"electro mecanica","civil","medicina",'topografia','enfermeria','enfer',"minas topografia","derecho","contaduria","contaduria publica",
     "comunicacion social","ciencias de la educacion"
     ,"laboratorio clinico","odontologia","odonto","infor",'tecnico superior en radioterapia nuclear','radioterapia nuclear'
     ,'radioterapia','radio nuclear','tecnico superior en medicina nuclear','medicina nuclear'
     ,'medi nuclear','tecnico superior radioterapia nuclear','tecnico superior medicina nuclear',
     'medi nuclear','recursos evaporiticos del litio','evaporiticos del litio','litio','evaporiticos litio'
     ,'bio medico','biomedico','bioquimica farmacia','electro','informati','bio','automotriz','automotris','auto','agronomica']
areas_no_tomar = ['tecnologia','salud','social','tecnologi','salu','sociales','sal','tecnolog','socia','sociale','tecnolo','tecnol','tecno','soci']
otros_no_tomar = ['unsxx','universidad','nacional','siglo','xx','universi','naciona','informacion']
def tokenizar(texto):
    #print(materias)
    doc = nlp(texto)
    palabras_filtradas = [
        token.text for token in doc
        if not token.is_stop and
           not token.text.isdigit() and
           not isinstance(token.text, int) and
           token.text not in carreras_no_tomar and
           token.text not in areas_no_tomar and
           token.text not in otros_no_tomar and
           not token.is_space]

    return " ".join([token for token in palabras_filtradas])


tokenized_asignaturas = [tokenizar(asignatura) for asignatura in asignaturas]
tokenized_texto_usuario = tokenizar(texto_usuario)

# Paso 3: Vectorizar los textos usando TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(tokenized_asignaturas + [tokenized_texto_usuario])

# Paso 4: Calcular la similitud del coseno
similarity_matrix = cosine_similarity(X[-1], X[:-1])

# Paso 5: Obtener las asignaturas relevantes
umbral = 0.15  # Ajusta este umbral según sea necesario
candidatos = [(asignaturas[i], similarity_matrix[0][i]) for i in range(len(asignaturas)) if similarity_matrix[0][i] > umbral]

# Mostrar los resultados
print("Asignaturas relevantes encontradas:", candidatos)
