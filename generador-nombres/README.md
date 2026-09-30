# Generador de nombres para empresas

Programa en Python que propone nombres para una empresa a partir de dos preguntas: **rubro** y **país**.
En lugar de repetir lo que escribe el usuario, busca palabras relacionadas en una pequeña base de datos (`datos.json`) y las combina.

Proyecto #1 de mi curso de Python con IA.

## Ejemplo

```
=== Generador de nombres para empresas ===

¿A qué rubro se dedica tu empresa? Tecnología
¿De qué país sos? Argentina

Opciones para una empresa de tecnologia en Argentina:
  1. Byte Pampa Labs
  2. Patagonia Nexo Studio
  3. PixelAndes
  4. Sync Criollo Hub
  5. Tango Logic Co.
```

(Los resultados cambian cada vez porque se eligen al azar.)

## Cómo ejecutarlo

Necesitás Python 3.8 o superior. No hay que instalar nada extra.

```bash
python generador_nombres.py
```

## Qué aprendí / conceptos usados

- `input()` y `print()` para interactuar con el usuario
- f-strings y `str.format()`
- Diccionarios y listas como base de datos
- Leer archivos JSON con el módulo `json`
- `random.choice()` y `set()` para generar opciones únicas
- Normalizar texto (quitar tildes y mayúsculas) con `unicodedata`
- Validación de entradas con un bucle `while`
- Funciones y `if __name__ == "__main__"`

## Estructura

```
generador-nombres/
├── generador_nombres.py   # el programa
├── datos.json             # palabras por rubro, por país y sufijos
└── README.md
```

## Cómo agregar rubros o países

Abrí `datos.json` y sumá una entrada nueva con una lista de palabras (sin tildes en la clave):

```json
"rubros": {
  "mascotas": ["Huella", "Pata", "Colita", "Mimo"]
}
```

## Ideas para mejorar

- Guardar la base de datos en SQLite en vez de JSON
- Guardar los nombres favoritos en un archivo
- Usar una API de IA para generar nombres más creativos
- Crear una versión web con Flask o Streamlit
