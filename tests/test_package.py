import re


def test_hyogu_has_version() -> None:
    import hyogu

    assert hasattr(hyogu, "__version__")
    assert isinstance(hyogu.__version__, str)
    assert re.match(r"\d+\.\d+\.\d+", hyogu.__version__)
