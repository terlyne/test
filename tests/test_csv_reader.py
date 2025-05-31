import pytest
from src.csv_reader import read_csv

def test_read_csv(tmp_path):
    # Создаем временный CSV файл
    test_file = tmp_path / "test.csv"
    test_file.write_text("name,department,hours_worked,rate\nJohn Doe,IT,40,50\nJane Smith,HR,35,45")
    
    expected = [
        {"name": "John Doe", "department": "IT", "hours_worked": "40", "rate": "50"},
        {"name": "Jane Smith", "department": "HR", "hours_worked": "35", "rate": "45"}
    ]
    
    result = read_csv(test_file)
    assert result == expected

def test_read_csv_empty_file(tmp_path):
    test_file = tmp_path / "empty.csv"
    test_file.write_text("name,department,hours_worked,rate\n")
    
    result = read_csv(test_file)
    assert result == []

def test_read_csv_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_csv("nonexistent_file.csv")