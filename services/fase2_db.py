
from __future__ import annotations

import streamlit as st
import pandas as pd


def show_fase2_view():
    st.subheader("Fase 2 - Banco de Dados Estruturado (MER / DER)")

    st.write(
        """Nesta fase consolidamos um **banco de dados relacional** que integra as
        informações de manejo agrícola, sensores e histórico da fazenda.

        Aqui na Fase 7 mostramos apenas um exemplo simplificado de tabelas relacionadas.
        Para a implementação real, este módulo deve se conectar ao banco utilizado na Fase 2
        (por exemplo MySQL, PostgreSQL ou SQL Server)."""
    )

    st.markdown("### Exemplo conceitual de esquema relacional")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Tabela `talhao`**")
        talhao = pd.DataFrame(
            {
                "id_talhao": [1, 2, 3],
                "nome": ["T1", "T2", "T3"],
                "area_ha": [1.2, 0.8, 2.3],
            }
        )
        st.dataframe(talhao, use_container_width=True)

    with col2:
        st.markdown("**Tabela `sensor_leitura`**")
        leitura = pd.DataFrame(
            {
                "id_leitura": [101, 102, 103],
                "id_talhao": [1, 1, 2],
                "umidade_solo": [45, 38, 52],
                "ph": [6.1, 5.8, 6.4],
            }
        )
        st.dataframe(leitura, use_container_width=True)

    st.info(
        "Na entrega real, este módulo pode expor funções de consulta (SELECT) e gravação "
        "(INSERT/UPDATE) utilizando a mesma modelagem MER/DER entregue na Fase 2."
    )
