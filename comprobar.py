import spacy
import unicodedata
import pymysql
import re
from sql import obtener_id_de_carrera,seleccionarAsignaturaTodos,buscar_AsignaturaPORnombre
from sql import buscar_Area_por_nombre,buscar_Carrera_por_nombre,obtener_asignaturas_embeddign
from sentence_transformers import SentenceTransformer, util
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from unidecode import unidecode
from sql import obtener_embeddings_ahora
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
# Cargar el modelo de lenguaje en español

# Cargar el modelo de embeddings
modelo = SentenceTransformer('paraphrase-MiniLM-L6-v2')
nlp = spacy.load("es_core_news_sm")

def obtener_carreras_nombre(texto):
    # Cargar el modelo pre-entrenado en español

    carreras_keywords = ["informatica",
    "mecanica automotriz",
    "minas",'contaduria publica','conta','contaduria'
     "electromecanica",
     "mecanica",
     'mecanica automotris',
     "agronomia",
     'agro',
     "enfermeria",
     "bioquimica",
     "bio quimica",
     'biofar',
     "electro mecanica",
     "civil","medicina",
     'topografia','enfermeria','enfer',
     "minas topografia","derecho","contaduria","contaduria publica",
     "comunicacion social","ciencias de la educacion"
     ,"laboratorio clinico","odontologia","odonto","infor",'tecnico superior en radioterapia nuclear','radioterapia nuclear'
     ,'radioterapia','radio nuclear','tecnico superior en medicina nuclear','medicina nuclear'
     ,'medi nuclear','tecnico superior radioterapia nuclear','tecnico superior medicina nuclear',
     'medi nuclear','recursos evaporiticos del litio','evaporiticos del litio','litio','evaporiticos litio'
     ,'bio medico','biomedico','bioquimica farmacia','electro','informati','bio','automotriz','automotris','auto','agronomica']

    carreras_encontradas = []
    # Convertir el texto a minúsculas y eliminar tildes
    salida = nlp(texto)
    # Buscar palabras clave asociadas con carreras universitarias en el texto
    for pal in salida:
        if pal.text in carreras_keywords:
            carreras_encontradas.append(obtener_id_de_carrera(pal.text))

    return carreras_encontradas



def detectar_numeros_delimiter(texto):
    # Tokenizar el texto en palabras
    tokens = word_tokenize(texto)

    # Etiquetar partes del habla
    tagged_tokens = pos_tag(tokens)

    # Buscar tokens etiquetados como números (CD: cardinal numbers)
    numeros = [token[0] for token in tagged_tokens if token[1] == 'CD']

    return numeros

# Funcion para procesar un texto y verificar si contiene palabras activas
def contiene_palabras_activas(texto):
    # array de palabras activas
    palabras_activas = ["activa", "activo", "activos", "activas","habilitado","habilitados"]
    # Procesar el texto con spaCy
    doc1 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc1:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_activas:
            return "si"
    return "no"

# Funcion para procesar un texto y verificar si contiene palabras desactivas
def contiene_palabras_desactivas(texto):
    # Array de palabras activas
    palabras_desactivas = ["desactiva", "desactivo", "desactivos", "desactivas","desahabilitado","desahabilitados"]
    # Procesar el texto con spaCy
    doc2 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc2:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_desactivas:
            return "si"
    return "no"

# Funcion para procesar un texto y verificar si contiene palabras desactivas
def contiene_palabras_sexo_varon(texto):
    # Array de palabras activas
    palabras_desactivas = ["masculino", "hombre", "varon", "machos","varones","masculinos","hombres","macho","m"]
    # Procesar el texto con spaCy
    doc2 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc2:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_desactivas:
            return "no"
    return "si"

# Funcion para procesar un texto y verificar si contiene palabras desactivas
def contiene_palabras_sexo_mujer(texto):
    # Array de palabras activas
    palabras_desactivas = ["mujer","mujeres","femenino","femeninos","señorita","señoritas","hembra","hembras","f"]
    # Procesar el texto con spaCy
    doc2 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc2:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_desactivas:
            return "no"
    return "si"


def palabras_departamento(texto):
    # Lista de nombres de departamentos que pueden consistir en múltiples tokens

    # Array de palabras activas
    departamentos = ["la paz", "santa cruz","oruro", "pando", "potosi", "sucre", "cochabamba", "chuquisaca", "tarija"]
    # Procesar el texto con spaCy
    doc2 = nlp(texto)
    # Si ninguna secuencia forma un nombre de departamento múltiple, buscar si hay nombres de departamento únicos
    for token in doc2:
        if token.text in departamentos:
            return token.text  # Devuelve el departamento encontrado
    return "no"


def palabras_provincia(texto):
    # Array para almacenar todas las provincias de Bolivia
    provincias = ["azurduy","juana","oropeza","tomina", "yamparaez", "zudañez","arani", "arque", "ayopaya", "capinota",
    "carrasco", "chapare","mizque", "punata", "quillacollo", "tapacari", "tiraque","aroma","caranavi","Ingavi", "inquisivi",
    "larecaja", "loayza", "muñecas", "omasuyos", "pacajes","atahuallpa", "cercado", "litoral","poopo", "sabaya", "sajama",
    "saucari","abuna","manuripi","chiquitos", "cordillera", "florida", "guarayos", "ichilo",
                    "vallegrande","cercado", "oconnor", "padcaya"]
    provincias_mul = ["belisario boeto","hernando siles","jaime zudañez","azurduy de padilla","luis calvo","nor cinti",
    "sud cinti","esteban arce","german jordan","Narciso Campero","abel Iturralde","bautista saavedra","eliodoro camacho",
    "franz tamayo","gualberto villarroel","jose manuel pando","los andes","manco kapac","nor yungas","pedro domingo murillo",
    "sud yungas","eduardo abaroa","eduardo avaroa","nor Carangas","pantaleon dalence","san pedro de totora","sebastian pagador","sud carangas",
     "federico roman","madre de dios","nicolas suarez","alonso de ibañez", "antonio quijarro", "bernardino bilbao", "charcas",
     "chayanta", "cornelio saavedra","daniel campos", "enrique baldivieso", "jose maria linares", "modesto Omiste", "nor chichas",
        "nor lipez", "rafael bustillo", "sud chichas", "sud lipez", "tomas frias","andres ibañez", "angel sandoval",
        "ignacio warnes", "jose miguel de velasco", "ñuflo de chavez", "obispo santistevan", "ñuflo de chavez",
            "ñuflo de chavez","aniceto arce", "burdett o connor","burdett oconnor","eustaquio mendez", "gran chaco",
             "jose maria aviles",
                               "o connor","sanchez de ocaña", "tomas barron"]
    # Procesar el texto con spaCy
    doc4 = nlp(texto)
    # Obtener todas las secuencias de tokens en el texto
    secuencias = [doc4[i:j].text for i in range(len(doc4)) for j in range(i + 1, len(doc4) + 1)]
    # Iterar sobre las secuencias de tokens
    for secuencia in secuencias:
        # Verificar si la secuencia forma parte de un nombre de departamento múltiple
        if secuencia in provincias_mul:
            return secuencia
    # Si ninguna secuencia forma un nombre de departamento múltiple, buscar si hay nombres de departamento únicos
    for token in doc4:
        if token.text in provincias:
            return token.text  # Devuelve el departamento encontrado
    return "no"


vec_nombre = ["aaron","abdon","abel","abelardo","abrahan","absalon","acacio","adalberto","adan","adela","adelaida","adolfo","adon","adrian","agustin",
"aitor","alba","albert","alberto","albina","alejandra","alejandro","alejo","alfonso","alfredo","alicia","alipio","almudena","alonso","alvaro",
"amadeo","amaro","ambrosio","amelia","amparo","ana","ananias","anastasia","anatolio","andrea","andres","angel","angela","angeles","aniano",
"anna","anselmo","antero","antonia","antonio","aquiles","araceli","aranzazu","arcadio","aresio","ariadna","aristides","arnaldo","artemio","arturo",
"ascension","asuncion","atanasio","augusto","aurea","aurelia","aureliano","aurelio","aurora","baldomero","balduino","baltasar","barbara","bartolome","basileo",
"beatriz","begoña","belen","beltran","benedicto","benigno","benito","benjamin","bernabe","bernarda","bernardo","blanca","blas","bonifacio","borja",
"bruno","calixto","camilo","candida","carina","carlos","carmelo","carmen","carolina","casiano","casimiro","casio","catalina","cayetano","cayo",
"cecilia","ceferino","celia","celina","celso","cesar","cesareo","cipriano","cirilo","cirino","ciro","clara","claudia","claudio","cleofas",
"clotilde","colombo","columba","columbano","concepcion","conrado","constancio","constantino","consuelo","cosme","cristian","cristina","cristobal","daciano","dacio",
"damaso","damian","daniel","dario","david","democrito","diego","dimas","dolores","domingo","donato","dorotea","edgar","edmundo","eduardo",
"eduvigis","efren","elena","elias","elisa","eliseo","elvira","emilia","emiliano","emilio","encarnacion","enrique","epifania","erico","ernesto",
"esdras","esiquio","esperanza","esteban","ester","esther","eugenia","eugenio","eulalia","eusebio","eva","evaristo","ezequiel","fabian","fabio",
"fabiola","facundo","fatima","faustino","fausto","federico","feliciano","felipe","felix","fermin","fernando","fidel","fortunato","francesc","francisca",
"francisco","fulgencio","gabriel","gema","genoveva","gerardo","german","gertrudis","gisela","gloria","godofredo","gonzalo","gregorio","guadalupe","guido",
"guillermo","gustavo","guzman","hector","heliodoro","heraclio","heriberto","hilarion","hildegarda","homero","honorato","honorio","hugo","humberto","ifigenia",
"ignacio","ildefonso","ines","inmaculada","inocencio","irene","ireneo","isaac","isabel","isaias","isidro","ismael","ivan","jacinto","jacob",
"jacobo","jaime","jaume","javier","jeremias","jeronimo","jesus","joan","joaquim","joaquin","joel","jonas","jonathan","jordi","jorge",
"josafat","jose","josefa","josefina","josep","josue","juan","juana","julia","julian","julio","justino","juvenal","ladislao","laura",
"laureano","lazaro","leandro","leocadia","leon","leonardo","leoncio","leonor","leopoldo","lidia","liduvina","lino","lorena","lorenzo","lourdes",
"lucano","lucas","lucia","luciano","lucrecia","luis","luisa","luz","macario","magdalena","manuel","manuela","mar","marc","marcelino",
"marcelo","marcial","marciano","marcos","margarita","maria","mariano","marina","mario","marta","martin","mateo","matias","matilde","mauricio",
"maximiliano","melchor","mercedes","miguel","milagros","miqueas","miriam","mohamed","moises","monica","montserrat","narciso","natalia","natividad","nazario",
"nemesio","nicanor","nicodemo","nicolas","nicomedes","nieves","noe","noelia","norberto","nuria","octavio","odon","olga","onesimo","orestes",
"oriol","oscar","oscar","oseas","oswaldo","otilia","oto","pablo","pancracio","pascual","patricia","patricio","paula","pedro","petronila",
"pilar","pio","poncio","porfirio","primo","priscila","probo","purificacion","rafael","raimundo","ramiro","ramon","raquel","raul","rebeca",
"reinaldo","remedios","renato","ricardo","rigoberto","rita","roberto","rocio","rodrigo","rogelio","roman","romualdo","roque","rosa","rosalia",
"rosario","rosendo","ruben","rufo","ruperto","salome","salomon","salvador","salvio","samuel","sandra","sanson","santiago","sara","sebastian",
"segismundo","sergio","severino","silvia","simeon","simon","siro","sixto","sofia","soledad","sonia","susana","tadeo","tarsicio","teodora",
"teodosia","teofanes","teofila","teresa","timoteo","tito","tobias","tomas","tomas","toribio","trinidad","ubaldo","urbano","ursula","valentin",
"valeriano","vanesa","velerio","venancio","veronica","vicenta","vicente","victor","victoria","victorino","victorio","vidal","virgilio","virginia","vladimiro",
"wilfredo","xavier","javier","yolanda","zacarias","zaqueo","limbert","limberth","limber","wilmer","gladis","gladys","gladdys","gladdis","edilma","dilma",
"wilson","wilma","alison","alice","nelson","eleuterio","israel","martha","geraldine","rosaura","rosamari","elisabet","elizabet","romina","raymi","yerlan","yerco",
"irma","isa","estefania","silvana","silvio","mary","mari","roxana","napoleon","leonarda","jhobana","jhovana","jhannet","jhanet","jhanneth","jhoselin","joselin",
"britani","britany","anastasio","magali","miguilina","cosio","reymundo","valeria","valerio","tania","victorio","lux","luz clara","luz","clara",
"brulefes","vismar","melisa","braulio","bacilio","jhonny","jhofan","edi","yesica","jesica","yessica","jessica","leyna","leina","juan pablo","virginia",
"raul","pablo","yanine","susan","nicol","pamela","ilda","hilda","shirley","ana","maicol","ivana","adriana"
]
def encontrar_nombre(texto):
    # Procesar el texto con spaCy
    doc5 = nlp(texto)
    for token in doc5:
        if token.text in vec_nombre:
            return token.text  # Devuelve el departamento encontrado
    return "no"

vec_apellidos = ["aguilar","alonso","alvarez","arias","benitez","blanco","blesa","bravo","caballero","cabrera","calvo","cambil","campos","cano","carmona",
"carrasco","castillo","castro","cortes","crespo","cruz","delgado","diaz","diez","dominguez","duran","esteban","fernandez","ferrer","flores",
"fuentes","gallardo","gallego","garcia","garrido","gil","gimenez","gomez","gonzalez","guerrero","gutierrez","hernandez","herrera","herrero","hidalgo",
"ibañez","iglesias","jimenez","leon","lopez","lorenzo","lozano","marin","marquez","martin","martinez","medina","mendez","molina","montero",
"montoro","mora","morales","moreno","moya","muñoz","navarro","nieto","nuñez","ortega","ortiz","parra","pascual","pastor","peña",
"perez","prieto","ramirez","ramos","rey","reyes","rodriguez","roman","romero","rubio","ruiz","saez","sanchez","santana","santiago",
"santos","sanz","serrano","soler","soto","suarez","torres","vargas","vazquez","vega","velasco","vicente","vidal","canaviri","ayaviri",
"lipiri","villca","villcaes","villcaez","torrico","titi","pacheco","lima","camiño","mitma","condori","mamani","quispe","sierra","acarapi",
"lia","huanca","colquillo","huallpa","wallpa","cosio","ayala","galindo","quispia","chaca","achacollo","gallo","romero","jorge","zeballos","chura",
"michaga","copatiti","acha","fernandes","cayo","coyo","medrano","porco","castillo","humeres","humerez","alizon","chambi","toledo","calani","charali",
"victorio","choque","huayllani","adam","tola","sola","acebedo","jani jani","janijani","salinas","luna","dias","diaz","jurado",
"callahuara","lopes","lopez"]
def encontrar_apellido(texto):
    apellidos_encontrados = []
    doc2 = nlp(texto)
    # Verificar si algún apellido está presente en el texto
    for token in doc2:
        if token.text in vec_apellidos:
            apellidos_encontrados.append(token.text)

    if apellidos_encontrados:
        return apellidos_encontrados
    else:
        return "no"

def obtener_area(texto):
    doc2 = nlp(texto)
    area_keywords = ["tecnologia", "salud", "social"]
    indice_keywords = [1, 2, 3]
    area = []

    # Procesar el texto con el modelo de SpaCy
    # Buscar palabras clave asociadas con áreas en el texto
    for token in doc2:
        if token.text in area_keywords:
            index = area_keywords.index(token.text)
            id = indice_keywords[index]
            area.append(id)

    return area

def palabra_desercion(texto):  # Suponiendo que eliminar_tildes(texto) está definida
    des_keywords = ["desercion", "desertados", "abandonados", "abandono", "abandonaron", "desertaron", "retiraron", "retirados", "desertaron"
    ,"desertores"]
    doc2 = nlp(texto)
    for palabra_clave in doc2:
        if palabra_clave.text in des_keywords:
            return "si"
    return "no"

def palabra_aplazaron(texto): # Suponiendo que eliminar_tildes(texto) está definida
    apla_keywords = ["aplazaron","aplasados","aplazados", "reprobados", "reprobaron","aplazar"]
    doc2 = nlp(texto)
    for palabra_clave in doc2:
        if palabra_clave.text in apla_keywords:
            print(palabra_clave.text)
            return "si"
    return "no"
def palabra_aprobados(texto): # Suponiendo que eliminar_tildes(texto) está definida
    apla_keywords = ["aprobados","aprobado"]
    doc2 = nlp(texto)
    for palabra_clave in doc2:
        if palabra_clave.text in apla_keywords:
            return "si"
    return "no"

def palabra_curso(texto): # Suponiendo que eliminar_tildes(texto) está definida
    apla_keywords = ["curso","cursos","grado","grados"]
    doc2 = nlp(texto)
    for palabra_clave in doc2:
        if palabra_clave.text in apla_keywords:
            return "si"
    return "no"
def obtener_que_curso_quiere(texto):# Suponiendo que eliminar_tildes(texto) está definida
    curso_keywords = ["1","1er año","1er","1ro","primero","primer","primer año","2","2do año","2do","segundo",
    "segundo año","3","3er","3er año","3ro","tercero","tercer año","tercer","4","4to","4to año","cuarto","cuarto año","5","5to",
    "5to año","quinto","quinto año","5to"]
    id_curso = ["1","1","1","1","1","1","1","2","2","2","2","2","3","3","3","3","3","3","3",
    "4","4","4","4","4","5","5","5","5","5","5"]
    curso=[]
    doc2 = nlp(texto)
    for token in doc2:
        if token.text in curso_keywords:
            index = curso_keywords.index(token.text)
            id = id_curso[index]
            curso.append(id)
    return curso


def palabra_nota(texto): # Suponiendo que eliminar_tildes(texto) está definida
    apla_keywords = ["calificacion","nota","calificaciones","notas"]
    doc2 = nlp(texto)
    for palabra_clave in doc2:
        if palabra_clave.text in apla_keywords:
            return "si"
    return "no"



fecha_regex = re.compile(
    r'\b(?:\d{1,2}[-/.\s]?\d{1,2}[-/.\s]?\d{2,4})\b|'  # dd/mm/aaaa, dd-mm-aaaa, dd.mm.aaaa
    r'\b(?:\d{4}[-/.\s]?\d{1,2}[-/.\s]?\d{1,2})\b|'    # aaaa/mm/dd, aaaa-mm-dd, aaaa.mm.dd
    r'\b(?:\d{1,2} (?:de )?(?:ene(?:ro)?|feb(?:rero)?|mar(?:zo)?|abr(?:il)?|may(?:o)?|jun(?:io)?|jul(?:io)?|ago(?:sto)?|sep(?:tiembre)?|oct(?:ubre)?|nov(?:iembre)?|dic(?:iembre)?) (?:de )?\d{2,4})\b'  # dd de mes de aaaa
)

def fechas(texto):
    fechas_encontradas = fecha_regex.findall(texto)
    c = 0
    fecha_e = []
    if len(fechas_encontradas) == 1:
        if es_entero(fechas_encontradas[0]):#si la fecha es un entero
            fecha_e.append(fechas_encontradas[0]+"-01-01")
            fecha_e.append(fechas_encontradas[0]+"-12-30")
        else:
            newFecha = formatear_fecha(fechas_encontradas[0])
            soloAno = formatear_fecha_solo_ano(newFecha)
            fecha_e.append(soloAno+"-01-01")
            fecha_e.append(soloAno+"-12-30")
    elif len(fechas_encontradas) >1:
        for fe in fechas_encontradas:
            if es_entero(fe):#si la fecha es un entero
                if c == 0:
                    fecha_e.append(fe+"-01-01")
                if c == 1:
                    fecha_e.append(fe+"-12-30")
            else:#no es estero puede que la fecha se asi 01/01/2025 y tenemos que cambiar a esto 01-01-2025
                fecha_e.append(formatear_fecha(fe))
            c = c + 1
    return fecha_e

def es_entero(cadena):
    return cadena.isdigit()

def formatear_fecha(fecha):
    # Separar la fecha en sus componentes (día, mes, año)
    if '/' in fecha:
        partes = fecha.split('/')
    elif '-' in fecha:
        partes = fecha.split('-')
    else:
        partes = fecha.split('.')
    # Reordenar los componentes para el formato deseado (año, mes, día)
    if len(partes) == 3:
        return partes[2] + '-' + partes[1] + '-' + partes[0]
    else:
        return fecha

def obtener_ano(texto):
    fechas_encontradas = fecha_regex.findall(texto)
    fecha_e = []
    for fe in fechas_encontradas:
        if not es_entero(fe):#si la fecha es un entero
            fecha_e.append(formatear_fecha_solo_ano(fe))
        else:
            fecha_e.append(fe)
    return fecha_e
#funciones de allar el dato si exite o no
def formatear_fecha_solo_ano(fecha):
    # Separar la fecha en sus componentes (día, mes, año)
    if '/' in fecha:
        partes = fecha.split('/')
    elif '-' in fecha:
        partes = fecha.split('-')
    else:
        partes = fecha.split('.')
    # Reordenar los componentes para el formato deseado (año, mes, día)
    if len(partes) == 3:
        return partes[2]
    else:
        return "2024"
def obtener_ano_de_fecha(fecha):
    # Separar la fecha en sus componentes (día, mes, año)
    if '/' in fecha:
        partes = fecha.split('/')
    elif '-' in fecha:
        partes = fecha.split('-')
    else:
        partes = fecha.split('.')
    # Reordenar los componentes para el formato deseado (año, mes, día)
    return partes[0]


def obtener_areas_id(texto):
    # Definir áreas y sus IDs correspondientes
    areas = ['tecnologia', 'técnologia','tecno','tecnologi', "tecnologia", "salud", "salud",'salu', "social", "sociales",'soci','socia']
    id_areas = [1, 1, 1, 1, 1, 2,2, 2, 3, 3,3,3]
    # Cargar el modelo de spaCy (asegúrate de tenerlo instalado y cargado adecuadamente)
    nlp = spacy.load("es_core_news_sm")
    # Procesar el texto con el modelo de spaCy
    doc = nlp(texto)
    # Lista para almacenar los IDs de las áreas encontradas en el texto
    new_areas = []
    # Iterar sobre cada token en el documento procesado por spaCy
    for token in doc:
        # Verificar si el texto del token está presente en la lista de áreas
        if token.text in areas:
            # Obtener el índice correspondiente en 'areas' y agregar el ID correspondiente
            index = areas.index(token.text)
            new_areas.append(id_areas[index])

    return new_areas
def seleccionarMateriasTodo_Partido(limit):
    resul = seleccionarAsignaturaTodos()
    vec = []
    codigos = []
    otro = []
    for fila in resul:
        vec1 = []
        pal = unidecode(fila[1].lower())#convertir a minuscula y quitar tildes
        palabras = filtraremos(pal)#filtramos
        for pala in palabras:
            vec1.append(pala)
            if len(pala)>=4:
                for i in range(1, len(pala)):
                    if len(pala[:-i]) == limit:
                        break;
                    vec1.append(pala[:-i])
        vec.append(vec1)
        otro.append(palabras)
        codigos.append(fila[0])
    return vec,codigos,otro

def seleccionarMateriasTodo_Partido_otro(limit):
    resul = seleccionarAsignaturaTodos()
    vec = []
    codigos = []
    otro = []
    for fila in resul:
        vec1 = []
        pal = unidecode(fila[1].lower())  # convertir a minúscula y quitar tildes
        palabras = tokenizar(pal)  # filtramos
        for pala in palabras:
            vec1.append(pala)
            if len(pala) >= 4:
                for i in range(1, len(pala)):
                    if len(pala[:-i]) == limit:
                        break
                    vec1.append(pala[:-i])
        vec.append(vec1)
        otro.append(palabras)
        codigos.append(fila[0])
    return vec, codigos, otro
#print(materias)
#funcion para filtrar eliminando del el las los la de etc
def filtraremos(pal):
    doc = nlp(pal)
    palabras_filtradas = [token.text for token in doc if not token.is_stop and not token.is_space ]
    return palabras_filtradas
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

def tokenizar(texto,texto_sin_nada):
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
            token.text not in texto_sin_nada and
           not token.is_space]

    return palabras_filtradas

def eliminar_posiciones(posiciones,usuario):
    usuario1 = [item for idx, item in enumerate(usuario) if idx not in posiciones]
    return usuario1

def obtener_id_materia(texto,texto_sin_nada):
    limite_derivacion = 3  # ejemplo si tengo 1=fisica 2=fisic,3=fisi
    vec, codigos, otro = seleccionarMateriasTodo_Partido(limite_derivacion)
    palabras_claves = tokenizar(texto,texto_sin_nada)
    asignaturas = otro
    #print("palabras claves =================================")
    #print(palabras_claves)
    #print("===================================")
    #print(asignaturas)
    # Convertir las listas de palabras en cadenas de texto
    asignaturas_texto = [' '.join(asignatura) for asignatura in asignaturas]

    # Agregar el texto del usuario a las asignaturas
    documentos = asignaturas_texto + [' '.join(palabras_claves)]

    # Calcular la matriz TF-IDF
    vectorizer = TfidfVectorizer().fit_transform(documentos)
    similitudes = cosine_similarity(vectorizer[-1], vectorizer[:-1])

    # Ordenar las asignaturas por similitud
    asignaturas_ordenadas = sorted(zip(codigos, asignaturas, similitudes[0]), key=lambda x: x[2], reverse=True)
    umbral = 0.5
    asignaturas_mencionadas = []
    for codigo, asignatura, similitud in asignaturas_ordenadas:
        # Si la similitud es mayor que un umbral, considera que la asignatura está mencionada
        if similitud >=umbral:  # Ajusta este umbral según sea necesario
            asignaturas_mencionadas.append((codigo, ' '.join(asignatura), similitud))

    # Imprimir todas las asignaturas mencionadas
    codigos_encontrado = []
    for codigo, asignatura, similitud in asignaturas_mencionadas:
        print(f"Código: {codigo}, Asignatura: {asignatura}, Similitud: {similitud:.2f}")
        codigos_encontrado.append(codigo)
    return codigos_encontrado  # Suponiendo que los índices coinciden con los códigos


def seleccionar_si_quiere_por_area_o_carrera(texto):
    # Definir áreas y sus IDs correspondientes
    bus = ['area', 'areas','are','carrera', "carreras", "carre"]
    relacion = [1,1,1,2,2,2]
    # Cargar el modelo de spaCy (asegúrate de tenerlo instalado y cargado adecuadamente)
    nlp = spacy.load("es_core_news_sm")
    # Procesar el texto con el modelo de spaCy
    doc = nlp(texto)
    # Lista para almacenar los IDs de las áreas encontradas en el texto
    new = []
    # Iterar sobre cada token en el documento procesado por spaCy
    for token in doc:
        # Verificar si el texto del token está presente en la lista de áreas
        if token.text in bus:
            # Obtener el índice correspondiente en 'areas' y agregar el ID correspondiente
            index = bus.index(token.text)
            new.append(relacion[index])

    return new
