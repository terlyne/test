import json
import os
from src.output_formatter import to_json, to_standard_output

def test_to_json(tmp_path):
    test_report = {"IT": {"employees": [], "total_hours": 0, "total_payout": 0}}
    test_file = tmp_path / "output.json"
    
    to_json(test_report, str(test_file))
    
    assert os.path.exists(test_file)
    with open(test_file) as f:
        content = json.load(f)
    assert content == test_report

def test_to_standard_output(capsys):
    test_report = {
        "IT": {
            "employees": [{"name": "John", "hours": 40, "rate": 50, "payout": 2000}],
            "total_hours": 40,
            "total_payout": 2000
        }
    }
    
    expected_output = """IT
---------
          Name                        Hours  Rate     Payout     

          John                        40     50       $2,000.00
          Total                       40              $2,000.00

"""
    
    to_standard_output(test_report)
    captured = capsys.readouterr()
    assert captured.out.replace(' ', '') == expected_output.replace(' ', '')