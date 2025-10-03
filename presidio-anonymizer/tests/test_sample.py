import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # Run the anonymizer on the sample text
    result = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Check that the anonymized text is correct
    assert result.text == "My name is BIP."

    # Extract the first anonymizer operator result
    item = result.items[0]

    # Expected values for the item's attributes
    expected = {
        "start": 11,
        "end": 15,
        "length": 4,
        "entity_type": "PERSON",
        "text": "BIP",
        "operator": "replace"
    }

    # Loop through each expected attribute and assert it matches
    for attr, value in expected.items():
        assert getattr(item, attr) == value
