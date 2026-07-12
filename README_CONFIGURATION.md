# GMIA Configuration

## Disease Priority

Edit:

config/topics.yaml

This file controls:

- Disease priority
- English keywords
- Mandarin keywords

---

## Search Strategy

Edit:

config/search_config.yaml

This file controls:

- Search period (days)
- Maximum search results
- Source-specific configuration

---

## AI Behaviour

Edit:

ai/prompt.py

This file controls:

- Executive Summary style
- Top Intelligence selection
- Medical Advisor role
- Prioritization logic

---

## Daily Workflow

GitHub Actions

.github/workflows/python.yml

Runs automatically every day according to the configured schedule.
