#!/usr/bin/env python3
"""Generate an executive campaign brief from a JSON metrics snapshot."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def number(value: float) -> str:
    return f"{value:,.2f}".rstrip("0").rstrip(".").replace(",", "X").replace(".", ",").replace("X", ".")


def metric_value(value: float, unit: str) -> str:
    return f"{number(value)}{unit}"


def analyse(metric: dict[str, Any]) -> dict[str, str]:
    name = metric["name"]
    value = float(metric["value"])
    target = float(metric["target"])
    previous = float(metric.get("previous", value))
    unit = metric.get("unit", "")
    lower_is_better = bool(metric.get("lower_is_better", False))

    change = 0.0 if previous == 0 else ((value - previous) / abs(previous)) * 100
    target_gap = 0.0 if target == 0 else ((value - target) / abs(target)) * 100
    meets_target = value <= target if lower_is_better else value >= target
    direction = "mejora" if (change <= 0 if lower_is_better else change >= 0) else "empeora"
    state = "logro" if meets_target else "riesgo"

    return {
        "state": state,
        "name": name,
        "line": (
            f"{name}: {metric_value(value, unit)} "
            f"({change:+.1f}% vs. periodo anterior; {direction}). "
            f"{'Cumple' if meets_target else 'No cumple'} el objetivo "
            f"de {metric_value(target, unit)} ({target_gap:+.1f}%)."
        ),
        "action": (
            f"Mantener la palanca que impulsa {name} y validar si se puede escalar."
            if meets_target
            else f"Revisar audiencia, creatividad y canal para recuperar {name} hacia el objetivo."
        ),
    }


def render(data: dict[str, Any], markdown: bool = False) -> str:
    findings = [analyse(metric) for metric in data["metrics"]]
    wins = [item for item in findings if item["state"] == "logro"]
    risks = [item for item in findings if item["state"] == "riesgo"]
    title = f"BRIEF · {data.get('period', 'Periodo sin nombre')}"

    if markdown:
        sections = [f"# {title}", "## Logros", *(f"- {x['line']}" for x in wins or [{"line": "Sin métricas por encima del objetivo."}]),
                    "## Riesgos", *(f"- {x['line']}" for x in risks or [{"line": "Sin riesgos detectados."}]),
                    "## Próximas acciones", *(f"- {x['action']}" for x in risks or wins)]
        return "\n\n".join(sections[:1]) + "\n\n" + "\n".join(sections[1:])

    lines = [title, "", "LOGROS"]
    lines += [f"- {x['line']}" for x in wins] or ["- Sin métricas por encima del objetivo."]
    lines += ["", "RIESGOS"]
    lines += [f"- {x['line']}" for x in risks] or ["- Sin riesgos detectados."]
    lines += ["", "PRÓXIMAS ACCIONES"]
    lines += [f"- {x['action']}" for x in risks or wins]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convierte métricas JSON en un brief ejecutivo.")
    parser.add_argument("input", type=Path, help="Archivo JSON con métricas")
    parser.add_argument("--format", choices=("text", "markdown"), default="text")
    parser.add_argument("--output", type=Path, help="Archivo de salida opcional")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    result = render(data, markdown=args.format == "markdown")
    if args.output:
        args.output.write_text(result + "\n", encoding="utf-8")
        print(f"Informe guardado en {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
