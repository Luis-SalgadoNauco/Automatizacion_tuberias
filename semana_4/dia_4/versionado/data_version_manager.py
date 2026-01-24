from typing import Dict


class DataVersionManager:
    """Gestor simple de versionado de datos y esquemas"""

    def __init__(self):
        self.schemas = self._load_schemas()

    def _load_schemas(self) -> Dict:
        """Definición de esquemas por versión"""
        return {
            1: {
                'fields': ['id', 'name', 'created_at']
            },
            2: {
                'fields': ['id', 'name', 'email', 'created_at', 'updated_at']
            },
            3: {
                'fields': ['id', 'name', 'email', 'phone', 'created_at', 'updated_at']
            }
        }

    def validate_schema(self, data: Dict, version: int = None) -> Dict:
        """Validar que los datos cumplan el esquema"""
        if version is None:
            version = data.get('schema_version', 1)

        if version not in self.schemas:
            return {'valid': False, 'errors': [f'Versión {version} no soportada']}

        required_fields = self.schemas[version]['fields']
        errors = []

        for field in required_fields:
            if field not in data:
                errors.append(f'Campo faltante: {field}')

        return {
            'valid': len(errors) == 0,
            'version': version,
            'errors': errors
        }

    def upgrade_data(self, data: Dict, target_version: int) -> Dict:
        """Actualizar datos a la versión objetivo"""
        current_version = data.get('schema_version', 1)

        while current_version < target_version:
            data = self._upgrade_one_version(data, current_version)
            current_version += 1
            data['schema_version'] = current_version

        return data

    def _upgrade_one_version(self, data: Dict, from_version: int) -> Dict:
        """Upgrade incremental de versión"""

        if from_version == 1:
            data['email'] = None
            data['updated_at'] = data.get('created_at')

        elif from_version == 2:
            data['phone'] = None

        return data


# ----------------------------
# Simulación ejecutable
# ----------------------------
if __name__ == "__main__":

    version_manager = DataVersionManager()

    legacy_data = {
        'id': '123',
        'name': 'Juan Pérez',
        'created_at': '2024-01-01T10:00:00'
    }

    print("\nValidando datos originales (v1)")
    validation = version_manager.validate_schema(legacy_data)
    print(validation)

    print("\nUpgradeando datos a versión 3")
    upgraded_data = version_manager.upgrade_data(legacy_data.copy(), 3)
    print(upgraded_data)

    print("\nValidando datos upgradeados (v3)")
    validation_upgraded = version_manager.validate_schema(upgraded_data)
    print(validation_upgraded)
