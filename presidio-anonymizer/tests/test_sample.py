import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    result = sample_run_anonymizer(text)

    # Check anonymized text
    assert "Bond" not in result.text
    assert result.text == "My name is BIP."

    # Extract the first entity
    item = result.entities[0]

    # Verify its fields
    assert item.start == 11
    assert item.end == 15
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"

    pass