"""Generador de nombres para empresas.

Le pregunta al usuario el rubro y el país, busca palabras relacionadas
en datos.json y las combina para proponer varias opciones de nombre.
También puede usar la API de Claude para generar nombres más creativos.
"""

import json
import random
import unicodedata
from pathlib import Path

import anthropic

RUTA_DATOS = Path(__file__).parent / "datos.json"
CANTIDAD_OPCIONES = 5
MODELO_IA = "claude-opus-4-8"

# Distintas formas de combinar: r = palabra del rubro, p = del país, s = sufijo
FORMATOS = ["{r} {p} {s}", "{p} {r} {s}", "{r} {p}"]


def cargar_datos(ruta=RUTA_DATOS):
    """Lee la base de datos (archivo JSON) y la devuelve como diccionario."""
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)


def normalizar(texto):
    """Pasa a minúsculas y quita espacios y tildes: ' México ' -> 'mexico'."""
    texto = texto.strip().lower()
    descompuesto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in descompuesto if unicodedata.category(c) != "Mn")


def pedir_opcion(pregunta, disponibles):
    """Repite la pregunta hasta que la respuesta esté en la base de datos."""
    while True:
        respuesta = normalizar(input(pregunta))
        if respuesta in disponibles:
            return respuesta
        print("No tengo ese dato todavía. Opciones disponibles:")
        print("  " + ", ".join(sorted(disponibles)))


def generar_nombres(rubro, pais, datos, cantidad=CANTIDAD_OPCIONES):
    """Devuelve una lista de nombres únicos combinando palabras al azar."""
    palabras_rubro = datos["rubros"][rubro]
    palabras_pais = datos["paises"][pais]
    sufijos = datos["sufijos"]

    nombres = set()  # el set evita repetidos
    while len(nombres) < cantidad:
        nombre = random.choice(FORMATOS).format(
            r=random.choice(palabras_rubro),
            p=random.choice(palabras_pais),
            s=random.choice(sufijos),
        )
        nombres.add(nombre)
    return sorted(nombres)


def generar_nombres_ia(rubro, pais, cantidad=CANTIDAD_OPCIONES):
    """Llama a la API de Claude para generar nombres creativos."""
    cliente = anthropic.Anthropic()
    prompt = (
        f"Generá {cantidad} nombres creativos y únicos para una empresa "
        f"del rubro '{rubro}' en {pais.title()}.\n"
        "Requisitos:\n"
        "- Memorables y originales\n"
        "- Que reflejen la identidad del país o del rubro\n"
        "- Entre 1 y 3 palabras cada nombre\n"
        "Devolvé solo los nombres, uno por línea, sin numeración ni explicaciones."
    )
    respuesta = cliente.messages.create(
        model=MODELO_IA,
        max_tokens=256,
        thinking={"type": "adaptive"},
        messages=[{"role": "user", "content": prompt}],
    )
    texto = next(b.text for b in respuesta.content if b.type == "text")
    nombres = [linea.strip() for linea in texto.strip().splitlines() if linea.strip()]
    return nombres[:cantidad]


def main():
    datos = cargar_datos()

    print("=== Generador de nombres para empresas ===\n")

    while True:
        rubro = pedir_opcion("¿A qué rubro se dedica tu empresa? ", datos["rubros"])
        pais = pedir_opcion("¿De qué país sos? ", datos["paises"])

        usar_ia = normalizar(input("¿Usar IA para generar nombres? (s/n) ")) in ("s", "si")

        print(f"\nOpciones para una empresa de {rubro} en {pais.title()}:")

        if usar_ia:
            print("(Generando con IA, puede tardar unos segundos...)\n")
            try:
                nombres = generar_nombres_ia(rubro, pais)
            except anthropic.AuthenticationError:
                print("Error: no se encontró la API key de Anthropic.")
                print("Configurá la variable de entorno ANTHROPIC_API_KEY y volvé a intentarlo.")
                print("Usando el método clásico como alternativa...\n")
                nombres = generar_nombres(rubro, pais, datos)
        else:
            nombres = generar_nombres(rubro, pais, datos)

        for numero, nombre in enumerate(nombres, start=1):
            print(f"  {numero}. {nombre}")

        otra = input("\n¿Querés generar más nombres? (s/n) ")
        if normalizar(otra) not in ("s", "si"):
            print("¡Éxitos con tu empresa!")
            break
        print()


if __name__ == "__main__":
    main()
