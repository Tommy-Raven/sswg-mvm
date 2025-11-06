# Schema Tracking & Version Control

Ensures all workflow templates remain consistent across updates.

## Core Modules
- `ai_validation/schema_tracker.py`
- `ai_validation/version_migrator.py`

## Schema Fields
```yaml
schema:
  version: 1.0
  last_migration: "2025-11-03"
  compatible_versions: [0.9, 1.0]

Automatic Migration
from ai_validation.version_migrator import SchemaMigrator
SchemaMigrator().upgrade_schema("workflow_001.json")

