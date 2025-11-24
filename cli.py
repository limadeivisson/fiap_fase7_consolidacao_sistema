
"""Interface em linha de comando para a Fase 7.

Exemplos de uso:

- python cli.py --sensor-alert
- python cli.py --simulate-fase1
"""
from __future__ import annotations

import argparse
from datetime import datetime

from aws_alerts import send_alert
from services.fase1_manejo import calcular_area_plantio
from services.fase3_iot import generate_fake_reading


def run_sensor_alert(threshold: int) -> None:
    reading = generate_fake_reading()
    print(f"[CLI] Leitura simulada às {reading.timestamp}:")
    print(
        f"   Umidade={reading.umidade}%, pH={reading.ph}, "
        f"Temperatura={reading.temperatura} °C"
    )

    if reading.umidade < threshold:
        print(f"[CLI] Umidade abaixo de {threshold}%. Disparando alerta...")
        send_alert(
            message=(
                f"[CLI] Alerta de baixa umidade: {reading.umidade}% "
                f"registrados às {reading.timestamp}."
            ),
            subject="Alerta CLI - Baixa Umidade",
        )
    else:
        print("[CLI] Níveis de umidade adequados. Nenhum alerta enviado.")


def run_simulate_fase1() -> None:
    area = calcular_area_plantio(50.0, 30.0)
    print(
        f"[CLI] Área de plantio simulada (50m x 30m): {area:.2f} m² "
        f"({area / 10_000:.2f} ha)"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ferramentas de linha de comando para a Fase 7."
    )
    parser.add_argument(
        "--sensor-alert",
        action="store_true",
        help="Gera uma leitura de sensor simulada e dispara alerta se necessário.",
    )
    parser.add_argument(
        "--simulate-fase1",
        action="store_true",
        help="Roda um exemplo simples da Fase 1 (cálculo de área).",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=30,
        help="Limite de umidade (%) para envio de alerta (padrão: 30).",
    )

    args = parser.parse_args()

    if args.sensor_alert:
        run_sensor_alert(threshold=args.threshold)
    elif args.simulate_fase1:
        run_simulate_fase1()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
