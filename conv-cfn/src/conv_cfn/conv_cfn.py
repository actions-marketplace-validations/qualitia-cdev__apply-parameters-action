import os
import yaml
from envyaml import EnvYAML
from typing import Dict, Any


def set_yaml_to_env(path: str):
    env = EnvYAML(path)

    for key in env.keys():
        if key not in os.environ:
            os.environ[key] = str(env[key])


def convert(path: str) -> Dict[str, str]:
    with open(path) as f:
        return os.path.expandvars(f.read())
