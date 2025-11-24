
from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression


def _build_sample_dataset() -> pd.DataFrame:
    # Exemplo simples: umidade média x produtividade
    rng = np.random.default_rng(42)
    umidade = rng.uniform(20, 80, size=30)
    produtividade = 40 + 0.8 * umidade + rng.normal(0, 5, size=30)
    return pd.DataFrame({"Umidade (%)": umidade, "Produtividade (sc/ha)": produtividade})


def show_fase4_view():
    st.subheader("Fase 4 - Dashboard Interativo com Data Science (Scikit-Learn + Streamlit)")

    st.write(
        """Nesta área demonstramos o uso de modelos preditivos simples para apoiar a
        tomada de decisão do gestor agrícola."""
    )

    data = _build_sample_dataset()
    st.markdown("### Amostra de dados de treinamento (simulados)")
    st.dataframe(data.head(), use_container_width=True)

    # Treina modelo de regressão linear
    model = LinearRegression()
    X = data[["Umidade (%)"]]
    y = data["Produtividade (sc/ha)"]
    model.fit(X, y)

    st.markdown("### Simulador de produtividade esperada")
    umidade_input = st.slider("Umidade média esperada do solo (%)", 20, 80, value=50)
    pred = model.predict([[umidade_input]])[0]
    st.metric(
        label="Produtividade estimada (sc/ha)",
        value=f"{pred:,.2f}",
        delta=None,
    )

    st.info(
        "Na Fase 4 original, a dashboard completa inclui múltiplos algoritmos de Machine "
        "Learning, gráficos interativos e integração direta com os dados do ESP32."
    )
