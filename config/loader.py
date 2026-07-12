import yaml


def load_topics():

    with open(
        "config/topics.yaml",
        "r",
        encoding="utf-8"
    ) as f:

        config = yaml.safe_load(f)

    return config
