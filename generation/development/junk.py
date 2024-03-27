from information import attributes, attributes_upgradable, skills
import json
combined_attributes = {}
for attr_dict in (attributes, attributes_upgradable):
    for category, attrs in attr_dict.items():
        if category not in combined_attributes:
            combined_attributes[category] = list(set(attrs))
        else:
            combined_attributes[category] += list(set(attrs) - set(combined_attributes[category]))

combined_skills = {
    **skills,
}

combined_dict = {
    "Attributes": combined_attributes,
    "Skills": combined_skills
}
with open('combined.py', 'w') as file:
    file.write("combined_dict = ")
    json.dump(combined_dict, file, indent=4)

print(json.dumps(combined_dict, indent=4))
