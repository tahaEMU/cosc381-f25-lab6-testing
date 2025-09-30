from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def run_anonymizer(text: str, start: int, end: int, replacement: str = "BIP"):
    """
    Testable wrapper around AnonymizerEngine.anonymize.
    Returns the engine result object so tests can assert fields.
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


def sample_run_anonymizer():
    """Keeps the original sample scenario but without input(), for demo/manual run."""
    return run_anonymizer("My name is Bond.", 11, 15, "BIP")


if __name__ == "__main__":
    res = sample_run_anonymizer()
    print(res)