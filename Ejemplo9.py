nombreArchivo=input("Ingrese el # de Cedula:")
nombreEstudiante=input("Ingrese el nombre del Estudiante ")
nombreArchivo=nombreArchivo+".txt"

notas=[] 
#print(type(notas))
#[] diccionario, () Tuplas, {} Conjuntos, {} Diccionario
x=1
while True:
    notas.append("\n"+input(f"Introduzca las calificacion N{x}:"))
    x+=1
    opc=input("Introduzca 1 para continuar ")
    if opc!="1":
        break

with open(nombreArchivo,"w") as archivo:
    archivo.write("Calificaciones del estudiante: "+nombreEstudiante)
    archivo.writelines(notas)