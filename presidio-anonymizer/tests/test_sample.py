import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # Input text
    input_text = "My name is Bond, James Bond"

    # Run the anonymizer
    # The numbers 11, 15 correspond to the start and end indices of "Bond" in the text
    result = sample_run_anonymizer(input_text, 11, 15)

    # Expected anonymized text (replace "Bond" with "BIP")
    expected_text = "My name is BIP, James Bond"
    
    #  Check the full text
    assert result.text == expected_text

    #  Check length matches input
    assert len(result.text) == len(input_text)

    #  Check the anonymized entity info
    item = result.items[0]
    assert item.start == 11        # start index of "Bond"
    assert item.end == 14          # end index of "Bond" (Python-style, exclusive)
    assert item.entity_type == "PERSON"
    assert item.operator == "replace"
    assert item.text == "BIP"
