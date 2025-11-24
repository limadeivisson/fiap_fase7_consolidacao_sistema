
from __future__ import annotations

import io
from typing import Optional

import numpy as np
import streamlit as st
from PIL import Image, ImageDraw, ImageFont


def _fake_yolo_detection(image: Image.Image) -> Image.Image:
    """Simula um resultado de detecção de pragas/doenças em uma imagem.

    Esta função NÃO substitui o modelo YOLO treinado na Fase 6. Ela apenas
    desenha uma caixa ilustrativa para fins de apresentação da Fase 7.
    """
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)

    w, h = img.size
    box = [w * 0.2, h * 0.2, w * 0.8, h * 0.8]
    draw.rectangle(box, outline="red", width=4)
    draw.text((box[0] + 5, box[1] + 5), "Área suspeita", fill="red")

    return img


def show_fase6_view():
    st.subheader("Fase 6 - Visão Computacional com Redes Neurais (YOLO)")

    st.write(
        """Na Fase 6 foi desenvolvido um modelo de visão computacional capaz de identificar
        pragas, doenças ou crescimento irregular nas plantações a partir de imagens da lavoura.

        Na consolidação (Fase 7), permitimos o upload de uma imagem e exibimos uma *simulação*
        de deteção, apenas para ilustrar o fluxo. No projeto real, este módulo deve importar o
        modelo YOLO treinado e chamar a função de inferência original."""
    )

    uploaded = st.file_uploader("Envie uma imagem da lavoura (JPG ou PNG)", type=["jpg", "jpeg", "png"])

    if uploaded is not None:
        image = Image.open(uploaded)
        st.image(image, caption="Imagem enviada", use_container_width=True)

        if st.button("Rodar detecção (simulada)"):
            output = _fake_yolo_detection(image)
            st.image(output, caption="Resultado ilustrativo de detecção", use_container_width=True)
            st.warning(
                "Este resultado é apenas ilustrativo. "
                "Conecte aqui o modelo YOLO treinado na Fase 6 para a inferência real."
            )
