import os
import yaml

def load_config():
    base_dir = os.path.dirname(__file__)  # путь к текущему файлу (app/)
    path = os.path.join(base_dir, "config.yaml")
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config
