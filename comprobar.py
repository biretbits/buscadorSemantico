import spacy
import unicodedata
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Cargar el modelo de lenguaje en español
nlp = spacy.load("es_core_news_sm")

def eliminar_tildes(texto):
    # Utilizamos la libreria unicodedata para eliminar las tildes
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
    texto = texto.lower();
    # Tokenizar el texto en palabras
    tokens = word_tokenize(texto)

    # Etiquetar partes del habla
    tagged_tokens = pos_tag(tokens)

    # Buscar tokens etiquetados como números (CD: cardinal numbers)
    numeros = [token[0] for token in tagged_tokens if token[1] == 'CD']

    return numeros

# Funcion para procesar un texto y verificar si contiene palabras activas
def contiene_palabras_activas(texto):
    texto = texto.lower();
    # array de palabras activas
    palabras_activas = ["activa", "activo", "activos", "activas","habilitado","habilitados"]
    # Procesar el texto con spaCy
    doc1 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc1:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_activas:
            return True
    return False

# Funcion para procesar un texto y verificar si contiene palabras desactivas
def contiene_palabras_desactivas(texto):
    texto = texto.lower();
    # Array de palabras activas
    palabras_desactivas = ["desactiva", "desactivo", "desactivos", "desactivas","desahabilitado","desahabilitados"]
    # Procesar el texto con spaCy
    doc2 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc2:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_desactivas:
            return True
    return False

# Funcion para procesar un texto y verificar si contiene palabras desactivas
def contiene_palabras_sexo_varon(texto):
    texto = texto.lower();
    # Array de palabras activas
    palabras_desactivas = ["masculino", "hombre", "varon", "machos","varones","masculinos","hombres","macho","m"]
    # Procesar el texto con spaCy
    doc2 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc2:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_desactivas:
            return True
    return False

# Funcion para procesar un texto y verificar si contiene palabras desactivas
def contiene_palabras_sexo_mujer(texto):
    texto = texto.lower();
    # Array de palabras activas
    palabras_desactivas = ["mujer","mujeres","femenino","femeninos","señorita","señoritas","hembra","hembras","f"]
    # Procesar el texto con spaCy
    doc2 = nlp(texto)
    # Iterar sobre los tokens
    for token in doc2:
        # Verificar si el token esta en el array de palabras activas
        if token.text in palabras_desactivas:
            return True
    return False


def palabras_departamento(texto):
    texto = texto.lower()
    # Lista de nombres de departamentos que pueden consistir en múltiples tokens
    departamentos_multiples = ["la paz", "santa cruz"]
    # Array de palabras activas
    departamentos = ["oruro", "pando", "potosi", "sucre", "cochabamba", "chuquisaca", "tarija"]
    # Procesar el texto con spaCy
    doc3 = nlp(texto)
    # Obtener todas las secuencias de tokens en el texto
    secuencias = [doc3[i:j].text for i in range(len(doc3)) for j in range(i + 1, len(doc3) + 1)]
    # Iterar sobre las secuencias de tokens
    for secuencia in secuencias:
        # Verificar si la secuencia forma parte de un nombre de departamento múltiple
        if secuencia in departamentos_multiples:
            return secuencia
    # Si ninguna secuencia forma un nombre de departamento múltiple, buscar si hay nombres de departamento únicos
    for token in doc3:
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

    texto = texto.lower()

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
    texto = texto.lower()

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
"victorio","choque","huayllani","adam","tola","sola","acebedo","jani jani","janijani","salinas","luna","diaz","jurado"]
def encontrar_apellido(texto):
    texto = texto.lower()
    apellidos_encontrados = []

    # Procesar el texto con spaCy
    doc = nlp(texto)

    # Verificar si algún apellido está presente en el texto
    for token in doc:
        if token.text in vec_apellidos:
            apellidos_encontrados.append(token.text)

    if apellidos_encontrados:
        return apellidos_encontrados
    else:
        return "no"
