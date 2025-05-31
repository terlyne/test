import pytest
from src.report_generator import generate_payout_report

def test_generate_payout_report_basic():
    test_data = [
        {"name": "John Doe", "department": "IT", "hours_worked": "40", "hourly_rate": "50"},
        {"name": "Jane Smith", "department": "HR", "hours_worked": "35", "rate": "45"},
        {"name": "Bob Johnson", "department": "IT", "hours_worked": "30", "salary": "60"}
    ]
    
    result = generate_payout_report(test_data)
    
    assert "IT" in result
    assert "HR" in result
    assert len(result["IT"]["employees"]) == 2
    assert result["IT"]["total_hours"] == 70
    assert result["HR"]["total_payout"] == 35 * 45

def test_generate_payout_report_empty_data():
    test_data = []
    result = generate_payout_report(test_data)
    assert result == {}

def test_generate_payout_report_missing_rate():
    test_data = [
        {"name": "John Doe", "department": "IT", "hours_worked": "40"}
    ]
    
    with pytest.raises(ValueError, match="Не указана почасовая ставка"):
        generate_payout_report(test_data)