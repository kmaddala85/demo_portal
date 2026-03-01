import os, yaml


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def yaml_raw(path_yaml):
    # fetching KPIs for plots from yaml based on choosen category
    with open(os.path.join(BASE_DIR, path_yaml)) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
    return data
