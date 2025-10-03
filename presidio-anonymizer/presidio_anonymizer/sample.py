from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Run the anonymizer
    result = engine.anonymize(
        text=text,
        analyzer_results=[RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}
    )

    # Return the full result so tests can check start/end/length/items
    return result

if __name__ == "__main__": 
    res = sample_run_anonymizer("My name is Bond.", 11, 15)
    print(res)
