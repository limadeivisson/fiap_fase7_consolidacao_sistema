FIAP - Faculdade de Informática e Administração Paulista
<p align="center"> <a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%"></a> </p> <br>
FarmTech Solutions
Fase 7 – Capítulo 1

A Consolidação de um Sistema Integrado para o Agronegócio

---

## 👨‍🎓 Integrantes do Grupo 34:
- Deivisson Gonçalves Lima – RM565095 – [deivisson.engtele@gmail.com](mailto:deivisson.engtele@gmail.com)
- Omar Calil Abrão Mustafá Assem – RM561375 – [ocama12@gmail.com](mailto:ocama12@gmail.com)
- Paulo Henrique de Sousa – RM564262 – [pauloo.sousa16@outlook.com](mailto:pauloo.sousa16@outlook.com)
- Renan Danilo dos Santos Pereira – RM566175 – [renansantos4978@gmail.com](mailto:renansantos4978@gmail.com)

## 👩‍🏫 Professores:
### Tutor(a):
- Lucas Gomes Moreira  
### Coordenador(a):
- André Godoi Chiovato  

---

## 📜 Introdução

A Fase 7 marca o momento em que integramos todos os módulos desenvolvidos ao longo das Fases 1 a 6, consolidando um único sistema inteligente, organizado e executável por meio de um único dashboard Streamlit ou por linha de comando.

O objetivo final é criar um sistema de gestão agrícola completo, reunindo:

- Cálculos de manejo e área

- Banco de dados estruturado

- IoT e ESP32

- Machine Learning

- Cloud & Segurança

- Visão Computacional com YOLO

- Mensageria AWS SNS para alertas

---

## 🔄 Resumo das Fases 1 a 6
### 🌱 Fase 1 – Base de Dados Inicial e Manejo Agrícola

- Construção dos primeiros cálculos de área de plantio

- Organização de insumos

- Integração inicial dos dados que alimentariam todo o ecossistema

- Cálculos implementados no dashboard consolidado

---

### 🗂️ Fase 2 – Banco de Dados Estruturado (MER/DER)

- Modelagem relacional completa

- Tabelas de talhões, sensores, manejo

- Preparação para integração com os sensores da Fase 3

---

### 🌦️ Fase 3 – IoT e Automação Inteligente (ESP32)

- Integração com sensores (DHT22, LDR, pH simulado)

- Lógica de irrigação automática

- CRUD via Python + banco de dados

- Simulação replicada na dashboard

---

### 📊 Fase 4 – Dashboard Interativo com Data Science

- Modelos preditivos Scikit-Learn

- Interface Streamlit para análise

- Visualizações e insights para tomada de decisão

- Reaproveitado e aprimorado na Fase 7

---

### ☁️ Fase 5 – Cloud Computing & Segurança

- Infra AWS

- Configuração de boas práticas ISO 27001/27002

- Integração com serviços AWS

- Nesta fase implementamos o serviço SNS utilizado agora para os alertas

---

### 👁️ Fase 6 – Visão Computacional (YOLO)

- Sistema para detectar pragas/doenças via imagens

- Pipeline de inferência

- Na Fase 7 usamos simulação visual para demonstração da arquitetura

---

### 🧩 Fase 7 – Consolidação de um Sistema Completo

Nesta etapa final, criamos:

✔️ 1. Um dashboard final único (Streamlit)

- Com navegação lateral para acessar cada fase, incluindo:

- Cálculo de plantio

- Banco relacional (mock conceitual)

- IoT e sensores com alerta

- Machine Learning

- Cloud

- Visão computacional

✔️ 2. Execução por linha de comando

- Arquivo cli.py permitindo:

- Teste de sensores

- Disparo manual de alertas

- Simulação da Fase 1

✔️ 3. Serviço de Mensageria AWS SNS – ALERTAS

- .env configurado

- Chave IAM com acesso programático

- SNS Topic configurado

- Função send_alert() integrada no dashboard e na CLI

✔️ 4. Estrutura de Pastas Unificada
fase7/
├─ main.py
├─ cli.py
├─ aws_alerts.py
├─ requirements.txt
├─ README.md
├─ assets/
│   ├─ imagem_teste_fase6.png
│   └─ logo-fiap.png
├─ services/
│   ├─ fase1_manejo.py
│   ├─ fase2_db.py
│   ├─ fase3_iot.py
│   ├─ fase4_dashboard.py
│   ├─ fase5_cloud.py
│   └─ fase6_vision.py
└─ utils/
    └─ layout.py

✉️ Envio de Alertas – AWS SNS

O dashboard possui:

- Botão “Enviar alerta de teste”

- Alerta automático para baixa umidade na Fase 3

- Integração via boto3

🎥 Vídeo de Apresentação (≤ 10 minutos)

👉 Link do vídeo (não listado):
🔗 [INSERIR LINK AQUI]

📜 Licença

Projeto acadêmico desenvolvido para o curso de Inteligência Artificial – FIAP.
Todos os direitos reservados aos autores.