import streamlit as st

from aws_alerts import send_alert
from services.fase1_manejo import show_fase1_view
from services.fase2_db import show_fase2_view
from services.fase3_iot import show_fase3_view
from services.fase4_dashboard import show_fase4_view
from services.fase5_cloud import show_fase5_view
from services.fase6_vision import show_fase6_view
from utils.layout import show_header, show_sidebar

st.header("Dashboard FarmTech - Fase 7")

if st.button("🚨 Enviar Alerta de Teste"):
    msg_id = send_alert("Mensagem de teste enviada pelo botão do Streamlit!")
    st.success(f"Alerta enviado! ID: {msg_id}")

st.set_page_config(
    page_title="Fase 7 - Consolidação de um Sistema",
    layout="wide",
    page_icon="🌱",
)


def show_overview():
    st.subheader("Visão Geral do Sistema Integrado")

    st.write(
        """Esta dashboard consolida as principais entregas das Fases 1 a 6 em uma única
        interface. A navegação na barra lateral permite explorar:

        - **Fase 1** – cálculos de área de plantio e manejo de insumos;
        - **Fase 2** – organização dos dados em um banco relacional;
        - **Fase 3** – leituras de sensores IoT e automação inteligente;
        - **Fase 4** – análises de dados e modelos preditivos;
        - **Fase 5** – infraestrutura em nuvem e boas práticas de segurança;
        - **Fase 6** – visão computacional com redes neurais (YOLO).

        Além disso, a Fase 7 adiciona:
        - Integração conceitual de todas as fases;
        - Serviço de mensageria com Amazon SNS para envio de alertas;
        - Opção de uso tanto por **dashboard** quanto por **linha de comando**.
        """
    )

    st.markdown("### Mapa conceitual (pipeline de dados)")
    st.markdown(
        """1. **Sensores / Dados de Manejo (Fases 1 e 3)** alimentam o banco relacional (Fase 2).  
        2. Os dados consolidados são utilizados pelos modelos preditivos no dashboard (Fase 4).  
        3. Toda a infraestrutura está hospedada em nuvem com segurança (Fase 5).  
        4. Imagens da lavoura são analisadas por visão computacional (Fase 6).  
        5. Situações críticas disparam **alertas via AWS SNS** (Fase 7)."""
    )


def main():
    show_header()
    option, enable_alerts, threshold = show_sidebar()

    # --- NOVO BOTÃO NA SIDEBAR: ENVIAR ALERTA DE TESTE ---
    test_alert_clicked = st.sidebar.button("🚨 Enviar alerta de teste SNS")

    if test_alert_clicked:
        ok = send_alert(
            message="Alerta de teste enviado manualmente a partir da dashboard da Fase 7.",
            subject="Alerta de Teste - Fase 7",
        )
        if ok:
            st.sidebar.success("Alerta de teste enviado com sucesso via SNS!")
        else:
            st.sidebar.warning(
                "Não foi possível enviar o alerta de teste. "
                "Verifique as variáveis do .env e as permissões do usuário IAM."
            )
    # -----------------------------------------------------

    if option == "Visão Geral":
        show_overview()
    elif option == "Fase 1 - Manejo e Base de Dados":
        show_fase1_view()
    elif option == "Fase 2 - Banco Relacional":
        show_fase2_view()
    elif option == "Fase 3 - IoT e Sensores":
        show_fase3_view(enable_alerts=enable_alerts, umidade_threshold=threshold)
    elif option == "Fase 4 - Dashboard & ML":
        show_fase4_view()
    elif option == "Fase 5 - Cloud & Segurança":
        show_fase5_view()
    elif option == "Fase 6 - Visão Computacional":
        show_fase6_view()
    else:
        st.error("Opção desconhecida.")

    st.markdown("---")
    st.caption("Fase 7 - FIAP 2025 • Dashboard consolidada")


if __name__ == "__main__":
    main()
