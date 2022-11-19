import kilosort


def test_version():
    assert len(kilosort.__version__.split(".")) == 3
