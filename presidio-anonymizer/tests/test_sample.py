import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Check anonymized text
    assert result.text == "My name is BIP."

    # Extract the operator result object
    item = result.items[0]

    # Verify its fields
    assert item.start == 11                # start index of original entity
    assert item.end == 15                  # end index (exclusive)
    assert item.length == 4                # length of the original entity "Bond"
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
