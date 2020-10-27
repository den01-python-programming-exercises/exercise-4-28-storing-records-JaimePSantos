import pytest
import os

def test_exercise(capsys):
    # os.chdir('src')
    from src.exercise import read_records_from_file #had to change this import
    file = "src\data.txt"
    records = read_records_from_file(file)

    assert records == ["lily","anton","levi","amy"]
