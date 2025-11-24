
import streamlit as st


def show_header():
    st.title("Fase 7 - Consolidação de um Sistema")
    st.caption(
        "Integração das Fases 1 a 6: Base de dados, IoT, Data Science, Cloud e Visão Computacional."
    )


def show_sidebar():
    st.sidebar.title("Navegação")
    option = st.sidebar.radio(
        "Escolha a visão:",
        [
            "Visão Geral",
            "Fase 1 - Manejo e Base de Dados",
            "Fase 2 - Banco Relacional",
            "Fase 3 - IoT e Sensores",
            "Fase 4 - Dashboard & ML",
            "Fase 5 - Cloud & Segurança",
            "Fase 6 - Visão Computacional",
        ],
    )
    st.sidebar.markdown("---")
    enable_alerts = st.sidebar.checkbox("Habilitar envio de alertas AWS SNS", value=False)
    threshold = st.sidebar.slider(
        "Limite crítico de umidade para alerta (Fase 3)",
        min_value=0,
        max_value=100,
        value=30,
        step=5,
    )
    return option, enable_alerts, threshold
