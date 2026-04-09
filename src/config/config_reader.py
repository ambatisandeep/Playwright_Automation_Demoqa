import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.yaml"
ENV_CONFIG_PATH = Path(__file__).parent / "environments.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)  # Added the 'e' here

def load_env_config():
    with open(ENV_CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)  # Added the 'e' here
