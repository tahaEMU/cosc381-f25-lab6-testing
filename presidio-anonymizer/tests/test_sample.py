from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")

    # check text replacement
    assert res.text == "My name is BIP."

    # one item only
    assert len(res.items) == 1
    item = res.items[0]

    # check anonymization fields
    assert getattr(item, "start", None) == 11
    assert getattr(item, "end", None) == 14