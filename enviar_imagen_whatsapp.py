import time

import pandas as pd
import pywhatkit as kit

# Ruta al archivo Excel y a la imagen
ruta_excel = "numeros.xlsx"      # Nombre de archivo xlsx con los números
columna = "tel"                  # Nombre de la columna con los números
ruta_imagen = "imagen.jpg"       # Imagen a enviar
codigo_pais = "+52"              # Código de México

# Cargar el Excel
df = pd.read_excel(ruta_excel)

# Enviar imagen a cada número
for index, row in df.iterrows():
    numero = str(row[columna])
    
    # Validar que tenga 10 dígitos y agregar el código de país
    if len(numero) == 10 and numero.isdigit():
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
            # Espera antes de mandar al siguiente número
            time.sleep(15)  
        except Exception as e:
            print(f"Error al enviar a {numero_completo}: {e}")
    else:
        print(f"Número inválido: {numero}")
