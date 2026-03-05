#Estructura de Datos
gente = []

#POO
class personas:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Agregamos datos
gente.append(personas(input("Nombre 1: "), int(input("Edad 1: "))))
gente.append(personas(input("Nombre 2: "), int(input("Edad 2: "))))
gente.append(personas(input("Nombre 3: "), int(input("Edad 3: "))))

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