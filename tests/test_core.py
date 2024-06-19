from rmq_message_pruner.cli import should_drop


def test_should_drop_any_case_sensitive():
    assert should_drop("alpha beta", ["beta"], "any", False) is True
    assert should_drop("alpha beta", ["gamma"], "any", False) is False


def test_should_drop_all():
    assert should_drop("alpha beta", ["alpha", "beta"], "all", False) is True
    assert should_drop("alpha beta", ["alpha", "gamma"], "all", False) is False


def test_should_drop_ignore_case():
    assert should_drop("Alpha", ["alpha"], "any", True) is True
