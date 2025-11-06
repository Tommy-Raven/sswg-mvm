# Plugin Development Guide

Plugins allow developers to extend the system without altering core files.

## Plugin Structure

```python
# Example: custom_plugin.py
from generator.plugin_loader import register_plugin

@register_plugin(name="CustomMetric")
def custom_quality_metric(workflow):
    return {"custom_score": 9.5}

How to Load


# config/settings.yml
plugins:
  - custom_plugin

