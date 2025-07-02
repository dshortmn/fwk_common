import yaml


def load_yaml(filename):
    """Load a YAML file and return its contents."""
    data = {}
    with open(filename, "r") as file:
        data = yaml.load(file, yaml.SafeLoader)
        if not isinstance(data, dict):
            raise ValueError(f"YAML file {filename} does not contain a dictionary")
        if not data:
            raise ValueError(f"YAML file {filename} is empty")
    if not data:
        raise ValueError(
            f"YAML file {filename} is empty or does not contain valid data"
        )
    return data
