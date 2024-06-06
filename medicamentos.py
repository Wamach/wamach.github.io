from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime, timedelta

def ingresar_medicamento():
    # Solicitar al usuario que ingrese los datos de un medicamento
    print("Ingresa todos los datos del medicamento")
    inicio_str = input("Fecha y hora de inicio del medicamento (YYYY-MM-DD HH:MM): ")
    nombre_medicamento = input("El nombre del medicamento: ")
    frecuencia_str = input("Frecuencia de consumo en horas: ")
    duracion_str = input("Duración del tratamiento en días: ")

    # Convertir las cadenas de entrada en tipos de datos apropiados
    inicio_medicamento = datetime.strptime(inicio_str, "%Y-%m-%d %H:%M")
    frecuencia_consumo_horas = int(frecuencia_str)
    duracion_dias = int(duracion_str)

    return inicio_medicamento, nombre_medicamento, frecuencia_consumo_horas, duracion_dias

# Lista para almacenar los medicamentos
medicamentos = []

# Bucle para agregar medicamentos
while True:
    print("\n¿Quiere agregar un medicamento?")
    opcion = input("Escriba 1 para agregar un medicamento, 0 para terminar: ")
    if opcion == '0':
        break
    elif opcion == '1':
        print("\nIngrese los datos del medicamento:")
        datos_medicamento = ingresar_medicamento()
        medicamentos.append(datos_medicamento)
    else:
        print("Opción no válida. Por favor, escriba 1 o 0.")

# Organizar los medicamentos en un diccionario de medicamentos por fecha y hora
medicamentos_por_fecha_hora = {}
for medicamento in medicamentos:
    inicio_medicamento, nombre_medicamento, frecuencia_consumo_horas, duracion_dias = medicamento
    fecha_final = inicio_medicamento + timedelta(days=duracion_dias)
    siguiente_toma = inicio_medicamento
    while siguiente_toma < fecha_final:
        # Solo agregar medicamentos programados para después de la fecha actual
        if siguiente_toma >= datetime.now():
            fecha_hora = siguiente_toma.strftime('%Y-%m-%d %H:%M')
            if fecha_hora not in medicamentos_por_fecha_hora:
                medicamentos_por_fecha_hora[fecha_hora] = []
            medicamentos_por_fecha_hora[fecha_hora].append(nombre_medicamento)
        siguiente_toma += timedelta(hours=frecuencia_consumo_horas)

# Ordenar los medicamentos por fecha y hora
medicamentos_ordenados = sorted(medicamentos_por_fecha_hora.items(), key=lambda x: x[0])

# Crear el documento PDF
pdf_filename = "programa_medicacion.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Crear la tabla y establecer estilos
table_data = [["Fecha", "Día", "Hora", "Medicamento"]]
for fecha_hora, medicamentos in medicamentos_ordenados:
    fecha, hora = fecha_hora.split(' ')
    nombres = ", ".join(medicamentos)
    # Obtener el día de la semana correspondiente a la fecha
    dia_semana_ingles = datetime.strptime(fecha, '%Y-%m-%d').strftime('%A')
    # Mapear el nombre del día de la semana a español
    dias_semana_espanol = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
    dia_semana = dias_semana_espanol.get(dia_semana_ingles, dia_semana_ingles)
    table_data.append([fecha, dia_semana, hora, nombres])

table = Table(table_data)
style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])

table.setStyle(style)

# Espaciamiento uniforme entre las filas y columnas
table.spaceBefore = 20
table.spaceAfter = 20
table.setStyle(TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
]))

# Agregar la tabla al documento PDF
doc.build([table])

print("Documento PDF generado:", pdf_filename)