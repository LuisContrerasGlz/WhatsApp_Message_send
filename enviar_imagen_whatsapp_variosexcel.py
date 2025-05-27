import os
import time

import pandas as pd
import pywhatkit as kit

# Configuración
carpeta_excels = "listas"
carpeta_logs = "logs"
ruta_imagen = "imagen.jpg"
codigo_pais = "+52"
columna = "tel"
espera_segundos = 15

# Crear carpeta de logs si no existe
os.makedirs(carpeta_logs, exist_ok=True)

# Obtener todos los archivos Excel en la carpeta
archivos_excel = [f for f in os.listdir(carpeta_excels) if f.endswith(".xlsx")]

for archivo in archivos_excel:
    ruta_archivo = os.path.join(carpeta_excels, archivo)
    nombre_base = os.path.splitext(archivo)[0]
    
    log_ok = os.path.join(carpeta_logs, f"{nombre_base}_exitosos.txt")
    log_fail = os.path.join(carpeta_logs, f"{nombre_base}_fallidos.txt")
    
    # Cargar registros anteriores si existen
    enviados = set()
    if os.path.exists(log_ok):
        with open(log_ok, "r") as f:
            enviados = set(line.strip() for line in f.readlines())

    print(f"Procesando archivo: {archivo}")
    
    try:
        df = pd.read_excel(ruta_archivo)
    except Exception as e:
        print(f"Error al leer {archivo}: {e}")
        continue

    total_enviados = 0
    total_fallidos = 0

    for index, row in df.iterrows():
        numero = str(row.get(columna, "")).strip()

        if not numero or not numero.isdigit() or len(numero) != 10:
            print(f"Número inválido: {numero}")
            with open(log_fail, "a") as f:
                f.write(f"{numero} - Número inválido\n")
            total_fallidos += 1
            continue

        numero_completo = codigo_pais + numero

        if numero_completo in enviados:
            print(f"Ya enviado previamente: {numero_completo}")
            continue

        print(f"Enviando imagen a {numero_completo}...")

        try:
            kit.sendwhats_image(
                receiver=numero_completo,
                img_path=ruta_imagen,
                caption="¡Hola! Te comparto esta imagen.",
                tab_close=True,
                close_time=3
            )

            with open(log_ok, "a") as f:
                f.write(f"{numero_completo}\n")
            enviados.add(numero_completo)
            total_enviados += 1

            time.sleep(espera_segundos)

        except Exception as e:
            print(f"Error al enviar a {numero_completo}: {e}")
            with open(log_fail, "a") as f:
                f.write(f"{numero_completo} - {str(e)}\n")
            total_fallidos += 1

    print(f"\nResumen de {archivo}:")
    print(f"Total enviados: {total_enviados}")
    print(f"Total fallidos: {total_fallidos}")
    print("-" * 40)
