import yaml
from pathlib import Path


def load_topics():
    config_path = Path("config/topics.yaml")

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
