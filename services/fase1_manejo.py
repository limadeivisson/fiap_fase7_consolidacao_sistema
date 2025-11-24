
from __future__ import annotations

import streamlit as st
import pandas as pd
import numpy as np


def calcular_area_plantio(comprimento_m: float, largura_m: float) -> float:
    """Retorna a área de plantio em metros quadrados."""
    return comprimento_m * largura_m


def show_fase1_view():
    st.subheader("Fase 1 - Base de Dados Inicial e Manejo de Insumos")

    st.write(
        """Aqui consolidamos os cálculos básicos de área de plantio,
        estimativa de insumos e organização da base de dados inicial."""
    )

    col1, col2 = st.columns(2)
    with col1:
        comprimento = st.number_input("Comprimento do talhão (m)", min_value=1.0, value=50.0)
    with col2:
        largura = st.number_input("Largura do talhão (m)", min_value=1.0, value=30.0)

    area = calcular_area_plantio(comprimento, largura)
    st.metric("Área calculada (m²)", f"{area:,.2f}")

    st.markdown("### Estimativa simplificada de insumos")
    densidade_semente = st.number_input(
        "Densidade de sementes (kg/ha)", min_value=1.0, value=60.0
    )
    area_ha = area / 10_000.0
    sementes_necessarias = densidade_semente * area_ha
    st.write(f"Sementes necessárias: **{sementes_necessarias:,.2f} kg**")

    # Demonstração de uma base de dados tabular
    st.markdown("### Amostra de base de manejo (dados simulados)")
    dados = pd.DataFrame(
        {
            "Talhão": ["T1", "T2", "T3"],
            "Área (ha)": [1.2, 0.8, 2.3],
            "Cultura": ["Soja", "Milho", "Café"],
            "Fertilizante (kg/ha)": [300, 280, 320],
        }
    )
    st.dataframe(dados, use_container_width=True)
