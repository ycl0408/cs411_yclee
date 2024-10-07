from typing import Optional, List

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:

    def __init__(self):
        self.habitats: dict[int, 'Habitat'] = {}

    def get_habitats_by_geographic_area(geographic_area: str) -> List['Habitat']:
        pass

    def get_habitats_by_size(size: int) -> List['Habitat']:
        pass

    def get_habitats_by_type(environment_type: str) -> List['Habitat']:
        pass

    def assign_animals_to_habitat(habitat_id: int, animals: List['Animal']) -> None:
        pass

    def remove_habitat(habitat_id: int) -> None:
        pass

    def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
        pass

    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> 'Habitat':
        pass
