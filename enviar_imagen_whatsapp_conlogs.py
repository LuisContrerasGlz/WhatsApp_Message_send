import os
import time

import pandas as pd
import pywhatkit as kit

# Ruta al archivo Excel y a la imagen
ruta_excel = "numeros.xlsx"
columna = "tel"
ruta_imagen = "imagen.jpg"
codigo_pais = "+52"
espera_segundos = 15  # puedes ajustar este valor fácilmente

# Archivos de log
log_ok = "envios_exitosos.txt"
log_fail = "envios_fallidos.txt"

# Limpiar logs anteriores
open(log_ok, "w").close()
open(log_fail, "w").close()

# Cargar Excel
df = pd.read_excel(ruta_excel)

# Enviar imagen a cada número
for index, row in df.iterrows():
    numero = str(row[columna]).strip()

    if not numero or not numero.isdigit() or len(numero) != 10:
        print(f"Número inválido: {numero}")
        with open(log_fail, "a") as f:
            f.write(f"{numero} - Número inválido\n")
        continue

    numero_completo = codigo_pais + numero
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

        time.sleep(espera_segundos)

    except Exception as e:
        print(f"Error al enviar a {numero_completo}: {e}")
        with open(log_fail, "a") as f:
            f.write(f"{numero_completo} - {str(e)}\n")
