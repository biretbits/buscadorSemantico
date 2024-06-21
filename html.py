import tempfile
import webbrowser
import platform
from weasyprint import HTML

# Definir el contenido HTML de la tabla
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, tdffffff {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>

<h2>Ejemplo de tabla con WeasyPrint</h2>

<table>
  <tr>
    <th>Nombre</th>
    <th>Edad</th>
    <th>Ciudad</th>
  </tr>
  <tr>
    <td>Carlos</td>
    <td>30</td>
    <td>Madrid</td>
  </tr>
  <tr>
    <td>Ana</td>
    <td>25</td>
    <td>Barcelona</td>
  </tr>
  <tr>
    <td>Pablo</td>
    <td>35</td>
    <td>Valencia</td>
  </tr>
</table>

</body>
</html>
"""

# Generar el PDF con WeasyPrint y guardar temporalmente
pdf_file = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
HTML(string=html_content).write_pdf(pdf_file.name)

# Abrir el PDF en el navegador predeterminado
system = platform.system()
if system == "Darwin":  # macOS
    webbrowser.open("file://" + pdf_file.name)
elif system == "Windows":
    webbrowser.open(pdf_file.name, new=2)
else:  # Linux u otro sistema
    webbrowser.open("file://" + pdf_file.name)
