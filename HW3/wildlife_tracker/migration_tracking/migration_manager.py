from typing import Optional

from wildlife_tracker.migration_management.migration import Migration
from wildlife_tracker.migration_management.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationManager:

    def __init__(self):
        self.migrations: dict[int, 'Migration'] = {}
        self.paths: dict[int, 'MigrationPath'] = {}

    def get_migrations_by_current_location(current_location: str) -> List['Migration']:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> List['Migration']:
        pass

    def get_migrations_by_start_date(start_date: str) -> List['Migration']:
        pass

    def get_migrations_by_status(status: str) -> List['Migration']:
        pass

    def schedule_migration(migration_path: 'MigrationPath') -> None:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

    def get_migrations() -> List['Migration']:
        pass
