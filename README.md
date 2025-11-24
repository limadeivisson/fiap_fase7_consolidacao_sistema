# FIAP - Faculdade de Informática e Administração Paulista  

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP" width="40%">
  </a>
</p>

# FarmTech Solutions  
## Fase 7 – Capítulo 1  
### **A Consolidação de um Sistema Integrado para o Agronegócio**

---

## 👨‍🎓 Integrantes do Grupo 34
- **Deivisson Gonçalves Lima** – RM565095 – deivisson.engtele@gmail.com
- **Omar Calil Abrão Mustafá Assem** – RM561375 – ocama12@gmail.com
- **Paulo Henrique de Sousa** – RM564262 – pauloo.sousa16@outlook.com
- **Renan Danilo dos Santos Pereira** – RM566175 – renansantos4978@gmail.com

---

## 👩‍🏫 Professores
### **Tutor(a):**
- Lucas Gomes Moreira  

### **Coordenador(a):**
- André Godoi Chiovato  

---

## 📜 Introdução

A Fase 7 representa o ponto de unificação de **todas as fases anteriores**, consolidando um **sistema inteligente completo** para o agronegócio, implementado em Python, Streamlit, IoT, Visão Computacional, Cloud e Arquitetura de Software.

O objetivo é integrar:

- Cálculos de manejo  
- Banco de dados  
- Sensores IoT (ESP32)  
- Machine Learning  
- Visão computacional YOLO  
- Infraestrutura em Cloud  
- Alertas via AWS SNS  
- Um dashboard único para navegação entre fases  
- Execução por CLI (linha de comando)

---

# 🔄 Resumo Geral das Fases (1 a 6)

## 🌱 **Fase 1 – Manejo e Base Agrícola**
- Cálculo de área plantada  
- Dimensionamento agrícola  
- Conceitos que alimentam as fases seguintes  

---

## 🗂️ **Fase 2 – Banco de Dados (MER / DER)**
- Modelagem relacional  
- Estrutura para sensores, talhões, manejo  
- Base conceitual utilizada na Fase 7  

---

## 🌦️ **Fase 3 – IoT (ESP32 + Sensores)**
- DHT22 (temperatura/umidade)  
- LDR e sensor de pH simulado  
- Lógica de irrigação inteligente  
- Alerta automático via SNS integrado na Fase 7  

---

## 📊 **Fase 4 – Dashboard com Data Science**
- Modelos de Machine Learning  
- Interface Streamlit  
- Gráficos e insights  

---

## ☁️ **Fase 5 – Cloud & Segurança**
- Arquitetura AWS  
- Governança e IAM  
- Integração com SNS (mensageria)  

---

## 👁️ **Fase 6 – Visão Computacional (YOLO)**
- Classificação / detecção de pragas e doenças  
- Pipeline de inferência  
- Integrado ao dashboard da Fase 7  

---

# 🧩 Fase 7 – Consolidação do Sistema

Nesta fase integramos todas as soluções anteriores em um **único ecossistema funcional**.

### ✔️ **1. Dashboard Streamlit Completo**
Com navegação lateral para:

- Manejo (Fase 1)  
- Banco de Dados (Fase 2)  
- IoT e Sensores (Fase 3)  
- Machine Learning (Fase 4)  
- Cloud (Fase 5)  
- Visão Computacional (Fase 6)  

---

### ✔️ **2. Execução por CLI (`cli.py`)**
Permite:

- Teste de sensores  
- Disparo manual de alertas  
- Execução de cálculos da Fase 1  
- Visualizações e simulações rápidas  

---

### ✔️ **3. AWS SNS – Sistema de Alertas**
Implementado no arquivo `aws_alerts.py`.

- Envio de SMS/E-mail  
- Alertas automáticos quando a umidade está baixa  
- Função integrada ao dashboard e à CLI  

---

# 📁 Estrutura Final do Projeto

```text
fase7/
│
├── main.py
├── cli.py
├── aws_alerts.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── Arquitetura_Cons.png
│   ├── imagem_teste_fase6.png
│   └── logo-fiap.png
│
├── services/
│   ├── fase1_manejo.py
│   ├── fase2_db.py
│   ├── fase3_iot.py
│   ├── fase4_dashboard.py
│   ├── fase5_cloud.py
│   └── fase6_vision.py
│
└── utils/
    └── layout.py
```

---

# ✉️ Envio de Alertas – AWS SNS

Integração com:

- `boto3`  
- IAM com acesso programático  
- SNS Topic configurado  
- Alerta manual e automático (umidade)

---

# 🎥 Vídeo de Apresentação (≤ 10 minutos)

📌 **Link do vídeo (não listado):**  
🔗 *https://youtu.be/wfoYVzE0aHQ*

---

# 📜 Licença

Projeto acadêmico desenvolvido para o curso de **Inteligência Artificial – FIAP**.  
Todos os direitos reservados aos autores.
