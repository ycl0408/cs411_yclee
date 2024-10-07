from typing import Any, Optional

class Animal:

    def __init__(self, animal_id: int, species: str, age: Optional[int] = None, health_status: Optional[str] = None):
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status
    
    def get_animal_by_id(animal_id: int) -> Optional['Animal']:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def register_animal(animal: 'Animal') -> None:
        pass

    def remove_animal(animal_id: int) -> None:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

