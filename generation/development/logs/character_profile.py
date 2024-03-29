from typing import List, Dict, Optional

import yaml
from pydantic import BaseModel, validator
from pydantic import Field


# Define Pydantic models for structured data validation
class Skill(BaseModel):
    name: str
    level: int


class Attributes(BaseModel):
    body: int = Field(ge=0)
    agility: int = Field(ge=0)
    reaction: int = Field(ge=0)
    strength: int = Field(ge=0)
    willpower: int = Field(ge=0)
    logic: int = Field(ge=0)
    intuition: int = Field(ge=0)
    charisma: int = Field(ge=0)


class CharacterProfileModel(BaseModel):
    name: str
    metatype: str
    level: int = Field(ge=0)
    priorities: Dict[str, str]
    karma: Dict[str, Optional[int]]
    resources: Dict[str, Optional[int]]
    attributes: Attributes
    skills: Optional[List[Skill]] = []
    spells_known: Optional[Dict[str, Dict[str, bool]]] = []
    equipment: Dict[str, Dict]

    @validator('skills', each_item=True)
    def check_skill_names(cls, v):
        if not v.name:
            raise ValueError('Skill name cannot be empty')
        return v


# CharacterProfile class for handling character data
class CharacterProfile:
    def __init__(self, file_path='character_profile.yaml'):
        self.file_path = file_path
        self._last_mod_time = None
        self.character_data = None

    def load_character_data(self):
        # Existing logic...
        with open(self.file_path, 'r') as file:
            data = yaml.safe_load(file)
            self.character_data = CharacterProfileModel(**data)  # Convert to Pydantic model

    def get_attribute(self, attribute_path: str):
        """Retrieve a character attribute using a dot-separated path."""
        self.load_character_data()  # Ensure data is loaded
        try:
            attributes = attribute_path.split('.')
            data = self.character_data.dict()
            for attr in attributes:
                data = data[attr]
            return data
        except KeyError:
            print(f"Attribute path '{attribute_path}' not found.")
            return None

    def update_attribute(self, attribute_path: str, value):
        """Update a character attribute based on a dot-separated path."""
        try:
            attributes = attribute_path.split('.')
            data = self.character_data.dict()
            for attr in attributes[:-1]:
                data = data[attr]
            data[attributes[-1]] = value
            self.character_data = CharacterProfileModel(**data)
            return True
        except KeyError:
            print(f"Attribute path '{attribute_path}' not found.")
            return False

    def save_character_data(self):
        """Save the current state of character data back to the YAML file."""
        try:
            with open(self.file_path, 'w') as file:
                yaml.dump(self.character_data.dict(), file, default_flow_style=False, allow_unicode=True)
        except Exception as e:
            print(f"Error saving character data: {e}")


# Example usage:
if __name__ == "__main__":
    profile = CharacterProfile('character_profile.yaml')

    # Access specific attributes
    print(profile.get_attribute('attributes.physical.body'))

    # Update an attribute and save
    if profile.update_attribute('attributes.physical.body', 5):
        print("Attribute updated successfully.")
        profile.save_character_data()
