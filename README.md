# Briefsmith

> Turn campaign metrics into a concise, explainable executive brief.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Español

**Briefsmith** es una herramienta local, sin dependencias, que convierte métricas de campaña en un resumen ejecutivo claro: qué está funcionando, qué necesita atención y qué acción tomar después.

### Por qué existe

Los dashboards enseñan números; las reuniones necesitan una historia. Briefsmith toma un JSON sencillo de métricas y redacta un informe accionable para compartir con marketing, producto o dirección.

### Funcionalidades

- Compara cada métrica con su objetivo y periodo anterior.
- Soporta métricas donde menos es mejor, como CAC o coste por lead.
- Agrupa hallazgos en logros, riesgos y próximas acciones.
- Genera una salida en texto o Markdown.
- Funciona completamente en local con la biblioteca estándar de Python.

### Inicio rápido

```bash
git clone https://github.com/alvaroalcalaa/briefsmith.git
cd briefsmith
python briefsmith.py examples/metrics.json
```

Para guardar un informe Markdown:

```bash
python briefsmith.py examples/metrics.json --format markdown --output weekly-brief.md
```

### Formato de entrada

```json
{
  "period": "Semana 45",
  "metrics": [
    {
      "name": "Leads cualificados",
      "value": 184,
      "target": 160,
      "previous": 142,
      "unit": ""
    }
  ]
}
```

Usa `"lower_is_better": true` para costes, errores o tiempos de respuesta.

### Estructura

```text
briefsmith/
├── briefsmith.py
├── examples/
│   └── metrics.json
├── tests.py
├── README.md
└── LICENSE
```

## English

**Briefsmith** is a dependency-free local CLI that turns campaign metrics into a clear executive brief: what is working, what needs attention, and what to do next.

### Features

- Compares every metric against its target and previous period.
- Supports lower-is-better metrics such as CAC and cost per lead.
- Separates findings into wins, risks, and suggested next actions.
- Renders plain text or Markdown.
- Uses only the Python standard library.

### Quick start

```bash
git clone https://github.com/alvaroalcalaa/briefsmith.git
cd briefsmith
python briefsmith.py examples/metrics.json --format markdown
```

### Demo output

```text
BRIEF · Semana 45
Wins
- Leads cualificados: 184 (+29.6% vs. prior period), above target by 15.0%.
Risks
- CTR: 1.70% (-15.0% vs. prior period), below target by 22.7%.
Next actions
- Review creative and audience targeting for CTR.
```

## License

MIT — see [LICENSE](LICENSE).
