import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# Configuración inicial del Dashboard
# ---------------------------------------------------------
st.set_page_config(
    page_title="Diagnóstico Alimentario - Escuela Nº 21",
    page_icon="🍎",
    layout="wide"
)

# Estilos CSS personalizados para tarjetas de métricas
st.markdown("""
    <style>
    .metric-card {
        background-color: #ffffff;
        border-left: 5px solid #2e7d32;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        margin-bottom: 10px;
    }
    .metric-title { font-size: 13px; color: #555; font-weight: 600; text-transform: uppercase; }
    .metric-value { font-size: 22px; color: #1b5e20; font-weight: bold; margin: 4px 0; }
    .metric-sub { font-size: 12px; color: #666; }
    </style>
""", unsafe_allow_html=True)

st.title("🍎 Diagnóstico Cuantitativo de Hábitos Alimentarios")
st.caption(
    "Investigación de Acción Comunitaria — Escuela Primaria Nº 21 'Coraceros de la Patria' (José León Suárez, Gral. San Martín)")

# ---------------------------------------------------------
# 1. Muestra y Datos del Diagnóstico
# ---------------------------------------------------------
N = 10


@st.cache_data
def cargar_csv():
    try:
        df = pd.read_csv('proyecto-habitos-alimentarios-csv (1).csv', encoding='utf-8-sig', sep=',')
        return df
    except Exception:
        return None


df_csv = cargar_csv()

# ---------------------------------------------------------
# 2. Resumen Metodológico (Marco del Proyecto)
# ---------------------------------------------------------
with st.expander("📌 Ver Contextualización y Marco del Proyecto", expanded=False):
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.markdown("""
        **Población de estudio:** Estudiantes de nivel primario de la Escuela Primaria Nº 21 "Coraceros de la Patria" (José León Suárez).  
        **Metodología:** Relevamiento empírico cuantitativo mediante el software Epicollect5 y jornada de trabajo de campo.
        """)
    with c_m2:
        st.markdown("""
        **Muestra analizada ($N$):** 10 encuestas válidas (6 mujeres y 4 varones).  
        **Propósito:** Generar un diagnóstico empírico local que visibilice necesidades de acción comunitaria e intervenciones escolares.
        """)

st.divider()

# ---------------------------------------------------------
# 3. Indicadores Principales (KPIs)
# ---------------------------------------------------------
st.subheader("📌 Indicadores Clave del Diagnóstico (N=10)")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">DESAYUNO DIARIO</div>
        <div class="metric-value">3 de 10</div>
        <div class="metric-sub">30% desayuna todos los días</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">ALIMENTACIÓN EN FAMILIA</div>
        <div class="metric-value">9 de 10</div>
        <div class="metric-sub">90% come acompañado en su hogar</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">USO DE PANTALLAS</div>
        <div class="metric-value">7 de 10</div>
        <div class="metric-sub">70% usa TV/Celular al comer (siempre o a veces)</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">BEBIDA PREDOMINANTE</div>
        <div class="metric-value">7 de 10</div>
        <div class="metric-sub">70% consume agua como bebida habitual</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# 4. Organización por los 4 Ejes del Proyecto
# ---------------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🥣 Eje 1: Frecuencias de Consumo",
    "🏡 Eje 2: Entorno Familiar",
    "🏫 Eje 3: Entorno Escolar",
    "📱 Eje 4: Pantallas y Actividad Física",
    "🎯 Acción Comunitaria"
])

# --- EJE 1: FRECUENCIAS DE CONSUMO ---
with tab1:
    st.markdown("### Eje 1: Frecuencias de consumo y esquema de comidas")
    st.caption("Preguntas asociadas: 1, 2, 3, 4, 5, 6 y 8 del cuestionario base.")

    col_e1a, col_e1b = st.columns(2)

    with col_e1a:
        df_desayuno = pd.DataFrame({
            'Frecuencia': ['Algunos días', 'Todos los días', 'Nunca'],
            'Cantidad': [6, 3, 1],
            'Etiqueta': ['6 de 10 (60%)', '3 de 10 (30%)', '1 de 10 (10%)']
        })
        fig_des = px.pie(
            df_desayuno,
            values='Cantidad',
            names='Frecuencia',
            title="Cumplimiento del Desayuno Diario",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig_des.update_traces(textinfo='label+percent')
        st.plotly_chart(fig_des, use_container_width=True)
        st.info(
            "💡 **Componentes frecuentes:** Leche/chocolatada, té, mate cocido y pan/galletitas. Quien no desayuna refiere falta de hambre matutina.")

    with col_e1b:
        df_alimentos = pd.DataFrame({
            'Alimento': ['Agua', 'Carnes', 'Verduras', 'Frutas', 'Jugos/Gaseosas'],
            'Todos los días': [7, 2, 2, 2, 0],
            'Casi todos los días / A veces': [3, 7, 6, 7, 3],
            'Casi nunca o nunca': [0, 1, 2, 1, 7]
        })
        df_alimentos_melt = df_alimentos.melt(id_vars=['Alimento'], var_name='Frecuencia', value_name='Niños')
        fig_alim = px.bar(
            df_alimentos_melt,
            x='Alimento',
            y='Niños',
            color='Frecuencia',
            title="Frecuencia Semanal por Grupo de Alimento",
            barmode='stack',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_alim, use_container_width=True)
        st.warning(
            "⚠️ **Frutas y Verduras:** Los motivos principales de bajo consumo son 'no me gusta' o falta de disponibilidad en el hogar/colegio.")

# --- EJE 2: ENTORNO FAMILIAR ---
with tab2:
    st.markdown("### Eje 2: Entorno familiar")
    st.caption("Preguntas asociadas: 7, 8 y 9 del cuestionario base (compañía, lugar físico y preparación).")

    col_e2a, col_e2b = st.columns(2)

    with col_e2a:
        df_comp = pd.DataFrame({
            'Compañía': ['Acompañado por la familia', 'Solo / Otros'],
            'Cantidad': [9, 1],
            'Etiqueta': ['9 de 10 (90%)', '1 de 10 (10%)']
        })
        fig_comp = px.bar(
            df_comp,
            x='Compañía',
            y='Cantidad',
            text='Etiqueta',
            title="Acompañamiento en el Momento de la Comida",
            color='Compañía',
            color_discrete_sequence=['#2e7d32', '#a5d6a7']
        )
        fig_comp.update_layout(showlegend=False)
        st.plotly_chart(fig_comp, use_container_width=True)

    with col_e2b:
        df_lugar = pd.DataFrame({
            'Lugar': ['En la mesa', 'En la cama', 'Depende el día'],
            'Cantidad': [8, 1, 1],
            'Etiqueta': ['8 de 10 (80%)', '1 de 10 (10%)', '1 de 10 (10%)']
        })
        fig_lug = px.bar(
            df_lugar,
            y='Lugar',
            x='Cantidad',
            orientation='h',
            text='Etiqueta',
            title="Espacio Físico Utilizado para Comer",
            color='Lugar',
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_lug.update_layout(showlegend=False)
        st.plotly_chart(fig_lug, use_container_width=True)

    st.success(
        "👨‍👩‍👧‍👦 **Conclusión del Entorno:** El 90% come en familia y el 80% en la mesa, reflejando un valor central del hogar como espacio de socialización.")

# --- EJE 3: ENTORNO ESCOLAR ---
with tab3:
    st.markdown("### Eje 3: Entorno escolar (Comedor y recreos)")
    st.caption("Preguntas asociadas: 10 y 11 del cuestionario base.")

    col_e3a, col_e3b = st.columns(2)

    with col_e3a:
        df_percepcion = pd.DataFrame({
            'Percepción': ['Más o menos (algunas cosas sí/no)', 'Muy rica', 'No le gusta casi nada', 'Sin respuesta'],
            'Cantidad': [5, 2, 2, 1],
            'Etiqueta': ['5 de 10 (50%)', '2 de 10 (20%)', '2 de 10 (20%)', '1 de 10 (10%)']
        })
        fig_perc = px.pie(
            df_percepcion,
            values='Cantidad',
            names='Percepción',
            title="Percepción del Menú del Comedor Escolar",
            color_discrete_sequence=px.colors.qualitative.Vivid
        )
        fig_perc.update_traces(textinfo='label+percent')
        st.plotly_chart(fig_perc, use_container_width=True)

    with col_e3b:
        df_recreo = pd.DataFrame({
            'Consumo Recreo': ['Nada', 'Snacks salados', 'Galletitas / Alfajores / Kiosco'],
            'Cantidad': [3, 2, 5],
            'Etiqueta': ['3 de 10 (30%)', '2 de 10 (20%)', '5 de 10 (50%)']
        })
        fig_rec = px.bar(
            df_recreo,
            x='Consumo Recreo',
            y='Cantidad',
            text='Etiqueta',
            title="Consumos Habituales durante los Recreos",
            color='Consumo Recreo',
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig_rec.update_layout(showlegend=False)
        st.plotly_chart(fig_rec, use_container_width=True)

    st.warning(
        "🏬 **Alimentación en Recreos:** Predominio de ultraprocesados (snacks salados, galletitas dulces, alfajores) y baja presencia de frutas o lácteos frescos.")

# --- EJE 4: PANTALLAS Y ACTIVIDAD FÍSICA ---
with tab4:
    st.markdown("### Eje 4: Uso de pantallas, sedentarismo y actividad física")
    st.caption("Preguntas asociadas: 12 y 13 del cuestionario base.")

    col_e4a, col_e4b = st.columns(2)

    with col_e4a:
        df_pan_uso = pd.DataFrame({
            'Frecuencia Uso': ['A veces / Muchas veces', 'Siempre', 'Nunca'],
            'Cantidad': [4, 3, 3],
            'Etiqueta': ['4 de 10 (40%)', '3 de 10 (30%)', '3 de 10 (30%)']
        })
        fig_pan_u = px.pie(
            df_pan_uso,
            values='Cantidad',
            names='Frecuencia Uso',
            title="Uso de Dispositivos (TV/Celular) al Comer",
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pan_u.update_traces(textinfo='label+percent')
        st.plotly_chart(fig_pan_u, use_container_width=True)

    with col_e4b:
        df_act_fis = pd.DataFrame({
            'Actividad Física Semanal': ['2 a 4 días a la semana', 'Todos o casi todos los días', 'Casi nunca o nunca'],
            'Cantidad': [6, 3, 1],
            'Etiqueta': ['6 de 10 (60%)', '3 de 10 (30%)', '1 de 10 (10%)']
        })
        fig_act_f = px.bar(
            df_act_fis,
            x='Actividad Física Semanal',
            y='Cantidad',
            text='Etiqueta',
            title="Nivel Semanal de Deporte / Movimiento",
            color='Actividad Física Semanal',
            color_discrete_sequence=px.colors.qualitative.Dark2
        )
        fig_act_f.update_layout(showlegend=False)
        st.plotly_chart(fig_act_f, use_container_width=True)

    st.info(
        "📱 **Impacto en la Ingesta:** La mitad de quienes comen con pantallas indica que 'no sabe' o no nota si modifica la cantidad de alimento ingerido.")

# --- SECCIÓN 5: ACCIÓN COMUNITARIA ---
with tab5:
    st.markdown("""
### 📋 Conclusión para la Acción Comunitaria

Los datos cuantitativos obtenidos a partir de las 10 encuestas relevadas con Epicollect5 proporcionan evidencia empírica directa sobre la cultura alimentaria de los estudiantes de la Escuela Primaria Nº 21 de José León Suárez.

🚀 **Líneas de Acción Prioritarias:**
- **Promoción del Desayuno:** Teniendo en cuenta que solo 3 de cada 10 desayunan a diario, se requiere fortalecer la cobertura y la promoción del desayuno escolar como hábito fundamental.
- **Mejora del Menú del Comedor:** Ante la baja valoración reportada sobre la comida del comedor escolar, resulta prioritario revisar la calidad, variedad y aceptación de las preparaciones ofrecidas para garantizar una nutrición adecuada e incentivada.
- **Entorno del Recreo Saludable:** Al no contar la escuela con kiosco interno, es clave promover meriendas saludables traídas desde el hogar (como frutas, lácteos o cereales) en reemplazo de los ultraprocesados.
- **Desconexión Digital en la Mesa:** Aprovechar el alto valor que las familias le otorgan a la comida compartida (90%) para fomentar momentos en la mesa libres de pantallas y dispositivos móviles.
""")

    if df_csv is not None:
        st.divider()
        st.markdown("#### 📋 Consulta de Registros Crudos del CSV (N=10)")
        st.dataframe(df_csv, use_container_width=True)

# ---------------------------------------------------------
# 5. Pie de Página
# ---------------------------------------------------------
st.divider()
st.caption(
    "Diagnóstico elaborado para la materia Metodologías Cuantitativas — Universidad Nacional de San Martín (UNSAM)")
