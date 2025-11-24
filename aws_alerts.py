import os
import boto3
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_SNS_TOPIC_ARN = os.getenv("AWS_SNS_TOPIC_ARN")

def send_alert(message="Alerta de teste do sistema integrado da Fase 7!"):
    """Envia um alerta SNS usando o tópico configurado no .env."""

    try:
        client = boto3.client(
            "sns",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        response = client.publish(
            TopicArn=AWS_SNS_TOPIC_ARN,
            Message=message,
            Subject="🚨 Alerta do Sistema FarmTech"
        )

        return response["MessageId"]

    except Exception as e:
        return f"Erro ao enviar alerta: {e}"
