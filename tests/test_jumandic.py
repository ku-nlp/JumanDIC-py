from jumandic import JumanDIC


def test_init():
    _ = JumanDIC()


def test_ContentW():
    jumandic = JumanDIC()
    assert len(jumandic.dic.ContentW) == 31952
