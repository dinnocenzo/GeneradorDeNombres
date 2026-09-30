import streamlit as st
import anthropic

from generador_nombres import cargar_datos, generar_nombres, generar_nombres_ia

st.set_page_config(
    page_title="Generador de nombres para empresas",
    layout="centered",
)

st.title("Generador de nombres para empresas")

datos = cargar_datos()

col1, col2 = st.columns(2)
with col1:
    rubro = st.selectbox("Rubro", sorted(datos["rubros"].keys()), format_func=str.title)
with col2:
    pais = st.selectbox("País", sorted(datos["paises"].keys()), format_func=str.title)

usar_ia = st.checkbox("Usar IA (Claude Opus)", value=True)

if st.button("Generar nombres", type="primary", use_container_width=True):
    if usar_ia:
        with st.spinner("Generando con IA..."):
            try:
                nombres = generar_nombres_ia(rubro, pais)
                st.caption("Generado con Claude Opus")
            except anthropic.AuthenticationError:
                st.warning(
                    "No se encontró la variable ANTHROPIC_API_KEY. "
                    "Usando el método clásico como alternativa."
                )
                nombres = generar_nombres(rubro, pais, datos)
    else:
        nombres = generar_nombres(rubro, pais, datos)

    st.subheader(f"Opciones para una empresa de {rubro} en {pais.title()}:")
    for i, nombre in enumerate(nombres, 1):
        st.write(f"**{i}.** {nombre}")
