# reporte.py

from weasyprint import HTML

def generar_reporte():
    # Aquí iría tu código para generar el reporte con WeasyPrint
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte</title>
    </head>
    <body>
        <h1>Este es un reporte generado con WeasyPrint</h1>
        <!-- Aquí iría el contenido del reporte -->
    </body>
    </html>
    """
    HTML(string=html_content).write_pdf("reporte.pdf")

if __name__ == "__main__":
    generar_reporte()
