import yaml
from gear import *
yaml_conversion = yaml.dump(concealability, sort_keys=False)

with open('equipment_concealability.yaml', 'w') as file:
    file.write(yaml_conversion)