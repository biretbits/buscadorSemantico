import spacy
import nltk
import pymysql
from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter,contiene_palabras_activas,contiene_palabras_desactivas,contiene_palabras_sexo_varon,contiene_palabras_sexo_mujer
from comprobar import palabras_departamento,palabras_provincia,encontrar_nombre,encontrar_apellido,obtener_area,palabra_desercion
from comprobar import palabra_aplazaron,palabra_aprobados,palabra_curso,obtener_que_curso_quiere
from comprobar import palabra_nota,fechas,obtener_ano,obtener_areas_id,obtener_id_materia
from comprobar import seleccionar_si_quiere_por_area_o_carrera
from sql import seleccionar_estudiante1,seleccionar_consultasEmbeddings,seleccionar_respuesta_y_consulta,seleccionarTodoPalabraClaves,seleccionarAsignaturaTodos
from sql import seleccionarTodoClaves,seleccionarTodoPalabraClaves_id
from sentence_transformers import SentenceTransformer, util
import numpy as np
from datetime import datetime
from comprobar import obtener_ano_de_fecha
from sklearn.metrics.pairwise import cosine_similarity

from unidecode import unidecode
from nltk.corpus import wordnet as wn


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#nltk.download('omw-1.4')
# Cargar el modelo pre-entrenado
model = SentenceTransformer('all-MiniLM-L6-v1')
nlp = spacy.load("es_core_news_sm")
#model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
#e.estado = 'desactivo' or e.cod_area = 3 and e.sexo = 'femenino' or  e.sexo = 'masculino';"
consultas_aux= {"activo_es" :" e.estado = 'activo'",
"desactivo_es":" e.estado = 'desactivo'",
"sexo_es_f" :" e.sexo = 'femenino'",
"sexo_es_m":"  e.sexo = 'masculino'",
"departamento_es":" e.departamento = '{}'",
"provincia_es":" e.provincia = '{}'",
"nombre_es":"  e.nombre_es = '{}' ",
"apellido_p_es":"  e.ap_es = '{}' ",
"apellido_m_es":"  e.am_es = '{}' ",
"nombre_carrera":" e.cod_carrera = {}",

"nombre_es_especifico":" e.nombre_es = '{}' ",
"apellido_p_es_especifico":" e.ap_es = '{}' ",
"apellido_m_es_especifico":" e.am_es = '{}' ",

"activo_es_unsxx" :" e.estado = 'activo' ",
"desactivo_es_unsxx":" e.estado = 'desactivo' ",
"sexo_es_f_unsxx" :" e.sexo = 'femenino' ",
"sexo_es_m_unsxx":" e.sexo = 'masculino' ",
"departamento_es_unsxx":" e.departamento = '{}' ",
"provincia_es_unsxx":" e.provincia = '{}'",
"nombre_carrera":" e.cod_carrera = {} ",
"cod_area":" c.cod_area = {}",
"cod_area_cursa":" e.cod_area = {}",
"desercion":" abandono = '{}'",
"aplazaron":" estado_ano = '{}'",
"curso_estudiante":" ep.cod_grado = {}",
"id_carrera":" cod_carrera = {}",
"id_estudiante": "cod_es = {}",
"id_grado": "cod_grado = {}",
"fechai": " fecha >= '{}'",
"fechaf": " fecha <= '{}'",
}


#"nombre_es":" and e.nombre_es like '%{}%' ",
#"apellido_p_es":" and e.ap_es like '%{}%' ",
#"apellido_m_es":" and e.am_es like '%{}%' ",

# Función para preprocesar y tokenizar el texto



def maximo(resultado_tensor):
    k = 0
    j = 0
    max = 0
    for score in resultado_tensor:
        if score > max:
            max = score
            j = k
        k = k + 1
    return j

def obtener_embedding(texto,posible_respuesta):
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "SELECT embedding,id FROM embeddings WHERE texto = %s and estado='activo'"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta, (texto))

    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener el embedding de la consulta
        result = cursor.fetchone()
        embedding_str = result[0]
        codigo = result[1]
        # Convertir la cadena de texto del embedding a un array numpy

        print(posible_respuesta," posible res")
        try:
            with conn.cursor() as cursor:
                if posible_respuesta:
                    sql_update = "UPDATE embeddings SET cod_respuesta = %s WHERE id = %s"
                    cursor.execute(sql_update, (posible_respuesta, codigo))
            # Confirmar la transacción
            conn.commit()
        finally:
            # Cerrar la conexión siempre, incluso si ocurre una excepción
            conn.close()
        embedding = np.frombuffer(embedding_str, dtype=np.float32)

        return embedding
    else:
        texto_embedding = model.encode(texto)
        # Convertir el embedding a bytes
        embedding_bytes = texto_embedding.tobytes()
        # Insertar el texto y el embedding en la base de datos
        # Si no se encuentra el embedding, calcularlo con el modelo
        if posible_respuesta != '':
            sql_insert = "INSERT INTO embeddings (texto, embedding, cod_respuesta) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (texto, embedding_bytes, posible_respuesta))
        else:
            sql_insert = "INSERT INTO embeddings (texto, embedding) VALUES (%s, %s)"
            cursor.execute(sql_insert, (texto, embedding_bytes))

        conn.commit()
        return texto_embedding

def seleccionarEmbeddinBd():
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "SELECT cod_respuesta,embedding,texto FROM embeddings WHERE cod_respuesta is not null"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)
    embeddings = []
    codigos = []
    texto = []
    # Obtener todos los embeddings y códigos de asignatura
    for row in cursor.fetchall():
        codigos.append(row[0])
        embeddings.append(np.frombuffer(row[1], dtype=np.float32))  # Convertir el blob a un array numpy
        texto.append(row[2])
    return codigos,embeddings,texto


def eliminar_tildes(texto):
    return unidecode(texto)

def seleccionarMaterias():
    resul = seleccionarAsignaturaTodos()
    vec = []
    for fila in resul:
        pal = eliminar_tildes(fila[1].lower())
        palabras = pal.split()
        vec.extend(palabras)
    return vec
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
tambien_no_tomar = ['año','ano','gestion','gestio','gesti']
otros_no_tomar = ['unsxx','universidad','nacional','siglo','xx','universi','naciona']
palabras_tomar_encuenta = ['a','de']#antes de eliminar tambien estas palabras de apoyo se toma como palabras claves
no_afecta_al_texto = ['a','de']#existen en palabras claves ya que ayuda a otros
#textos a mejorar sus respuesta, pero ademas en otros textos no afecta
def filtrar(texto):
    materias = seleccionarMaterias()
    #print(materias)
    doc = nlp(texto)
    palabras_filtradas = [
        token.text for token in doc
        if not token.is_stop and
           not token.text.isdigit() and
           not isinstance(token.text, int) and
           token.text not in tambien_no_tomar and
           token.text not in carreras_no_tomar and
           token.text not in areas_no_tomar and
           token.text not in otros_no_tomar and
           not token.is_space and
           token.text not in materias]
    for palabra in palabras_tomar_encuenta:
        if palabra in texto.split():
            palabras_filtradas.append(palabra)

    return palabras_filtradas

def sinonimos(palabra):
    claves,cod_agrupar = seleccionarTodoClaves()
    nuevo = []
    otro = []
    derivar = ['dos','on','do','damente','as','an','iamos','ias','ia','e','is','iais','ais','mos','s']
    for pa in palabra:
        # Buscar sinónimos en WordNet
        nuevo1 = []
        sinonimos = []
        if pa in claves:#existe la palabra en las claves si o no
            posicion = claves.index(pa)
            # Obtener el valor correspondiente en el vector valores usando la posición
            id = cod_agrupar[posicion]
            pal_claves = seleccionarTodoPalabraClaves_id(id)
            print(pal_claves)
            for p_c in pal_claves:
                nuevo.append(p_c)
                nuevo1.append(p_c)
        nuevo.append(pa)
        nuevo1.append(pa)
        for synset in wn.synsets(pa, lang='spa'):
            for lemma in synset.lemmas(lang='spa'):
                nuevo.append(lemma.name())
                nuevo1.append(lemma.name())
                sinonimos.append(lemma.name())
        # Agregar variantes flexionadas basadas en reglas simples (puedes expandir estas reglas según tus necesidades)
        #print(sinonimos,"      ",pa)
        for sino in sinonimos:
            for de in derivar:
                nuevo.append(sino + de)
                nuevo1.append(sino + de)

        doc = nlp(pa)
        raiz = doc[0].lemma_
        if raiz:
            nuevo.append(raiz)
            for de in derivar:
                nuevo.append(raiz + de)
                nuevo1.append(raiz + de)
        # Agregar más formas flexionadas según las reglas
        # Combinar sinónimos y variantes flexionadas
        if len(pa)>=4:
            for i in range(1, len(pa)):
                nuevo.append(pa[:-i])
                nuevo1.append(pa[:-i])
                if len(pa[:-i])==4:
                    break

        otro.append(nuevo1)
    return nuevo,otro

def clasificando(diccionario,top_10_textos,top_10_codigos,sino,claves,posiciones,materias_user):
    vec_suma = [0]*len(top_10_textos)
    #vec_id = [0]*len(top_10_textos)
    # Imprimir los resultados o hacer lo que necesites con ellos
    j = 0
    for pal in diccionario:
        descartar = []
        encontrados = []
        contar_cor = 0
        contar_des = 0
        for pa in pal:
            if pa in sino:
                contar_cor+=1
                if pa in claves:
                    encontrados.append(pa)
            else:
                if pa in claves:
                    descartar.append(pa)
        print(j, "  =  ",pal,'pal',contar_cor," contar",len(descartar)," = des")
        
        if contar_cor > 0 and len(descartar) == 0:
            print("llego 1")
            if(len(materias_user)>0):
                si_mater = obtener_id_materia(top_10_textos[j],pal)
                if(len(si_mater)>0):
                    vec_suma[j]+=contar_cor 
            else:
                vec_suma[j]+=contar_cor
        else:
            #si en el pal que es de los 20 semanticas ['cantidad','estudiantes','de'] si hay palabras claves
            #al recorrer las 20 similitudes, ademas de contar si tienes palabras similares y no similares con el texto del usuario
            #tambien contamos y guardamos las palabras similares si existe en palabras claves y se fuarda en encontrados
            if len(encontrados) == len(posiciones):#si son iguales
                if len(descartar) > 0:
                    for des in descartar:
                        if des in no_afecta_al_texto:#palabra clave descartar hay en palabras claves que no afectan
                            contar_des+=1
                if contar_des > 0:
                    if(len(materias_user)>0):
                        si_mater = obtener_id_materia(top_10_textos[j],pal)
                        if(len(si_mater)>0):
                            vec_suma[j]+=contar_cor 
                    else:
                        vec_suma[j]+=contar_cor
                    print('llego')
                print("llego 2")
        j += 1
    return vec_suma


def obtener_palabras_claves_del_texto_usuario(otro,palabras_filtradas,claves):
    posiciones = []
    k = 0
    #recorremos las palabras filtradas del usuario
    for pa in palabras_filtradas:
        if pa in claves:#verificamos si la palabra existe en palabras claves
            posiciones.append(k)#si existe guardamos la posicion de la coencidencia
        k=k+1
        #creamos dos nuevos vectores para un nuevo recorrido
    #recorremo las posiciones obtenidas
    resultado = []
    #al recorrer obtenemos de la posicion obtenida las derivaciones y sinonimos de la palabra encontrado en palabras claves
    for posi in posiciones:
        resultado.extend(otro[posi])#guardamos todos las derivaciones de la palabra clave que se encontro en el texto del usuario

    return resultado,posiciones

def clasificacando_por_segunda_ves(vec_new_id,vec_new_text,otro,claves,palabras_filtradas,resultado):

    vec_contar = [0]*len(vec_new_text)
    vec_new_ids = [0]*len(vec_new_text)
    kk = 0
    for palabra in vec_new_text:
        contar = 0
        print(palabra)
        for pa in palabra:
            if pa in resultado:
                contar=contar+1
        print(palabra," contar  ",contar)
        if contar > 0:
            vec_contar[kk] +=contar
            vec_new_ids[kk] = vec_new_id[kk]
        kk+=1
    return vec_contar,vec_new_ids


def coseno_de_similitud_buscar(bd_texto,documentos,top_10_codigos,top_10_textos):

    # Calcular la matriz TF-IDF
    vectorizer = TfidfVectorizer().fit_transform(documentos)
    similitudes = cosine_similarity(vectorizer[-1], vectorizer[:-1])

    # Ordenar las asignaturas por similitud
    texto_ordenadas = sorted(zip(top_10_codigos, top_10_textos, similitudes[0]), key=lambda x: x[2], reverse=True)
    umbral = 0.2
    texto_similar = []
    for codigo, asignatura, similitud in texto_ordenadas:
        # Si la similitud es mayor que un umbral, considera que la asignatura está mencionada
        if similitud >=umbral:  # Ajusta este umbral según sea necesario
            texto_similar.append((codigo, ''.join(asignatura), similitud))

    # Imprimir todas las asignaturas mencionadas
    codigos_encontrado = []
    texto_encontrados = []
    print("¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿")
    k = 0
    for codigo, es_texto, similitud in texto_similar:
        print(k,f"Código: {codigo}, texto: {es_texto}, Similitud: {similitud:.2f}")
        codigos_encontrado.append(codigo)
        texto_encontrados.append(es_texto)
        k = k +1
    print("¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿")
    return texto_encontrados,codigos_encontrado



def buscar(texto,posible_respuesta):
    texto = eliminar_tildes(texto.lower())

    # Filtrar las palabras no deseadas (palabras de apoyo como conjunciones, preposiciones, etc.)
    palabras_filtradas = filtrar(texto)
    si_hay_materias = obtener_id_materia(texto,palabras_filtradas)#verificar si hay alguna materia en el texto
    #print(texto)
    consulta = ""
    response = "argumentar_poco_mas"
    # Tokenizar el texto del usuario
    # Codificar las oraciones en un espacio semántico
    texto_embedding = obtener_embedding(texto,posible_respuesta)
    # Inicializar lista para almacenar los resultados de la similitud del coseno
    coseno_salida = []
    # Calcular la similitud coseno entre la consulta y todas las oraciones
    codigos,embedding,text_new = seleccionarEmbeddinBd()#seleccionar embedding de base de dtos
    embe = np.array(embedding)
    similitudes = cosine_similarity([texto_embedding], embe)
    #indice_max_coseno = similitudes.argmax()

    # Obtener los índices de las similitudes ordenadas de mayor a menor
    indices_ordenados = np.argsort(similitudes[0])[::-1]

    # Seleccionar los 10 máximos o mas
    top_10_indices = indices_ordenados[:25]
    # Obtener los códigos y respuestas asociadas a los 10 máximos
    top_10_textos = [text_new[idx] for idx in top_10_indices]
    top_10_codigos = [codigos[idx] for idx in top_10_indices]
    #top_10_respuestas = [seleccionar_respesta_y_consulta(codigos[idx]) for idx in top_10_indices]
    claves = seleccionarTodoPalabraClaves()
    diccionario = []
    for res in top_10_textos:
        diccionario.append(filtrar(res))
    bd_texto = [' '.join(tokens) for tokens in diccionario]
    documentos = bd_texto + [' '.join(palabras_filtradas)]
    texto_encontrados,codigos_encontrado = coseno_de_similitud_buscar(bd_texto,documentos,top_10_codigos,top_10_textos)
    diccionario = []
    #print("-----------------------------------------------------------")
    #print(texto_encontrados," === ",codigos_encontrado)
    for res in texto_encontrados:
        diccionario.append(filtrar(res))
    top_10_codigos = [idx for idx in codigos_encontrado]
    top_10_textos = [idx for idx in texto_encontrados]
    sino,otro = sinonimos(palabras_filtradas)#aproabado aprobaron apr

    #print(sino)
    resultado,posiciones = obtener_palabras_claves_del_texto_usuario(otro,palabras_filtradas,claves)

    print(palabras_filtradas," palabras filtradas")
    vec_suma= clasificando(diccionario,top_10_textos,top_10_codigos,sino,claves,posiciones,si_hay_materias)
    vec_new_id = []
    vec_new_text = []
    k = 0
    print(vec_suma)
    if len(vec_suma)>0:
        for da in vec_suma:
            if da != 0:
                vec_new_id.append(top_10_codigos[k])
                vec_new_text.append(diccionario[k])
            k+=1
    print(vec_new_id,"    ",vec_new_text)
    print(palabras_filtradas," palabras filtradas")

    vec_contar,vec_ids = clasificacando_por_segunda_ves(vec_new_id,vec_new_text,otro,claves,palabras_filtradas,resultado)
    print(vec_contar,"    ",vec_ids)
    maximo = 0
    id_max = 0
    contar_cero = 0
    for cero in vec_contar:
        if cero == 0:
            contar_cero+=1
    contar_cero_primero = 0
    for cero in vec_suma:
        if cero == 0:
            contar_cero_primero+=1

    if len(vec_contar) != contar_cero:
        print("llego")
        maximo = max(vec_contar)
        posicion = vec_contar.index(maximo)
        print(posicion,"   posicion")
        id_max = vec_ids[posicion]
    elif len(vec_suma) != contar_cero_primero:
        maximo = max(vec_suma)
        posicion = vec_suma.index(maximo)
        print(posicion,"   posicion")
        id_max = top_10_codigos[posicion]
    if id_max != 0:
        respuesta_bd = seleccionar_respuesta_y_consulta(id_max)
        consultas_sql={}
        if respuesta_bd != "no":
            response = respuesta_bd[1]
            consultas_sql[response] = respuesta_bd[2]
            # Ordenar las oraciones según la similitud
            #resultados = zip(range(len(cosine_scores)), cosine_scores)
            #sorted_results = sorted(resultados, key=lambda x: x[1], reverse=True)
            #resultado_tensor = sorted_results[0][1]

    print(response,"  repuesta")

    if response:
        vec1=[]
        if response == "ver_carreras":
            response = ""
            areas = obtener_areas_id(texto)#obtener las areas
            nombre_posicion_sql = "ver_carreras"
            sql = consultas_sql[nombre_posicion_sql]
            carreras_encontradas = obtener_carreras_nombre(texto)
            if carreras_encontradas:
                vec1.append("si_car_n")
                # Obtener la primera carrera encontrada
                si = "no"
                idd = ""
                for car in carreras_encontradas:
                    idd+=str(car)+","
                    if si == "no":
                        response+=" where cod_carrera = "+str(car)
                        si = "si"
                    elif si == "si":
                        response+= " or cod_carrera = "+str(car)
                response = sql+" "+response
                vec1.append(idd)
                vec1.append("no")
                vec1.append("no")
            elif areas:
                vec1.append("no")
                vec1.append("no")
                vec1.append("si_ar")
                si = "no"
                idd = ""
                for i in areas:#recorremos las areas solicitadas
                    idd+=str(i)+","
                    if si == "no":
                        response += " where cod_area = "+str(i)
                        si = "si"
                    elif si == "si":
                        response += " or cod_area="+str(i) #obtenemos la consulta y lo concatenamos
                vec1.append(idd)
                response = sql+" "+response;
            else:
                vec1.append("no")
                vec1.append("no")
                vec1.append("no")
                vec1.append("no")
                vec1.append("si_car")
                response = sql
            vec1.append(nombre_posicion_sql)
            vec1.append(response)

        if response== "total_de_estudiantes":
            vec1=[]
            res = busqueda(texto,"total_de_estudiantes",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "seleccionar_carreras_area":#nos permite seleccionar todas las carreras por area
            vec1 = []
            response = ""
            contar_parametros=0
            ar = obtener_area(texto)  # Supongamos que esto devuelve una lista de áreas
            if ar:
                vec1.append("si_ar")  # Agrega "si_ar" a vec1 si se encontraron áreas en el texto
                contar_parametros+=1
            else:
                vec1.append("no")  # Agrega "no" a vec1 si no se encontraron áreas en el texto
            nombre_posicion_sql = "seleccionar_carreras_area"
            sql = consultas_sql[nombre_posicion_sql]  # Obtiene la consulta SQL según el nombre de la posición
            si = "no"
            unir = ""
            if contar_parametros ==0:
                response = "argumentar_poco_mas"
            else:
                for i in range(len(ar)):
                    sql_aux = consultas_aux["cod_area"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                    if si == "no":
                        response += sql_aux.format(ar[i])  # Agrega la consulta auxiliar al response si es la primera iteración
                        unir+=str(ar[i])+"|"
                        si = "si"
                    elif si == "si":
                        unir+=str(ar[i])+"|"
                        response += " or " + sql_aux.format(ar[i])  # Agrega "or" y la consulta auxiliar al response para otras iteracpara otras iteraciones
                vec1.append(unir)
                vec1.append(nombre_posicion_sql)  # Agrega el nombre de la posición SQL a vec1
                response = sql + response  # Combina la consulta principal con las consultas auxiliares
            vec1.append(response)  # Agrega la consulta completa a vec1
        if response == "total_de_estudiantes_estadisticas":#obtener estadistica de estudiantes aprobados y reprobados
            vec1=[]
            res = busqueda(texto,"total_de_estudiantes_estadisticas",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "seleccionar_estudiantes_desertores":
            vec1=[]
            res = busqueda(texto,"seleccionar_estudiantes_desertores",consultas_sql)
            for r in res:
                vec1.append(r)

        if response == "diferencia_entre_primero_quinto":
            vec1=[]
            res = busqueda(texto,"diferencia_entre_primero_quinto",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "asignaturas_desercion":
            vec1=[]
            res = busqueda(texto,"asignaturas_desercion",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "clasificado_sexo":
            vec1=[]
            res = busqueda(texto,"clasificado_sexo",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "transferencias_buscar":
            vec1=[]
            res = busqueda(texto,"transferencias_buscar",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "concepto_transferencia":
            vec1=[]
            res = busqueda(texto,"concepto_transferencia",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "mayor_inscritos":
            vec1=[]
            res = busqueda(texto,"mayor_inscritos",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "modalidad_titulacion":
            vec1=[]
            res = construir_consulta(texto,"modalidad_titulacion",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "total_estudiante_desercion":
            vec1=[]
            res = busqueda(texto,"total_estudiante_desercion",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "titulados_relacion":
            vec1=[]
            res = busqueda(texto,"titulados_relacion",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "clasificacion_departamento":
            vec1=[]
            res = busqueda(texto,"clasificacion_departamento",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "plan_de_estudio":
            areas = obtener_areas_id(texto)
            vec = []
            vec1 = []
            response = ""
            contar_parametros = 0
            nombre_posicion_sql="plan_de_estudio"
            if areas:
                contar_parametros+=1

            if contar_parametros>0:#existe un nombre de area entonces solo buscar en los areas o en el area
                si = "no"
                idd = ""
                for i in range(len(areas)):#recorremos las areas solicitadas
                    idd+=str(areas[i])+","
                    if si == "no":
                        response += " where cod_area = "+str(areas[i])
                        si = "si"
                    elif si == "si":
                        response += " or cod_area="+str(areas[i])
                sql = consultas_sql[nombre_posicion_sql] #obtenemos la consulta y lo concatenamos
                vec1.append("si_ar")
                vec1.append(idd)
                vec1.append("no")
                vec1.append("no")
                vec1.append("no")
                vec1.append(nombre_posicion_sql)
                vec1.append(sql+response)
            else:
                contar_parametros=0
                carreras_encontradas = obtener_carreras_nombre(texto);#buscar carreras si en el texto hay alguna carrera
                if carreras_encontradas:#si existe algun nombre de carrera ingresa
                    contar_parametros+=1

                if contar_parametros>0:#existe carreras
                    si = "no"
                    idd = ""
                    for i in range(len(carreras_encontradas)):
                        idd+=str(carreras_encontradas[i])+","
                        if si == "no":
                            response += " where cod_carrera = "+str(carreras_encontradas[i])
                            si = "si"
                        elif si == "si":
                            response += " or cod_carrera="+str(carreras_encontradas[i])
                    sql = consultas_sql[nombre_posicion_sql] #obtenemos la consulta y lo concatenamos
                    vec1.append("no")
                    vec1.append("no")
                    vec1.append("si_car")
                    vec1.append(idd)
                    vec1.append("no")
                    vec1.append(nombre_posicion_sql)
                    vec1.append(sql+response)
                else:
                    sql = consultas_sql[nombre_posicion_sql] #obtenemos la consulta y lo concatenamos
                    vec1.append("no")
                    vec1.append("no")
                    vec1.append("no")
                    vec1.append("no")
                    vec1.append("si_total")
                    vec1.append(nombre_posicion_sql)
                    vec1.append(sql)
        if response == "materias_inscritos":
            vec1=[]
            res = busqueda(texto,"materias_inscritos",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "asignaturas":
            vec1=[]
            res = consulta_buscar(texto,"asignaturas",consultas_sql)
            for r in res:
                vec1.append(r)
        if response== "total_de_estudiantes_carrera":
            vec1=[]
            res = busqueda(texto,"total_de_estudiantes_carrera",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "porcentaje_de_avance_materias":
            vec1=[]
            res = busqueda(texto,"porcentaje_de_avance_materias",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "titulados":
            vec1=[]
            res = busqueda(texto,"titulados",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "cantidad_docentes":
            vec1=[]
            res = busqueda(texto,"cantidad_docentes",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "docente_sexo":
            vec1=[]
            res = busqueda(texto,"docente_sexo",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "departamento_docente":
            vec1=[]
            res = busqueda(texto,"departamento_docente",consultas_sql)
            for r in res:
                vec1.append(r)

        if response == "datos_carrera":#seleccionamos los datos de la carrera
            vec1=[]
            res = buscarDatosCarrera(texto,"datos_carrera",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "areas":
            vec1=[]
            res = buscarDatosArea(texto,"areas",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == 'areas_unsxx':
            vec1 = []
            vec1.append('areas_unsxx')
            vec1.append(consultas_sql['areas_unsxx'])
        if response == 'materias_aprobados':
            vec1=[]
            res = construir_consulta_materia(texto,"materias_aprobados",consultas_sql,si_hay_materias)
            for r in res:
                vec1.append(r)
        if response == "datos_asignaturas":
            vec1=[]
            res = consulta_buscar(texto,"datos_asignaturas",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == 'carrera_area_mas_inscritos':
            vec1=[]
            resulta = seleccionar_si_quiere_por_area_o_carrera(texto)
            vec1.append(resulta)
            res = busqueda(texto,"carrera_area_mas_inscritos",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "total_estudiantes_area":
            vec1=[]
            res = busqueda(texto,"total_estudiantes_area",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "pasaron_de_curso":
            vec1=[]
            res=consulta_pasaron(texto,"pasaron_de_curso",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == 'estudiantes_regulares_en_materia':
            vec1=[]
            res = construir_consulta_materia(texto,"estudiantes_regulares_en_materia",consultas_sql,si_hay_materias)
            for r in res:
                vec1.append(r)
        if response == 'estudiantes_desercion_en_materia':
            vec1=[]
            res = construir_consulta_materia(texto,"estudiantes_desercion_en_materia",consultas_sql,si_hay_materias)
            for r in res:
                vec1.append(r)
        if response == 'materia_total_datos':
            vec1=[]
            res = construir_consulta_materia_datos(texto,"materia_total_datos",consultas_sql,si_hay_materias)
            for r in res:
                vec1.append(r)
        if response == 'argumentar_poco_mas':
            vec1 = []
            vec1.append(response)
        if response == "culminacion_estudios":
            vec1=[]
            res = busqueda(texto,"culminacion_estudios",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == "aprobechamiento":
            vec1=[]
            res = busqueda(texto,"aprobechamiento",consultas_sql)
            for r in res:
                vec1.append(r)
        return vec1
    else:
        vec1=[]
        vec1.append("argumentar_poco_mas")
        return vect1

#construyendo consulta sql de materiasss

def construir_consulta_materia_datos(texto,respuesta,consultas_sql,materias):
    print(texto,"   =    ",respuesta)
    vec = []
    vec1 = []
    response = "";
    fecha = fechas(texto)
    areas = obtener_areas_id(texto)#obtener las areas
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    carreras_encontradas = obtener_carreras_nombre(texto)
    bien_de = 0

    if len(fecha) >= 1:#si existe fechas
        vec.append("si_fecha")
        if len(fecha) == 1:
            fecha1 = fecha[0]
            fecha2 = ""
        elif len(fecha)>1:
            fecha1 = fecha[0]
            fecha2 = fecha[1]
    else:#no hay fechas
        fecha_actual = datetime.now()
        # Formatear la fecha como año, mes, día
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
        anio = obtener_ano_de_fecha(fecha_formateada)
        vec.append("si_fecha")
        fecha1 = anio+"-01-01"
        fecha2 = anio+"-12-30"
    response2 = ''
    existe = 'si'
  
    response = " where c.cod_parcial = 1 and "
    if materias:
        vec1.append("si_mat")
        # Obtener la primera carrera encontrada
        si = "no"
        idd = ""
        for mat in materias:
            idd+=str(mat)+","
            if si == "no":
                response+=" c.cod_asig = "+str(mat)
                si = "si"
            elif si == "si":
                response+= " or c.cod_asig = "+str(mat)
        response = sql+" "+response
        vec1.append(idd)
        bien_de = 1

    else:
        vec1.append("argumentar_poco_mas")
        existe = 'no'

    if existe == 'si':
        if carreras_encontradas:
            vec1.append("si_car_n")
            # Obtener la primera carrera encontrada
            si = "no"
            idd = ""
            for car in carreras_encontradas:
                idd+=str(car)+","
                if si == "no":
                    response+=" and c.cod_carrera = "+str(car)
                    si = "si"
                elif si == "si":
                    response+= " or c.cod_carrera = "+str(car)

            response= " "+response+" and "
            vec1.append(idd)
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            bien_de = 1
        elif areas:
            vec1.append("no")
            vec1.append("no")
            vec1.append("si_ar")
            si = "no"
            idd = ""
            for i in areas:#recorremos las areas solicitadas
                idd+=str(i)+","
                if si == "no":
                    response += " and c.cod_area = "+str(i)
                    si = "si"
                elif si == "si":
                    response += " or c.cod_area="+str(i) #obtenemos la consulta y lo concatenamos
            vec1.append(idd)
            vec1.append("no")
            bien_de = 1
            response= " "+response+" and "
        else:
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            vec1.append("si_total")
            bien_de = 2 #ponemos dos porque no se esta buscando por carrera o area si no todo
        if bien_de != 0: #quiero el eusuari todo o de carrera o area
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            response3 = ''

            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response3+=" ( c."+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and c."+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and c."+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response3+=" and ( c."+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and c."+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and c."+sql_aux.format(fecha1)+")"

                    si = "si"
                vec[i] = "no"
            if bien_de == 1:#si se mantienen en no entonces aumentamos WHERE
                response= response+" "+response3
            elif bien_de == 2:
                response=response+" and "+response3

        vec1.append(nombre_posicion_sql)
        vec1.append(response)
    return vec1

#contruir consulta para cuantos estudiantes pasaron de curso o # NOTE:
def consulta_pasaron(texto,respuesta,consultas_sql):
    vec = []
    vec1 = []
    response = "";
    areas = obtener_areas_id(texto)#obtener las areas
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    carreras_encontradas = obtener_carreras_nombre(texto)
    bien_de = 0
    response2 = ''
    grado = obtener_que_curso_quiere(texto)
    if grado:#si existe algun curso en el texto ingresa
        si = 'no'
        idd2=''
        for gra in grado:
            idd2+=str(gra)+","#concatenamos los id de grado
        vec1.append(idd2)

        if carreras_encontradas:

            vec1.append("si_car_n")
            # Obtener la primera carrera encontrada
            si = "no"
            idd = ""
            for car in carreras_encontradas:
                idd+=str(car)+","
                if si == "no":
                    response+=" where cod_carrera = "+str(car)
                    si = "si"
                elif si == "si":
                    response+= " or cod_carrera = "+str(car)

            response = sql+" "+response+" and "
            vec1.append(idd)
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            bien_de = 1
        elif areas:
            vec1.append("no")
            vec1.append("no")
            vec1.append("si_ar")
            si = "no"
            idd = ""
            for i in areas:#recorremos las areas solicitadas
                idd+=str(i)+","
                if si == "no":
                    response += " where cod_area = "+str(i)
                    si = "si"
                elif si == "si":
                    response += " or cod_area="+str(i) #obtenemos la consulta y lo concatenamos
            vec1.append(idd)
            vec1.append("no")
            response = sql+" "+response+" and "
            bien_de = 1
        else:
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            vec1.append("si_total")
            response=sql+" where "
            bien_de = 2
        fecha = fechas(texto)
        if len(fecha) >= 1:#si existe fechas
            vec.append("si_fecha")
            if len(fecha) == 1:
                fecha1 = fecha[0]
                fecha2 = ""
            elif len(fecha)>1:
                fecha1 = fecha[0]
                fecha2 = fecha[1]
        else:#no hay fechas
            fecha_actual = datetime.now()
            # Formatear la fecha como año, mes, día
            fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
            anio = obtener_ano_de_fecha(fecha_formateada)
            vec.append("si_fecha")
            fecha1 = anio+"-01-01"
            fecha2 = anio+"-12-30"
        si = "no"
        if fecha2 == "" and fecha1 != "":
            vec1.append(fecha1)
            vec1.append(fecha1)
        else:
            vec1.append(fecha1)
            vec1.append(fecha2)
        response3 = ''

        for i in range(len(vec)):
            if vec[i] == "si_fecha" and si == "no":
                if fecha1 != "":#si es diferente de vacio
                    sql_aux = consultas_aux["fechai"]
                    response3+=" ( "+sql_aux.format(fecha1)
                if fecha2 != "":
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha2)+")"
                else:
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha1)+")"
                si = "si"
            elif vec[i] == "si_fecha" and si == "si":
                if fecha1 != "":#si es diferente de vacio
                    sql_aux = consultas_aux["fechai"]
                    response3+=" and ( "+sql_aux.format(fecha1)
                if fecha2 != "":
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha2)+")"
                else:
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha1)+")"
                si = "si"
            vec[i] = "no"
            response = response+" "+response3
            vec1.append(nombre_posicion_sql)
            vec1.append(response)
        return vec1
    else:
        vec1.append("argumentar_poco_mas")
        return vec1

def buscarDatosCarrera(texto,respuesta,consultas_sql):
    vec1 = []
    response = ''
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    carreras_encontradas = obtener_carreras_nombre(texto)
    if carreras_encontradas:
        vec1.append("si_car_n")
        # Obtener la primera carrera encontrada
        si = "no"
        idd = ""
        for car in carreras_encontradas:
            idd+=str(car)+","
            if si == "no":
                response+=" where cod_carrera = "+str(car)
                si = "si"
            elif si == "si":
                response+= " or cod_carrera = "+str(car)
        response = sql+" "+response
        vec1.append(idd)
        vec1.append(nombre_posicion_sql)
        vec1.append(response)
    else:
        vec1.append("argumentar_poco_mas")
    return vec1
def buscarDatosArea(texto,respuesta,consultas_sql):
    vec1 = []
    response = ''
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    areas = obtener_areas_id(texto)#obtener las areas
    if areas:
        vec1.append("si_ar")
        # Obtener la primera carrera encontrada
        si = "no"
        idd = ""
        for are in areas:
            idd+=str(are)+","
            if si == "no":
                response+=" where cod_area = "+str(are)
                si = "si"
            elif si == "si":
                response+= " or cod_area = "+str(are)
        response = sql+" "+response
        vec1.append(idd)
        vec1.append(nombre_posicion_sql)
        vec1.append(response)
    else:
        response = sql
        vec1.append(nombre_posicion_sql)
        vec1.append(response)
    return vec1

#funcion para construir consulta sql con carreras y grados y obtener_areas_id
def consulta_buscar(texto,respuesta,consultas_sql):
    vec = []
    vec1 = []
    response = "";
    areas = obtener_areas_id(texto)#obtener las areas
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    carreras_encontradas = obtener_carreras_nombre(texto)
    bien_de = 0
    response2 = ''
    if carreras_encontradas:
        grado = obtener_que_curso_quiere(texto)
        vec1.append("si_car_n")
        # Obtener la primera carrera encontrada
        si = "no"
        idd = ""
        for car in carreras_encontradas:
            idd+=str(car)+","
            if si == "no":
                response+=" where cod_carrera = "+str(car)
                si = "si"
            elif si == "si":
                response+= " or cod_carrera = "+str(car)
        vec1.append(idd)
        if grado:#si existe algun curso en el texto ingresa
            si = 'no'
            idd2=''
            for gra in grado:
                idd2+=str(gra)+","#concatenamos los id de grado
                response+= " and cod_grado = "+str(gra)
            vec1.append("si_grado")
            vec1.append(idd2)
        else:
            vec1.append("no")
            vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        response = sql+" "+response
        bien_de = 1
    elif areas:
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("si_ar")
        si = "no"
        idd = ""
        for i in areas:#recorremos las areas solicitadas
            idd+=str(i)+","
            if si == "no":
                response += " where cod_area = "+str(i)
                si = "si"
            elif si == "si":
                response += " or cod_area="+str(i) #obtenemos la consulta y lo concatenamos
        vec1.append(idd)
        vec1.append("no")
        response = sql+" "+response
        bien_de = 1
    else:
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("si_total")
        response=sql
        bien_de = 2


    if nombre_posicion_sql == "datos_asignaturas":
        fecha = fechas(texto)
        if len(fecha) >= 1:#si existe fechas
            vec.append("si_fecha")
            if len(fecha) == 1:
                fecha1 = fecha[0]
                fecha2 = ""
            elif len(fecha)>1:
                fecha1 = fecha[0]
                fecha2 = fecha[1]
        else:#no hay fechas
            fecha_actual = datetime.now()
            # Formatear la fecha como año, mes, día
            fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
            anio = obtener_ano_de_fecha(fecha_formateada)
            vec.append("si_fecha")
            fecha1 = anio+"-01-01"
            fecha2 = anio+"-12-30"
        si = "no"
        if fecha2 == "" and fecha1 != "":
            vec1.append(fecha1)
            vec1.append(fecha1)
        else:
            vec1.append(fecha1)
            vec1.append(fecha2)
        response3 = ''

        for i in range(len(vec)):
            if vec[i] == "si_fecha" and si == "no":
                if fecha1 != "":#si es diferente de vacio
                    sql_aux = consultas_aux["fechai"]
                    response3+=" ( "+sql_aux.format(fecha1)
                if fecha2 != "":
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha2)+")"
                else:
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha1)+")"
                si = "si"
            elif vec[i] == "si_fecha" and si == "si":
                if fecha1 != "":#si es diferente de vacio
                    sql_aux = consultas_aux["fechai"]
                    response3+=" and ( "+sql_aux.format(fecha1)
                if fecha2 != "":
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha2)+")"
                else:
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha1)+")"
                si = "si"
            vec[i] = "no"
            if bien_de == 1:
                response = response+" and "+response3
            elif bien_de == 2:
                response = response+" where "+response3
    vec1.append(nombre_posicion_sql)
    vec1.append(response)
    return vec1

def construir_consulta_materia(texto,respuesta,consultas_sql,materias):
    print(texto,"   =    ",respuesta)
    vec = []
    vec1 = []
    response = "";
    fecha = fechas(texto)
    areas = obtener_areas_id(texto)#obtener las areas
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    carreras_encontradas = obtener_carreras_nombre(texto)
    bien_de = 0

    if len(fecha) >= 1:#si existe fechas
        vec.append("si_fecha")
        if len(fecha) == 1:
            fecha1 = fecha[0]
            fecha2 = ""
        elif len(fecha)>1:
            fecha1 = fecha[0]
            fecha2 = fecha[1]
    else:#no hay fechas
        fecha_actual = datetime.now()
        # Formatear la fecha como año, mes, día
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
        anio = obtener_ano_de_fecha(fecha_formateada)
        vec.append("si_fecha")
        fecha1 = anio+"-01-01"
        fecha2 = anio+"-12-30"
    response2 = ''
    existe = 'si'
    print(materias,"llego")
    if materias:
        vec1.append("si_mat")
        # Obtener la primera carrera encontrada
        si = "no"
        idd = ""
        for mat in materias:
            idd+=str(mat)+","
            if si == "no":
                response+=" where cod_parcial = 1 and cod_asig = "+str(mat)
                si = "si"
            elif si == "si":
                response+= " or cod_asig = "+str(mat)
        response = sql+" "+response
        vec1.append(idd)
        bien_de = 1

    else:
        vec1.append("argumentar_poco_mas")
        existe = 'no'

    if existe == 'si':
        if carreras_encontradas:
            vec1.append("si_car_n")
            # Obtener la primera carrera encontrada
            si = "no"
            idd = ""
            for car in carreras_encontradas:
                idd+=str(car)+","
                if si == "no":
                    response+=" and cod_carrera = "+str(car)
                    si = "si"
                elif si == "si":
                    response+= " or cod_carrera = "+str(car)

            response= " "+response+" and "
            vec1.append(idd)
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            bien_de = 1
        elif areas:
            vec1.append("no")
            vec1.append("no")
            vec1.append("si_ar")
            si = "no"
            idd = ""
            for i in areas:#recorremos las areas solicitadas
                idd+=str(i)+","
                if si == "no":
                    response += " and cod_area = "+str(i)
                    si = "si"
                elif si == "si":
                    response += " or cod_area="+str(i) #obtenemos la consulta y lo concatenamos
            vec1.append(idd)
            vec1.append("no")
            bien_de = 1
            response= " "+response+" and "
        else:
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            vec1.append("no")
            vec1.append("si_total")
            bien_de = 2 #ponemos dos porque no se esta buscando por carrera o area si no todo
        if bien_de != 0: #quiero el eusuari todo o de carrera o area
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            response3 = ''

            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response3+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response3+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response3+=" and "+sql_aux.format(fecha1)+")"

                    si = "si"
                vec[i] = "no"
            if bien_de == 1:#si se mantienen en no entonces aumentamos WHERE
                response= response+" "+response3
            elif bien_de == 2:
                response=response+" and "+response3

        vec1.append(nombre_posicion_sql)
        vec1.append(response)
    return vec1

#funcion para construir una consulta sql con solo fechas carrera y area
def busqueda(texto,respuesta,consultas_sql):
    print(texto,"   =    ",respuesta)
    vec = []
    vec1 = []
    response = "";

    fecha = fechas(texto)
    areas = obtener_areas_id(texto)#obtener las areas
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    carreras_encontradas = obtener_carreras_nombre(texto)
    bien_de = 0

    if len(fecha) >= 1:#si existe fechas
        vec.append("si_fecha")
        if len(fecha) == 1:
            fecha1 = fecha[0]
            fecha2 = ""
        elif len(fecha)>1:
            fecha1 = fecha[0]
            fecha2 = fecha[1]
    else:#no hay fechas
        fecha_actual = datetime.now()
        # Formatear la fecha como año, mes, día
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
        anio = obtener_ano_de_fecha(fecha_formateada)
        vec.append("si_fecha")
        fecha1 = anio+"-01-01"
        fecha2 = anio+"-12-30"
    response2 = ''
    if carreras_encontradas:
        vec1.append("si_car_n")
        # Obtener la primera carrera encontrada
        si = "no"
        idd = ""
        for car in carreras_encontradas:
            idd+=str(car)+","
            if si == "no":
                response+=" where cod_carrera = "+str(car)
                si = "si"
            elif si == "si":
                response+= " or cod_carrera = "+str(car)
        if nombre_posicion_sql == "titulados_relacion":
            response2 = "select *from titulado "+response+" and "
        response = sql+" "+response+" and "
        vec1.append(idd)
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        bien_de = 1
    elif areas:
        vec1.append("no")
        vec1.append("no")
        vec1.append("si_ar")
        si = "no"
        idd = ""
        for i in areas:#recorremos las areas solicitadas
            idd+=str(i)+","
            if si == "no":
                response += " where cod_area = "+str(i)
                si = "si"
            elif si == "si":
                response += " or cod_area="+str(i) #obtenemos la consulta y lo concatenamos
        vec1.append(idd)
        vec1.append("no")
        bien_de = 1
        if nombre_posicion_sql == "titulados_relacion":
            response2 = "select *from titulado "+response+" and"
        response = sql+" "+response+" and "
    else:
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("si_total")
        bien_de = 2 #ponemos dos porque no se esta buscando por carrera o area si no todo
    if bien_de != 0: #quiero el eusuari todo o de carrera o area
        si = "no"
        if fecha2 == "" and fecha1 != "":
            vec1.append(fecha1)
            vec1.append(fecha1)
        else:
            vec1.append(fecha1)
            vec1.append(fecha2)
        response3 = ''
        for i in range(len(vec)):
            if vec[i] == "si_fecha" and si == "no":
                if fecha1 != "":#si es diferente de vacio
                    sql_aux = consultas_aux["fechai"]
                    response3+=" ( "+sql_aux.format(fecha1)
                if fecha2 != "":
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha2)+")"
                else:
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha1)+")"
                si = "si"
            elif vec[i] == "si_fecha" and si == "si":
                if fecha1 != "":#si es diferente de vacio
                    sql_aux = consultas_aux["fechai"]
                    response3+=" and ( "+sql_aux.format(fecha1)
                if fecha2 != "":
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha2)+")"
                else:
                    sql_aux = consultas_aux["fechaf"]
                    response3+=" and "+sql_aux.format(fecha1)+")"

                si = "si"
            vec[i] = "no"
        if bien_de == 1:#si se mantienen en no entonces aumentamos WHERE
            if nombre_posicion_sql == "titulados_relacion":
                vec1.append(response2+" "+response3)
            response = response+" "+response3
        elif bien_de == 2:
            if nombre_posicion_sql == "titulados_relacion":
                vec1.append("select *from titulado where "+response3)
            response=sql+" where "+response3
    if nombre_posicion_sql == "materias_inscritos":
        response +=" and cod_parcial = 1"
    vec1.append(nombre_posicion_sql)
    vec1.append(response)
    return vec1

def construir_consulta(texto,respuesta,consultas_sql):
    print(texto,"   =    ",respuesta)
    vec = []
    vec1 = []
    response = "";
    areas = obtener_areas_id(texto)#obtener las areas
    nombre_posicion_sql = respuesta
    sql = consultas_sql[nombre_posicion_sql]
    carreras_encontradas = obtener_carreras_nombre(texto)
    bien_de = 0
    if carreras_encontradas:
        vec1.append("si_car_n")
        # Obtener la primera carrera encontrada
        si = "no"
        idd = ""
        for car in carreras_encontradas:
            idd+=str(car)+","
            if si == "no":
                response+=" where cod_carrera = "+str(car)
                si = "si"
            elif si == "si":
                response+= " or cod_carrera = "+str(car)
        response = sql+" "+response
        vec1.append(idd)
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
    elif areas:
        vec1.append("no")
        vec1.append("no")
        vec1.append("si_ar")
        si = "no"
        idd = ""
        for i in areas:#recorremos las areas solicitadas
            idd+=str(i)+","
            if si == "no":
                response += " where cod_area = "+str(i)
                si = "si"
            elif si == "si":
                response += " or cod_area="+str(i) #obtenemos la consulta y lo concatenamos
        vec1.append(idd)
        vec1.append("no")
        response = sql+" "+response

    else:
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("no")
        vec1.append("si_total")
        response = sql
    vec1.append(nombre_posicion_sql)
    vec1.append(response)
    return vec1
