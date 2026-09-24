from learning_sprint_planner_agent import application


class FakeChain:
    def invoke(self, input_data):
        assert input_data == {
            "topic": "Python generators",
            "level": "Beginner",
        }

        return "A generator produces values one at a time."


def test_run_explain_returns_chain_output(monkeypatch):
    fake_chain = FakeChain()

    monkeypatch.setattr(
        application,
        "explain_chain",
        fake_chain,
    )

    result = application.run_explain(
        "Python generators",
        "Beginner",
    )

    assert result == "A generator produces values one at a time."