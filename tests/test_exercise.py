import pytest
import os
from src.exercise import read_records_from_file

def test_exercise(capsys):
    os.chdir('src')
     #had to change this import
    file = "data.txt"
    records = read_records_from_file(file)
    assert records == ["lily","anton","levi","amy"]
