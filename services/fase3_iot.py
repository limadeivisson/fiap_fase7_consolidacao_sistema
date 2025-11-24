
from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import datetime

import pandas as pd
import streamlit as st

from aws_alerts import send_alert


@dataclass
class SensorReading:
    timestamp: datetime
    umidade: float
    ph: float
    temperatura: float


def generate_fake_reading() -> SensorReading:
    """Gera uma leitura simulada de sensores (como se viesse do ESP32)."""
    return SensorReading(
        timestamp=datetime.now(),
        umidade=round(random.uniform(10, 80), 1),
        ph=round(random.uniform(5.0, 7.5), 2),
        temperatura=round(random.uniform(15, 35), 1),
    )


def show_fase3_view(enable_alerts: bool, umidade_threshold: int):
    st.subheader("Fase 3 - IoT e Automação Inteligente (ESP32 + Sensores)")

    st.write(
        """Nesta fase criamos um sistema IoT com ESP32 para automação de irrigação.
        Na consolidação (Fase 7) usamos uma simulação de leituras para demonstrar a lógica
        de decisão e disparo de alertas na AWS."""
    )

    if st.button("Gerar nova leitura de sensor"):
        reading = generate_fake_reading()

        df = pd.DataFrame(
            [
                {
                    "Data/Hora": reading.timestamp.strftime("%d/%m/%Y %H:%M:%S"),
                    "Umidade (%)": reading.umidade,
                    "pH": reading.ph,
                    "Temperatura (°C)": reading.temperatura,
                }
            ]
        )
        st.dataframe(df, use_container_width=True)

        if reading.umidade < umidade_threshold:
            st.error(
                f"Umidade abaixo do limite ({umidade_threshold}%). "
                "Bomba de irrigação deve ser acionada!"
            )
            if enable_alerts:
                send_alert(
                    message=(
                        f"Alerta de baixa umidade: {reading.umidade}% "
                        f"registrados às {reading.timestamp}."
                    ),
                    subject="Alerta de Irrigação - Baixa Umidade",
                )
                st.success("Alerta enviado via AWS SNS (veja logs/console).")
            else:
                st.info("Envio de alerta AWS SNS está desabilitado na barra lateral.")
        else:
            st.success("Níveis de umidade adequados. Nenhuma ação corretiva necessária.")
