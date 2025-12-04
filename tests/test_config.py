"""
Tests configuration loading + template resolution.
"""

from data.data_parsing import load_template


def test_load_template_by_slug(template_dir):
    data = load_template("creative")
    assert isinstance(data, dict)
    assert "phases" in data
