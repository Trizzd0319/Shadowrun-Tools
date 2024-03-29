import yaml

from char_data import *

yaml_conversion = yaml.dump(character_data, sort_keys=False)

with open('character_profile.yaml', 'w') as file:
    file.write(yaml_conversion)