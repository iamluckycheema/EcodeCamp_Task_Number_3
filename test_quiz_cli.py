# test_quiz_cli.py
from quiz import play_quiz

def test_correct_answers(monkeypatch, capsys):
    # Simulate correct answers
    inputs = iter(['B', 'C', 'B'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the quiz function (assuming play_quiz uses internal questions, no arguments needed)
    play_quiz()

    # Capture the output
    captured = capsys.readouterr()
    assert 'Quiz finished! Your score is 3/3.' in captured.out

def test_incorrect_answers(monkeypatch, capsys):
    # Simulate incorrect answers
    inputs = iter(['A', 'A', 'A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the quiz function
    play_quiz()

    # Capture the output
    captured = capsys.readouterr()
    assert 'Quiz finished! Your score is 0/3.' in captured.out
