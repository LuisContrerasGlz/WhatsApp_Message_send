# 📦 Sistema de Envío Masivo de Imágenes por WhatsApp

Este proyecto permite enviar **una imagen personalizada a miles de números de teléfono** mediante WhatsApp Web, utilizando listas en archivos Excel (`.xlsx`). Es ideal para promociones, recordatorios o comunicación directa con clientes.

---

## ✅ Requisitos previos

Antes de ejecutar este sistema asegúrate de tener lo siguiente:

- ✅ [Python 3.10 o superior](https://www.python.org/downloads/)
- ✅ [Google Chrome](https://www.google.com/chrome/)
- ✅ Cuenta de WhatsApp activa
- ✅ Imagen llamada exactamente `imagen.jpg`
- ✅ Uno o varios archivos `.xlsx` con la lista de números (10 dígitos sin espacios)
- ✅ [GOUST VPN](https://goustvpn.com/) u otra VPN activa (opcional pero recomendado)

---

## 📁 Estructura del proyecto

```
WhatsApp_Message_send/
│
├── enviar_mensaje.py              # Script principal
├── imagen.jpg                     # Imagen a enviar (reemplazable)
├── listas/                        # Carpeta con archivos Excel (lista1.xlsx, lista2.xlsx, etc.)
├── logs/                          # Se crean automáticamente; guardan enviados y errores
├── venv/                          # Entorno virtual Python
├── .gitignore                     # Para excluir carpetas innecesarias
└── README.md                      # Esta guía
```

---

## 📄 Formato del archivo Excel

Cada archivo `.xlsx` debe tener **una sola hoja** con una columna llamada:

```
tel
```

Ejemplo:

| tel        |
|------------|
| 4491234567 |
| 5567890123 |
| 8123456789 |

---

## 🚀 Instrucciones de uso (modo básico)

### 1. Clonar o copiar el proyecto

Copia la carpeta completa en cualquier computadora con Windows o macOS.

### 2. Activar el entorno virtual

Desde la terminal:

```bash
# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias (solo la primera vez)

```bash
pip install -r requirements.txt
```

O bien:

```bash
pip install pandas pywhatkit openpyxl
```

### 4. Abrir WhatsApp Web

- Abre Google Chrome en modo incógnito (`Ctrl + Shift + N`)
- Ve a [https://web.whatsapp.com](https://web.whatsapp.com)
- Escanea el código QR desde el celular

### 5. Ejecutar el sistema

```bash
python enviar_mensaje.py
```

---

## 🔁 Funcionalidades avanzadas

- ✅ **Lectura de múltiples archivos Excel** en orden (lista1, lista2, lista3...)
- ✅ **Control de reintentos** con archivos `.txt` para saber qué ya se envió
- ✅ **Pausa configurable entre envíos** (`time.sleep`)
- ✅ **Reanudación automática** desde donde se quedó si algo falla
- ✅ **Soporte para ejecución en paralelo desde varias computadoras**

---

## 🧠 Buenas prácticas

- Usa un número de WhatsApp **exclusivo** para envíos.
- Conéctate a través de una VPN confiable.
- No envíes más de **500–1000 mensajes por sesión**.
- Cambia la imagen y los Excel según campaña.

---

## ⚠️ Importante

Este sistema **no usa ni requiere que los números estén en tus contactos**.  
Solo necesitas que el número esté **correctamente escrito** (10 dígitos sin espacios ni símbolos).

---

## 📂 Archivos ignorados (.gitignore)

```gitignore
venv/
__pycache__/
*.log
logs/
.DS_Store
*.done
```

---

## 👥 Guía rápida para usuarios no técnicos

### Paso 1 – Colocar la imagen
Coloca una imagen en la carpeta principal del proyecto con el nombre **`imagen.jpg`**.

### Paso 2 – Copiar tus archivos de Excel
Copia tus archivos con nombre como `lista1.xlsx`, `lista2.xlsx`, etc. dentro de la carpeta **`listas/`**.

### Paso 3 – Ejecutar el sistema
1. Abre **Visual Studio Code**
2. Abre la terminal integrada
3. Escribe:

```bash
venv\Scripts\activate
python enviar_mensaje.py
```

Presiona **Enter**. WhatsApp Web se abrirá en el navegador. Escanea el código QR y se iniciará el envío automático.

---

## 🧑‍💻 Autor y licencia

Desarrollado por: **[Tu nombre o alias]**  
Licencia: Uso privado y educativo
