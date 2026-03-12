#Estructura de Datos
from base_datos import add_person, list_people, find_person

#POO
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# carga la información existente de la "base de datos" JSON
gente = [Persona(p["nombre"], p["edad"]) for p in list_people()]

# pedir tres registros nuevos y guardarlos en la base de datos
for i in range(1, 4):
    nombre = input(f"Nombre {i}: ")
    edad = int(input(f"Edad {i}: "))
    add_person(nombre, edad)
    gente.append(Persona(nombre, edad))

# Generar contenido HTML
contenido = """
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Gente</title>
    <style>
        body { font-family: Papyrus; text-align: center; background: #00CC00; }
        table { margin: auto; border-collapse: collapse; }
        th, td { padding: 10px; border: 1px solid black; }
        th { background: #4CAF50; color: white; }
    </style>
</head>
<body>
    <h1>Lista de Gente</h1>
    <table>
        <tr>
            <th>Nombre</th>
            <th>Edad</th>
        </tr>
"""
#Ciclo de la programación estructurada
for persona in gente:
    contenido += f"""
        <tr>
            <td>{persona.nombre}</td>
            <td>{persona.edad}</td>
        </tr>
    """
    contenido += """
    </table>
</body>
</html>
"""

# Crear archivo index.html
with open("index.html", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print("Archivo index.html generado correctamente.")

# ejemplo de búsqueda usando la base de datos
consulta = input("\nBuscar persona por nombre (o presione ENTER para saltar): ")
if consulta:
    resultado = find_person(consulta)
    if resultado:
        print(f"Encontrado: {resultado['nombre']} - {resultado['edad']} años")
    else:
        print("No se encontró ninguna persona con ese nombre.")