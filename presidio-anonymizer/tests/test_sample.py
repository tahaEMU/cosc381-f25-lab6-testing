from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")

    # text is updated correctly
    assert res.text == "My name is BIP."

    # result should contain exactly one item
    assert len(res.items) == 1

    item = res.items[0]

    # check start and end
    assert item.start == 11
    assert item.end == 14