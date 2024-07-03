import ruamel.yaml


yaml = ruamel.yaml.YAML(typ='rt')

with open('robot.yaml', 'r') as file:
    robotConfig = yaml.load(file)
