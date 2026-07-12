import yaml


def load_topics():

    with open(
        "config/topics.yaml",
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)


def load_search_config():

    with open(
        "config/search_config.yaml",
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)
