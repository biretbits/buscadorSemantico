import random
import pymysql

def seleccionar():
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "select * from dicta_asignatura where cod_grado = 5 and cod_carrera = 1;"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)
    estudiante = cursor.fetchall()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    return estudiante
def seleccionar_docente():
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "select * from docente where cod_carrera=1;"
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)
    estudiante = cursor.fetchall()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    return estudiante
def seleccionar_estudiante():
    # Conexión a la base de datos
    conn = pymysql.connect(host='localhost', user='unsxx', password='123', database='academico')

    cursor = conn.cursor()
    # Consulta SQL para obtener el embedding
    sql_consulta = "select * from estudiante where cod_carrera=1 "
    # Ejecutar la consulta SQL
    cursor.execute(sql_consulta)
    estudiante = cursor.fetchall()
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    return estudiante
def crear2():
    html = ""
    conta = 1
    v = [8,8,13,13,4,0]
    curso = 1
    k = 0
    desercion = "no"
        
    estu =seleccionar_estudiante()
    suma = 0
    for estudiante in estu:
        
        sel = seleccionar_docente()
        estado = "aprobado"
        abandono = 'no'
        p =0
        html+="insert into estudiante_perdio(estado_ano,abandono,cod_grado,cod_carrera,"
        html+="cod_es,cod_area,fecha,nota)values("
        if suma%5==0:
            estado = 'aprobado'
            abandono='si'
        else:
            estado ='reprobado'
            abandono='no'
        nota = 45
        if estado == "reprobado":
            nota = random.randint(0,50)
        else:
            nota =random.randint(51,100) 
        html+="'"+str(estado)+"','"+str(abandono)+"',"+str(estudiante[14])+","+str(estudiante[13])+","
        html+=str(estudiante[0])+","+str(estudiante[12])+",'2020-02-03',"+str(nota)+");"
        suma+=1
    with open("mi_archivo.txt", "w") as archivo:
        # Escribe la variable 'datos' en el archivo
        archivo.write(html)
      
def crear():
    html = ""
    conta = 1
    v = [8,8,13,13,4,0]
    curso = 1
    k = 0
   
    estu = seleccionar_estudiante()
    for estudiante in estu:
        desercion = "no"
        estado = 'activo'
        suma = 0
        if k%3 == 0:
            desercion = 'si'
        if k%5==0:
            estado = 'desactivo'
        sel = seleccionar()
        for fila in sel:
            for j in range(4):
                if j !=0:
                    html+="insert into cursa_asignatura(ano,calificacion,estado_asignatura,desercion,"
                    html+="cod_es,cod_dicta,cod_docente,cod_asig,cod_pe,cod_carrera,"
                    html+="cod_grado,cod_area,estado,fecha,teoria,"
                    html+="investigacion,extencion,cod_parcial)values("
                   
                    valor1 = random.randint(48,100)
                    
                    valor2 = random.randint(25,100)
                  
                    valor3 = random.randint(48,100)
                    suma+= (valor1+valor2+valor3)/3
                    
                    html+="2024,0,'"+estado+"','"+desercion+"',"
                    html+=str(estudiante[0])+","+str(fila[0])+","
                    html+=str(fila[3])+","+str(fila[4])+","+str(fila[5])+","
                    html+=str(fila[6])+","+str(fila[7])+","+str(fila[8])+","
                    html+="'activo','2024-03-04',"+str(valor1)+","+str(valor2)+","+str(valor3)+","+str((j+1))+");"
            valor1 = random.randint(45,100)
            valor2 = random.randint(48,100)
            valor3 = random.randint(48,100)
            suma+= (valor1+valor2+valor3)/3
            total = 0
            total = suma/4
            html+="insert into cursa_asignatura(ano,calificacion,estado_asignatura,desercion,"
            html+="cod_es,cod_dicta,cod_docente,cod_asig,cod_pe,cod_carrera,"
            html+="cod_grado,cod_area,estado,fecha,teoria,"
            html+="investigacion,extencion,cod_parcial)values("
            html+="2024,"+str(int(total))+",'"+estado+"','"+desercion+"',"
            html+=str(estudiante[0])+","+str(fila[0])+","
            html+=str(fila[3])+","+str(fila[4])+","+str(fila[5])+","
            html+=str(fila[6])+","+str(fila[7])+","+str(fila[8])+","
            html+="'activo','2024-03-04',"+str(valor1)+","+str(valor2)+","+str(valor3)+",1);"
        k=k+1
    with open("mi_archivo.txt", "w") as archivo:
        # Escribe la variable 'datos' en el archivo
        archivo.write(html)
      

crear2()