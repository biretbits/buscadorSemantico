
import pymysql
from comprobar import obtener_carreras_nombre,detectar_numeros_delimiter,contiene_palabras_activas,contiene_palabras_desactivas,contiene_palabras_sexo_varon,contiene_palabras_sexo_mujer
from comprobar import palabras_departamento,palabras_provincia,encontrar_nombre,encontrar_apellido,obtener_area,palabra_desercion
from comprobar import palabra_aplazaron,palabra_aprobados,palabra_curso,obtener_que_curso_quiere
from comprobar import palabra_nota,fechas,obtener_ano
from sql import seleccionar_estudiante1
from sentence_transformers import SentenceTransformer, util
import numpy as np
from datetime import datetime
from comprobar import obtener_ano_de_fecha
# Cargar el modelo pre-entrenado
model = SentenceTransformer('all-MiniLM-L6-v1')
sentencias = [
    "informacion carreras unsxx universidad nacional siglo xx",
    "informacion catidad estudiantes unsxx universidad nacional siglo xx",
    "informacion cantidad estudiantes carrera unsxx universidad nacional siglo xx",
    "informacion total estudiante carrera unsxx universidad nacional siglo xx",
    "informacion estudiantes unsxx universidad nacional siglo xx",
    "informacion carreras area areas tecnologia salud social unsxx universidad nacional siglo xx",
    "cuales carreras area areas tecnologia salud social unsxx universidad nacional siglo xx",
    "informacion estudiantes area tecnologia salud social unsxx universidad nacional siglo xx",
    "informacion calificacion estudiante carrera unxx universidad nacional siglo xx",
    "estadistica estudiantes area areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "estadistica estudiantes aprobados area areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "estadistica estudiantes reprobados area areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "cuales carreras unsxx universidad nacional siglo xx",
    "informacion carrera unsxx universidad nacional siglo xx",
    "cuales materias estudiante unsxx universidad nacional siglo xx",
    "estadistica estudiantes desertores area areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "estadistica estudiantes abandonaron dejaron estudios area areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "estadistica estudiantes concluyeron estudioss areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "estadistica estudiantes desertores asignaturas especificas areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "cuales cantidad de estudiantes que dejaron asignaturas areas  carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "cuales cantidad de estudiantes que abandonaron asignaturas areas  carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "cuales cantidad de estudiantes que dejaron materias areas  carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "cuales cantidad de estudiantes que abandonaron materias areas  carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "cual cantidad estudiantes sexo femenino masculino areas  carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "cual cantidad estudiantes clasificados varones mujeres areas  carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "poblacion estudiantil clasificado varones mujeres areas  carreras tecnologia salud social unsxx universidad nacional siglo xx"
    "cantidad estudiantes realizan transferencias universidades unsxx universidad nacional siglo xx",
    "total estudiantes realizan transferencias universidades sistema universitario unsxx universidad nacional siglo xx",
    "cantidad estudiantes realizan transferencia universidades unsxx universidad nacional siglo xx",
    "cantidad estudiantes provenientes universidades transferencias universidades unsxx universidad nacional siglo xx",
    "total de estudiantes vinieron concepto transferencia unsxx universidad nacional siglo xx",
    "cantidad estudiantes otras universidades concepto transferencia unsxx universidad nacional siglo xx",
    "numero estudiantes transferidos universidades unsxx universidad nacional siglo xx",
    "cantidad estudiantes inscritos primeros niveles areas  carreras tecnologia salud social unsxx universidad nacional siglo xx"
    "existe mas estudiantes inscritos primeros niveles areas carreras tecnologia salud social unsxx universidad nacional siglo xx",
    "en que carreras y areas hay mas inscritos de estudiantes tecnologia salud social unsxx universidad nacional siglo xx",
]
# Definir la lista de pares

respuesta =[
'ver_carreras',
'total_de_estudiantes',
'total_de_estudiantes_carrera',
'total_de_estudiantes_carrera',
'estudiantes_de_unsxx',
"seleccionar_carreras_area",
"seleccionar_carreras_area",
"estudiante_por_area",
"seleccionar_asignatura_estudiante",
"total_de_estudiantes_estadisticas",
"total_de_estudiantes_estadisticas",
"total_de_estudiantes_estadisticas",
'ver_carreras',
'ver_carreras',
"seleccionar_asignatura_estudiante",
"seleccionar_estudiantes_desertores",
"seleccionar_estudiantes_desertores",
"diferencia_entre_primero_quinto",
"asignaturas_desercion",
"asignaturas_desercion",
"asignaturas_desercion",
"asignaturas_desercion",
"asignaturas_desercion",
"clasificado_sexo",
"clasificado_sexo",
"clasificado_sexo",
"transferencias_buscar",
"transferencias_buscar",
"transferencias_buscar",
"concepto_transferencia",
"concepto_transferencia",
"concepto_transferencia",
"concepto_transferencia",
"mayor_inscritos",
"mayor_inscritos",
"mayor_inscritos",
]
consultas_sql = {
"ver_carreras":"select *from carrera",
"ver_por_nombre_estudiante":" select e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera from carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera where e.nombre_es like '%{}%' ",
"ver_carreras_nombre":"select *from carrera where cod_carrera = {};",
"total_de_estudiantes":"SELECT COUNT(*) FROM estudiante",
"total_de_estudiantes_carrera":"select *from estudiante",
"datos_especificos_estudiante":"SELECT e.nombre_es,e.ap_es,e.am_es,e.ci,e.pais_es,e.departamento,e.provincia,e.ciudad,e.region,e.sexo,c.nombre_carrera,e.cod_es FROM carrera as c inner join estudiante as e on c.cod_carrera = e.cod_carrera  where  ",
"estudiantes_de_unsxx":"select * from estudiante as e where ",
"seleccionar_carreras_area":"select *from area as a inner join carrera as c on a.cod_area = c.cod_area where ",
"estudiante_por_area":"select *from estudiante as e inner join estudiante_perdio as ep on e.cod_es = ep.cod_es",
"seleccionar_asignatura_estudiante":"select *from cursa_asignatura",
"seleccionar_asignatura_estudiante_calificacion":"select *from cursa_asignatura",
"total_de_estudiantes_estadisticas":"select * from estudiante_perdio",
"seleccionar_estudiantes_desertores":"select * from estudiante_perdio",
"diferencia_entre_primero_quinto":"select *from estudiante_perdio",
"asignaturas_desercion":"select *from cursa_asignatura",
"clasificado_sexo":"select *from estudiante",
"transferencias_buscar":"select *from transferencia",
"concepto_transferencia":"select * from transferir ",
"mayor_inscritos":"select * from estudiante",
}
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

def obtener_embedding(texto):
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "SELECT embedding FROM embeddings WHERE texto = %s"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta, (texto))

    # Verificar si hay algún resultado antes de obtenerlos
    if cursor.rowcount > 0:
        # Si hay resultados, obtener el embedding de la consulta
        embedding_str = cursor.fetchone()[0]
        # Convertir la cadena de texto del embedding a un array numpy
        embedding = np.frombuffer(embedding_str, dtype=np.float32)
        return embedding
    else:
        # Si no se encuentra el embedding, calcularlo con el modelo
        texto_embedding = model.encode(texto)
        # Convertir el embedding a bytes
        embedding_bytes = texto_embedding.tobytes()
        # Insertar el texto y el embedding en la base de datos
        sql_insert = "INSERT INTO embeddings (texto, embedding) VALUES (%s, %s)"
        cursor.execute(sql_insert, (texto, embedding_bytes))
        conn.commit()
        return texto_embedding


def buscar(texto):

    consulta = ""
    response = "argumentar_poco_mas"
    # Tokenizar el texto del usuario
    # Codificar las oraciones en un espacio semántico
    texto_embedding = obtener_embedding(texto)
    # Inicializar lista para almacenar los resultados de la similitud del coseno
    coseno_salida = []
    # Calcular la similitud coseno entre la consulta y todas las oraciones
    for s in sentencias:
        sentencia_embedding = obtener_embedding(s)
        coseno_similar = util.cos_sim(texto_embedding, sentencia_embedding)
        coseno_salida.append(coseno_similar.item())

    # Ordenar las oraciones según la similitud
    #resultados = zip(range(len(cosine_scores)), cosine_scores)
    #sorted_results = sorted(resultados, key=lambda x: x[1], reverse=True)
    #resultado_tensor = sorted_results[0][1]
    print(coseno_salida)
    posicionMax = maximo(coseno_salida)
    print(posicionMax,"   el maximo indice es")
    response = respuesta[posicionMax]
    print(response, "la respuesta es ")
    nombre_posicion_sql = ""
    if response:
        vec1=[]
        if response == "ver_carreras":
            carreras_encontradas = obtener_carreras_nombre(texto);
            if carreras_encontradas:
                vec1.append("si_car_n")
                # Obtener la primera carrera encontrada
                primera_carrera = carreras_encontradas.pop(0)
                nombre_posicion_sql = "ver_carreras_nombre"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql.format(primera_carrera)
            else:
                vec1.append("si_car")
                nombre_posicion_sql = "ver_carreras"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql
            vec1.append(nombre_posicion_sql)
            vec1.append(response)

        if response== "total_de_estudiantes":
            hay = "no"
            response = ""
            vec1=[]
            #puede decir el total de estudiante de la carrera infor
            carreras_encontradas = obtener_carreras_nombre(texto);
            if carreras_encontradas:#si existe algun nombre de carrera ingresa
                primera_carrera = carreras_encontradas.pop(0)
                nombre_posicion_sql = "total_de_estudiantes_carrera"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql.format(primera_carrera)
                hay  = 'si'
                vec1.append("total_es_car")
            if hay == 'no':
                nombre_posicion_sql = "total_de_estudiantes"
                sql = consultas_sql[nombre_posicion_sql]
                response = sql
                vec1.append("total_es_unsxx")
            vec1.append(nombre_posicion_sql)
            vec1.append(response)

        if response== "total_de_estudiantes_carrera":
            nombre_posicion_sql = "total_de_estudiantes_carrera"
            vec=[]
            vec1=[]
            response = ""
            contar_parametros=0
            sql = consultas_sql[nombre_posicion_sql]#obtenemos la cosulta
            #obtener el nombre de la carrera
            carreras_encontradas = obtener_carreras_nombre(texto)#enviamos el texto y buscamos si existe una carrera
            aux = ""
            if carreras_encontradas:#si existe algun nombre de carrera ingresa

                if len(carreras_encontradas)>1:#preguntamos si las carreras encotradas es mayor a 1
                    si  = "no"
                    for carr in carreras_encontradas:#recorremos todas las carreras y las concatenamos
                        if si == "no":
                            aux+=" cod_carrera = "+str(carr)
                            si = "si"
                        elif si == "si":
                            aux+=" or cod_carrera = "+str(carr)
                else:
                    aux = " cod_carrera = "+str(carreras_encontradas.pop(0))
            response = sql + " where "+aux
            vec1.append(nombre_posicion_sql)
            vec1.append(response)
        if response == "datos_especificos_estudiante":
            vec=[]
            vec1=[]
            response = ""
            contar_parametros=0
            carreras_encontradas = obtener_carreras_nombre(texto)
            if carreras_encontradas:#si hay carrera por lo menos entonces buscamos datos de la carrera

                nombre_posicion_sql = "datos_especificos_estudiante"
                sql = consultas_sql[nombre_posicion_sql]
                if carreras_encontradas:#si existe algun nombre de carrera ingresa
                    vec.append("si_car")
                else:
                    vec.append("no")
                    contar_parametros+=1
                nomb = encontrar_nombre(texto)#si existe algun nombre ingresa
                if nomb != "no":
                    vec.append("si_nom")
                else:
                    vec.append("no")
                    contar_parametros+=1
                ap = encontrar_apellido(texto)#si hay algun apellido ingresa
                if ap != "no":
                    vec.append("si_apell")
                else:
                    vec.append("no")
                si = "no"
                if contar_parametros>0:
                    response = "argumentar_poco_mas"
                else:
                    print(ap,"  esto son los apellidos")
                    for i in range(len(vec)):
                        vec1.append(vec[i])
                    vec1.append(nombre_posicion_sql)
                    for i in range(len(vec)):
                        if vec[i] == "si_car" and si == "no":
                            auxi = consultas_aux["nombre_carrera"]
                            primera_carrera = carreras_encontradas.pop(0)
                            response += auxi.format(primera_carrera)
                            si = "si"
                        elif vec[i] == "si_car" and si == "si":
                            auxi = consultas_aux["nombre_carrera"]
                            primera_carrera = carreras_encontradas.pop(0)
                            si = "si"
                            response += " and "+auxi.format(primera_carrera)
                        if vec[i] == "si_nom" and si == "no":
                            sql_aux = consultas_aux["nombre_es_especifico"]
                            response += sql_aux.format(nomb)
                            si = "si"
                        elif vec[i] == "si_nom" and si == "si":
                            sql_aux = consultas_aux["nombre_es_especifico"]
                            response += " and "+sql_aux.format(nomb)
                            si = "si"
                            #apellidos
                        if vec[i] == "si_apell" and si == "no":
                            if len(ap) == 1:#numero de apellidos maryor a 1
                                sql_aux = consultas_aux["apellido_p_es_especifico"]
                                response += sql_aux.format(ap[0])
                            elif len(ap)>1:
                                sql_aux = consultas_aux["apellido_p_es_especifico"]
                                response += sql_aux.format(ap[0])
                                sql_aux = consultas_aux["apellido_m_es_especifico"]
                                response += sql_aux.format(ap[1])
                            si = "si"
                        elif vec[i] == "si_apell" and si == "si":
                            if len(ap) == 1:#numero de apellidos maryor a 1
                                sql_aux = consultas_aux["apellido_p_es_especifico"]
                                response += " and "+sql_aux.format(ap[0])
                            elif len(ap)>1:
                                sql_aux = consultas_aux["apellido_p_es_especifico"]
                                response += " and "+sql_aux.format(ap[0])
                                sql_aux = consultas_aux["apellido_m_es_especifico"]
                                response += " or "+sql_aux.format(ap[1])
                            si = "si"
                    response = sql+" "+response
            else:
                response = "argumentar_poco_mas"
            vec1.append(response);
        if response == "estudiantes_de_unsxx":
            existe  ="no"
            response = ""
            vec = []
            contar_parametros=0
            nombre_posicion_sql = "estudiantes_de_unsxx"
            sql = consultas_sql[nombre_posicion_sql]
        #realizamos consultas de if para saber en  llega y poder el and o no
            if contiene_palabras_activas(texto) != "no":#si contiene la palabra activo ingresa
                vec.append("si_activo")
                contar_parametros=0
            else:
                vec.append("no")

            if contiene_palabras_desactivas(texto) != "no":#si contiene la palabra desactivo o al relacionado ingresa
                vec.append("si_desactivo")
                contar_parametros=0
            else:
                vec.append("no")
            if contiene_palabras_sexo_varon(texto) != "no":#si contiene la palabra sexo
                vec.append("si_m")
                contar_parametros+=1
            else:
                vec.append("no")
            if contiene_palabras_sexo_mujer(texto) != "no":#si contiene femenino ingresa
                vec.append("si_f")
                contar_parametros+=1
            else:
                vec.append("no")
            pr_encontrado = palabras_provincia(texto)#si contiene algun departamento ingresa
            if pr_encontrado != "no":
                vec.append("si_prov")
                contar_parametros+=1
            else:
                vec.append("no")

            dep_encontrado = palabras_departamento(texto)#buscamos si en el texto hay un departamento
            if dep_encontrado != "no":
                vec.append("si_dep")
                contar_parametros+=1
            else:
                vec.append("no")
            si = "no"
            vec1 = []
            if contar_parametros==0:
                response = "argumentar_poco_mas"
            else:
                for i in range(len(vec)):
                    vec1.append(vec[i])
                vec1.append(nombre_posicion_sql)
                for i in range(len(vec)):
                    if vec[i] == "si_activo" and si == "no":
                        response += consultas_aux["activo_es_unsxx"]
                        si = "si"
                    elif vec[i] == "si_activo" and si == "si":
                        response += " and "+consultas_aux["activo_es_unsxx"]
                        si = "si"

                    if vec[i] == "si_desactivo" and si == "no":
                        response += consultas_aux["desactivo_es_unsxx"]
                        si = "si"
                    elif vec[i] == "si_desactivo" and si == "si":
                        response += " and "+consultas_aux["desactivo_es_unsxx"]
                        si = "si"

                    if vec[i] == "si_m" and si == "no":
                        response += consultas_aux["sexo_es_m_unsxx"]
                        si = "si"
                    elif vec[i] == "si_m" and si == "si":
                        response += " and "+consultas_aux["sexo_es_m_unsxx"]
                        si = "si"

                    if vec[i] == "si_f" and si == "no":
                        response += consultas_aux["sexo_es_f_unsxx"]
                        si = "si"
                    elif vec[i] == "si_f" and si == "si":
                        response += " and "+consultas_aux["sexo_es_f_unsxx"]
                        si = "si"

                    if vec[i] == "si_prov" and si == "no":
                        sql_aux = consultas_aux["provincia_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(pr_encontrado)
                    elif vec[i] == "si_prov" and si == "si":
                        sql_aux = " and "+consultas_aux["provincia_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(pr_encontrado)
                    if vec[i] == "si_dep" and si == "no":
                        sql_aux = consultas_aux["departamento_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(dep_encontrado)
                    elif vec[i] == "si_dep" and si == "si":
                        sql_aux = " and "+consultas_aux["departamento_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(dep_encontrado)
                    print(vec[i],  si)
                    vec[i] = "no"
                    #print(vec[i])
                #print(response,"   eess")
                response = sql + response
            vec1.append(response)
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
        if response == "estudiante_por_area":#obtner estudiantes por area
            existe  ="no"
            response = ""
            vec = []
            contar_parametros=0
            nombre_posicion_sql = "estudiante_por_area"#creamos una varible para referenciar a mi array consultas_sql
            sql = consultas_sql[nombre_posicion_sql]#obtenemos la consulta
            #realizamos preguntas del texto ingresado para saber que es lo que busca el usuario

            if  contiene_palabras_activas(texto) != "no":#si contiene la palabra activo ingresa
                vec.append("si_activo")
                contar_parametros+=1
            else:
                vec.append("no")

            if contiene_palabras_desactivas(texto) != "no":#si contiene la palabra desactivo o al relacionado ingresa
                vec.append("si_desactivo")
                contar_parametros+=1
            else:
                vec.append("no")
            if contiene_palabras_sexo_varon(texto) != "no":#si contiene la palabra sexo
                vec.append("si_m")
                contar_parametros+=1
            else:
                vec.append("no")
            if contiene_palabras_sexo_mujer(texto) != "no":#si contiene femenino ingresa
                vec.append("si_f")
                contar_parametros+=1
            else:
                vec.append("no")
            pr_encontrado = palabras_provincia(texto)#si contiene algun departamento ingresa
            if pr_encontrado != "no":
                vec.append("si_prov")
                contar_parametros+=1
            else:
                vec.append("no")

            dep_encontrado = palabras_departamento(texto)#buscamos si en el texto hay un departamento
            if dep_encontrado != "no":
                vec.append("si_dep")
                contar_parametros+=1
            else:
                vec.append("no")

            desercion = palabra_desercion(texto)#buscamos palabras relacionados con desercion o relacionado
            if desercion != "no":
                vec.append("si_des")
                contar_parametros+=1
            else:
                vec.append("no")

            aplazar = palabra_aplazaron(texto)#buscamos palabras relacionados con aplazar
            print(aplazar,"  aplazadoss")
            if aplazar != "no":
                vec.append("si_apla")
                aplazar = "reprobado"
                contar_parametros+=1
            else:
                vec.append("no")

            aprobado = palabra_aprobados(texto)
            if aprobado != "no":
                vec.append("si_apro")
                aprobado = "aprobado"
                contar_parametros+=1
            else:
                vec.append("no")
            ar = obtener_area(texto)  # Supongamos que esto devuelve una lista de áreas
            if ar:
                vec.append("si_ar")  # Agrega "si_ar" a vec1 si se encontraron áreas en el texto
            else:
                vec.append("no")  # Agrega "no" a vec1 si no se encontraron áreas en el texto
            si = "no"
            vec1 = []
            unir = ""
            if contar_parametros==0:
                response = "argumentar_poco_mas"
            else:
                for i in range(len(vec)):
                    vec1.append(vec[i])

                for i in range(len(vec)):
                    if vec[i] == "si_activo" and si == "no":
                        response += consultas_aux["activo_es_unsxx"]
                        si = "si"
                    elif vec[i] == "si_activo" and si == "si":
                        response += " and "+consultas_aux["activo_es_unsxx"]
                        si = "si"

                    if vec[i] == "si_desactivo" and si == "no":
                        response += consultas_aux["desactivo_es_unsxx"]
                        si = "si"
                    elif vec[i] == "si_desactivo" and si == "si":
                        response += " and "+consultas_aux["desactivo_es_unsxx"]
                        si = "si"

                    if vec[i] == "si_m" and si == "no":
                        response += consultas_aux["sexo_es_m_unsxx"]
                        si = "si"
                    elif vec[i] == "si_m" and si == "si":
                        response += " and "+consultas_aux["sexo_es_m_unsxx"]
                        si = "si"

                    if vec[i] == "si_f" and si == "no":
                        response += consultas_aux["sexo_es_f_unsxx"]
                        si = "si"
                    elif vec[i] == "si_f" and si == "si":
                        response += " and "+consultas_aux["sexo_es_f_unsxx"]
                        si = "si"

                    if vec[i] == "si_prov" and si == "no":
                        sql_aux = consultas_aux["provincia_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(pr_encontrado)
                    elif vec[i] == "si_prov" and si == "si":
                        sql_aux = " and "+consultas_aux["provincia_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(pr_encontrado)
                    if vec[i] == "si_dep" and si == "no":
                        sql_aux = consultas_aux["departamento_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(dep_encontrado)
                    elif vec[i] == "si_dep" and si == "si":
                        sql_aux = " and "+consultas_aux["departamento_es_unsxx"]
                        si = "si"
                        response += sql_aux.format(dep_encontrado)
                    if vec[i] == "si_des" and si == "no":
                        sql_aux = consultas_aux["desercion"]
                        si = "si"
                        response+= sql_aux.format(desercion)
                    elif vec[i] == "si_des" and si=="si":
                        sql_aux = " and "+consultas_aux["desercion"]
                        si = "si"
                        response+= sql_aux.format(desercion)

                    if vec[i] == "si_apro" and  si == "no":
                        sql_aux = consultas_aux["aplazaron"]
                        si = "si"
                        response+= sql_aux.format(aprobado)
                    elif vec[i] == "si_apro" and si=="si":
                        sql_aux = " and "+consultas_aux["aplazaron"]
                        si = "si"
                        response+= sql_aux.format(aprobado)

                    if vec[i] == "si_apla" and  si == "no":
                        sql_aux = consultas_aux["aplazaron"]
                        si = "si"
                        response+= sql_aux.format(aplazar)
                    elif vec[i] == "si_apla" and si=="si":
                        sql_aux = " and "+consultas_aux["aplazaron"]
                        si = "si"
                        response+= sql_aux.format(aplazar)

                    if vec[i] == "si_ar" and si == "no":
                        sql_aux = consultas_aux["cod_area_cursa"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                        response += sql_aux.format(ar[0])  # Agrega la consulta auxiliar al response si es la primera iteración
                        unir+=str(ar[0])+"|"
                        si = "si"
                    elif vec[i] == "si_ar" and si == "si":
                        sql_aux = consultas_aux["cod_area_cursa"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                        unir+=str(ar[0])+"|"
                        response += " and " + sql_aux.format(ar[0])  # Agrega "or" y la consulta auxiliar al response para otras iteracpara otras iteraciones
                        si = "si"
                    print(vec[i],  si)
                    vec[i] = "no"
                    #print(vec[i])
                #print(response,"   eess")
                vec1.append(unir)
                vec1.append(nombre_posicion_sql)
                if si == "no":#si se mantienen en no entonces aumentamos WHERE
                    response = response
                else:
                    response=" where "+response

                response = sql + response
            vec1.append(response)

        if response == "seleccionar_asignatura_estudiante":
            vec = []
            vec1 = []
            response = "";
            contar_parametros = 0
            if palabra_nota(texto) != "no":
                vec.append("si_cali")
            else:
                vec.append("no")
            carreras_encontradas = obtener_carreras_nombre(texto);
            nombre_posicion_sql = "seleccionar_asignatura_estudiante"
            sql = consultas_sql[nombre_posicion_sql]

            if carreras_encontradas:#si existe algun nombre de carrera ingresa
                vec.append("si_car")
                contar_parametros+=1
            else:
                vec.append("no")
            nombre = "no"
            apellido = "no"
            nomb = encontrar_nombre(texto)#si existe algun nombre ingresa
            print(nomb)
            if nomb != "no":
                nombre = "si"
                contar_parametros+=1
            ap = encontrar_apellido(texto)#si hay algun apellido ingresa
            if ap != "no" and nombre == "si":
                apellido = "si"
            print(contar_parametros,"  los paramentso son ")
            if contar_parametros >= 2:
                if nombre == "si" or apellido == "si":
                    id_estudiante = seleccionar_estudiante1(nomb,ap,carreras_encontradas)#buscamos el id con el nombre y apellido del estudiante
                    print(id_estudiante,"   no hay estudiante")
                    if id_estudiante == "no":
                        vec.append("no")
                        vec1.append(nomb)
                        vec1.append(ap[0])
                    else:
                        vec.append("si_nom_apell")
                        vec1.append("")
                        vec1.append("")
                else:
                    vec.append("no")
                    vec1.append("")
                    vec1.append("")
                curso = palabra_curso(texto)
                id_curso = "no";
                id_curso=obtener_que_curso_quiere(texto)
                if curso != "no" or id_curso != "no" and  len(id_curso) != 0:#existe la palabra curso
                    vec.append("si_curso")
                else:
                    vec.append("no")
                si = "no"
                if contar_parametros == 0 and contar_parametros<=2:
                    response = "argumentar_poco_mas"
                else:
                    for i in range(len(vec)):
                        vec1.append(vec[i])
                    vec1.append(nombre_posicion_sql)

                    for i in range(len(vec)):
                        if vec[i] == "si_car" and si == "no":
                            sql_aux = consultas_aux["id_carrera"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                            response += sql_aux.format(carreras_encontradas[0])
                            si = "si"
                        elif vec[i] == "si_car" and si == "si":
                            sql_aux = consultas_aux["id_carrera"]  # Supongamos que consultas_aux es un diccionario con consultas auxiliares
                            response += " and "+sql_aux.format(carreras_encontradas[0])
                            si = "si"
                        if vec[i] == "si_nom_apell" and si == "no":
                            sql_aux = consultas_aux["id_estudiante"]
                            response+=sql_aux.format(id_estudiante)
                            si = "si"
                        elif vec[i] == "si_nom_apell" and si == "si":
                            sql_aux = consultas_aux["id_estudiante"]
                            response+=" and "+sql_aux.format(id_estudiante)
                            si = "si"

                        if vec[i] == "si_curso" and si == "no":
                            sql_aux = consultas_aux["id_grado"]
                            si = "si"
                            response+= sql_aux.format(id_curso.pop(0))
                        elif vec[i] == "si_curso" and si == "si":
                            sql_aux = consultas_aux["id_grado"]
                            si = "si"
                            response+= " and "+sql_aux.format(id_curso.pop(0))
                        vec[i] = "no"
                    if si == "no":#si se mantienen en no entonces aumentamos WHERE
                        response = response
                    else:
                        response=" where "+response
                    response = sql+response
                    vec1.append(nombre_posicion_sql)
            else:
                response = "argumentar_poco_mas"
            vec1.append(response)

        if response == "total_de_estudiantes_estadisticas":#obtener estadistica de estudiantes aprobados y reprobados
            vec = []
            vec1 = []
            response = "";
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

            nombre_posicion_sql = "total_de_estudiantes_estadisticas"
            sql = consultas_sql[nombre_posicion_sql]
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        if response == "seleccionar_estudiantes_desertores":
            vec = []
            vec1 = []#iniciamos los vectores para alamacenar
            response = "";
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

            nombre_posicion_sql = "seleccionar_estudiantes_desertores"
            sql = consultas_sql[nombre_posicion_sql]

            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)

        if response == "diferencia_entre_primero_quinto":
            vec = []
            vec1 = []#iniciamos los vectores para alamacenar
            response = "";
            #para contar si hay lo necesario para realizar la consulta sql
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

            nombre_posicion_sql = "diferencia_entre_primero_quinto"
            sql = consultas_sql[nombre_posicion_sql]
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        if response == "asignaturas_desercion":
            vec = []
            vec1 = []#iniciamos los vectores para alamacenar
            response = "";
            #para contar si hay lo necesario para realizar la consulta sql
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

            nombre_posicion_sql = "asignaturas_desercion"
            sql = consultas_sql[nombre_posicion_sql]
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        if response == "clasificado_sexo":
            vec = []
            vec1 = []#iniciamos los vectores para alamacenar
            response = "";
            #para contar si hay lo necesario para realizar la consulta sql
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

            nombre_posicion_sql = "clasificado_sexo"
            sql = consultas_sql[nombre_posicion_sql]
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        if response == "transferencias_buscar":
            vec = []
            vec1 = []#iniciamos los vectores para alamacenar
            response = "";
            #para contar si hay lo necesario para realizar la consulta sql
            fecha = fechas(texto)
            if len(fecha) >= 1:#si existe fechas
                vec.append("si_fecha")
                if len(fecha) == 1:
                    fecha1 = fecha[0]
                    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
                    anio = obtener_ano_de_fecha(fecha_formateada)
                    fecha2 = anio+"-12-30"
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

            nombre_posicion_sql = "transferencias_buscar"
            sql = consultas_sql[nombre_posicion_sql]
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        if response == "concepto_transferencia":
            vec = []
            vec1 = []#iniciamos los vectores para alamacenar
            response = "";
            #para contar si hay lo necesario para realizar la consulta sql
            fecha = fechas(texto)
            if len(fecha) >= 1:#si existe fechas
                vec.append("si_fecha")
                if len(fecha) == 1:
                    fecha1 = fecha[0]
                    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
                    anio = obtener_ano_de_fecha(fecha_formateada)
                    fecha2 = anio+"-12-30"
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

            nombre_posicion_sql = "concepto_transferencia"
            sql = consultas_sql[nombre_posicion_sql]
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        if response == "mayor_inscritos":
            vec = []
            vec1 = []#iniciamos los vectores para alamacenar
            response = "";
            #para contar si hay lo necesario para realizar la consulta sql
            fecha = fechas(texto)
            if len(fecha) >= 1:#si existe fechas
                vec.append("si_fecha")
                if len(fecha) == 1:
                    fecha1 = fecha[0]
                    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
                    anio = obtener_ano_de_fecha(fecha_formateada)
                    fecha2 = anio+"-12-30"
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

            nombre_posicion_sql = "mayor_inscritos"
            sql = consultas_sql[nombre_posicion_sql]
            si = "no"
            if fecha2 == "" and fecha1 != "":
                vec1.append(fecha1)
                vec1.append(fecha1)
            else:
                vec1.append(fecha1)
                vec1.append(fecha2)
            for i in range(len(vec)):
                if vec[i] == "si_fecha" and si == "no":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                elif vec[i] == "si_fecha" and si == "si":
                    if fecha1 != "":#si es diferente de vacio
                        sql_aux = consultas_aux["fechai"]
                        response+=" and ( "+sql_aux.format(fecha1)
                    if fecha2 != "":
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha2)+")"
                    else:
                        sql_aux = consultas_aux["fechaf"]
                        response+=" and "+sql_aux.format(fecha1)+")"
                    si = "si"
                vec[i] = "no"
            if si == "no":#si se mantienen en no entonces aumentamos WHERE
                response = response
            else:
                response=" where "+response
            vec1.append(nombre_posicion_sql)
            response = sql + response
            vec1.append(response)
        return vec1
    else:
        vec1=[]
        vec1.append("argumentar_poco_mas")
        return vect1
