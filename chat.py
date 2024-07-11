
import pymysql
from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter,contiene_palabras_activas,contiene_palabras_desactivas,contiene_palabras_sexo_varon,contiene_palabras_sexo_mujer
from comprobar import palabras_departamento,palabras_provincia,encontrar_nombre,encontrar_apellido,obtener_area,palabra_desercion
from comprobar import palabra_aplazaron,palabra_aprobados,palabra_curso,obtener_que_curso_quiere
from comprobar import palabra_nota,fechas,obtener_ano,obtener_areas_id,obtener_id_materia
from comprobar import seleccionar_si_quiere_por_area_o_carrera
from sql import seleccionar_estudiante1,seleccionar_consultasEmbeddings,seleccionar_respuesta_y_consulta
from sentence_transformers import SentenceTransformer, util
import numpy as np
from datetime import datetime
from comprobar import obtener_ano_de_fecha
from sklearn.metrics.pairwise import cosine_similarity

from unidecode import unidecode
# Cargar el modelo pre-entrenado
model = SentenceTransformer('all-MiniLM-L6-v1')
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
        print("el id es ",codigo)
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
    sql_consulta = "SELECT cod_respuesta,embedding FROM embeddings WHERE cod_respuesta is not null"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)
    embeddings = []
    codigos = []
    # Obtener todos los embeddings y códigos de asignatura
    for row in cursor.fetchall():
        codigos.append(row[0])
        embeddings.append(np.frombuffer(row[1], dtype=np.float32))  # Convertir el blob a un array numpy
    return codigos,embeddings


def eliminar_tildes(texto):
    return unidecode(texto)

def buscar(texto,posible_respuesta):
    print(posible_respuesta,"respuenndndndnnnnnnnnnnn")
    texto = eliminar_tildes(texto.lower())
    #print(texto)
    consulta = ""
    response = "argumentar_poco_mas"
    # Tokenizar el texto del usuario
    # Codificar las oraciones en un espacio semántico
    texto_embedding = obtener_embedding(texto,posible_respuesta)
    # Inicializar lista para almacenar los resultados de la similitud del coseno
    coseno_salida = []
    # Calcular la similitud coseno entre la consulta y todas las oraciones
    codigos,embedding = seleccionarEmbeddinBd()#seleccionar embedding de base de dtos
    embe = np.array(embedding)
    similitudes = cosine_similarity([texto_embedding], embe)
    indice_max_coseno = similitudes.argmax()
    max_coseno = similitudes[0, indice_max_coseno]
    codigo_respuesta = codigos[indice_max_coseno]
    respuesta_bd = seleccionar_respuesta_y_consulta(codigo_respuesta)
    consultas_sql={}
    if respuesta_bd != "no":
        response = respuesta_bd[1]
        consultas_sql[response] = respuesta_bd[2]
    # Ordenar las oraciones según la similitud
    #resultados = zip(range(len(cosine_scores)), cosine_scores)
    #sorted_results = sorted(resultados, key=lambda x: x[1], reverse=True)
    #resultado_tensor = sorted_results[0][1]
    print(response)
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
            res = construir_consulta_materia(texto,"materias_aprobados",consultas_sql)
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
            res = construir_consulta_materia(texto,"estudiantes_regulares_en_materia",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == 'estudiantes_desercion_en_materia':
            vec1=[]
            res = construir_consulta_materia(texto,"estudiantes_desercion_en_materia",consultas_sql)
            for r in res:
                vec1.append(r)
        if response == 'materia_total_datos':
            vec1=[]
            res = construir_consulta_materia_datos(texto,"materia_total_datos",consultas_sql)
            for r in res:
                vec1.append(r)
        return vec1
    else:
        vec1=[]
        vec1.append("argumentar_poco_mas")
        return vect1

#construyendo consulta sql de materiasss

def construir_consulta_materia_datos(texto,respuesta,consultas_sql):
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
    materias = obtener_id_materia(texto)
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
        vec1.append("argumentar_poco_mas")
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

def construir_consulta_materia(texto,respuesta,consultas_sql):
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
    materias = obtener_id_materia(texto)
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
