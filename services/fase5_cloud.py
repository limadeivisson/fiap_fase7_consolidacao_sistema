
from __future__ import annotations

import streamlit as st


def show_fase5_view():
    st.subheader("Fase 5 - Cloud Computing & Segurança (AWS)")

    st.write(
        """Aqui resumimos o papel da infraestrutura em nuvem na consolidação do projeto.

        A Fase 5 garantiu:
        - Disponibilidade e escalabilidade via AWS;
        - Armazenamento seguro dos dados sensíveis dos sensores;
        - Aplicação de boas práticas de segurança (ISO 27001 / 27002);
        - Criação da base para o serviço de mensageria utilizado nesta Fase 7 (Amazon SNS)."""
    )

    st.markdown("### Checklist de boas práticas (exemplo)")
    itens = [
        "Uso de credenciais de usuário IAM em vez de root account",
        "Criação de roles específicas para o ESP32 / serviços de aplicação",
        "Criptografia em repouso para banco de dados e buckets de dados brutos",
        "Backups automáticos configurados",
        "Monitoramento com CloudWatch e alarmes de uso",
    ]
    for item in itens:
        st.checkbox(item, value=True, disabled=True)

    st.info(
        "A implementação detalhada encontra-se no repositório da Fase 5. "
        "Aqui apenas consolidamos a visão conceitual no fluxo do sistema."
    )
