import yaml


def load_yaml(filename):
    """Load a YAML file and return its contents."""
    data = {}
    with open(filename) as file:
        for key, value in yaml.load(file).iteritems():
            print(f" {key=} , {value=}")
            if data.get(key) is not None:
                raise ValueError(f"Duplicate key found: {key}")
            data[key] = value
    return data
