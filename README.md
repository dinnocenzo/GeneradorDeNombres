# Generador de nombres para empresas

Proyecto #1 del curso de Python con IA. Propone nombres para una empresa a partir del rubro y el país, usando una base de datos propia o la API de Claude para resultados más creativos.

**Demo en vivo → [dinnocenzo.github.io/GeneradorDeNombres](https://dinnocenzo.github.io/GeneradorDeNombres/)**

## Versiones

| Versión | Archivo | Cómo ejecutar |
|---|---|---|
| Web (estática) | `index.html` | Abrí la demo o cualquier servidor local |
| CLI (Python) | `generador-nombres/generador_nombres.py` | `python generador_nombres.py` |
| Web app (Streamlit) | `generador-nombres/app.py` | `streamlit run app.py` |

## Instalación (CLI y Streamlit)

```bash
cd generador-nombres
pip install -r requirements.txt
```

Requiere Python 3.8+.

## Usar la IA

Las versiones web y CLI pueden generar nombres con **Claude Opus** de Anthropic.

1. Creá una API key en [console.anthropic.com](https://console.anthropic.com/settings/api-keys)
2. En la versión web: pegala en el campo "API Key" de la página
3. En la versión CLI/Streamlit: configurá la variable de entorno antes de ejecutar:

```bash
# Windows
set ANTHROPIC_API_KEY=sk-ant-...

# macOS / Linux
export ANTHROPIC_API_KEY=sk-ant-...
```

## Estructura

```
GeneradorDeNombres/
├── index.html                        # versión web (GitHub Pages)
└── generador-nombres/
    ├── generador_nombres.py          # CLI
    ├── app.py                        # Streamlit
    ├── datos.json                    # rubros, países y sufijos
    └── requirements.txt
```

## Conceptos aplicados

- Leer y combinar datos desde JSON
- `random.choice()` y `set()` para opciones únicas
- Normalización de texto con `unicodedata`
- Integración con la API de Claude (`anthropic` SDK)
- Interfaz web con Streamlit
- Página estática con HTML, CSS y JavaScript puro
- Deploy en GitHub Pages

## Licencia

MIT
