from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text: str, start: int, end: int, replacement: str = "BIP"):
    """
    Anonymize PERSON entities in text.
    Refactored for testability: takes parameters instead of input(),
    and returns the result so tests can assert on it.
    """
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=int(start), end=int(end), score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": replacement})},
    )
    return result


if __name__ == "__main__":
    res = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")
    print(res)