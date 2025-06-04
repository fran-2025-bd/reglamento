import streamlit as st
import json

# Título principal
st.title("📘 Gestor del Reglamento Interno")
st.markdown("---")

# Mostrar el reglamento completo
with st.expander("📖 Ver el reglamento completo"):
    with open("reglamento.txt", "r", encoding="utf-8") as f:
        reglamento_completo = f.read()
        st.text_area("Texto completo del reglamento", reglamento_completo, height=400)

# Cargar artículos desde JSON (lista)
with open("articulos.json", "r", encoding="utf-8") as f:
    articulos = json.load(f)

# Crear lista de títulos para el dropdown
titulos_articulos = [art["titulo"] for art in articulos]

# Selección
st.subheader("🔍 Buscar artículo específico")
seleccionado = st.selectbox("Selecciona un artículo", titulos_articulos)

# Mostrar contenido del artículo seleccionado



# Mostrar contenido del artículo seleccionado
for art in articulos:
    if art["titulo"] == seleccionado:
        st.markdown(f"### 📑 {art['titulo']}")
        st.write(art["contenido"])

        # Si hay ordenanzas asociadas, verifícalas *aquí*
        if "ordenanzas" in art:
            for ordenanza in art["ordenanzas"]:
                nombre = ordenanza.get("nombre", "Ordenanza")
                url = ordenanza.get("url", "")

                # Botón o enlace para abrir
                st.markdown(f"🔗 [Ordenanza **{nombre}**]({url.replace('/preview', '/view')})", unsafe_allow_html=True)

                # Mostrar incrustado
                st.components.v1.html(
                    f'<iframe src="{url}" width="700" height="500" allow="autoplay"></iframe>',
                    height=520
                )