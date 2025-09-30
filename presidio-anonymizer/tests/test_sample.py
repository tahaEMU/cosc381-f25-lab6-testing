from presidio_anonymizer.sample import run_anonymizer

def test_run_anonymizer_replaces_person_name():
    res = run_anonymizer("My name is Bond.", 11, 15, "BIP")

    # text should be anonymized correctly
    assert res.text == "My name is BIP."

    # one replacement item
    assert len(res.items) == 1
    item = res.items[0]  # this is an OperatorResult-like object

    # verify fields via attributes (not dict subscripts)
    assert getattr(item, "entity_type", None) == "PERSON"
    assert getattr(item, "start", None) == 11
    assert getattr(item, "end", None) == 14  # exclusive end after "BIP"
    assert getattr(item, "text", None) == "BIP"
    assert getattr(item, "operator", None) == "replace"