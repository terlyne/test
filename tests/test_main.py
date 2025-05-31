import pytest
import subprocess
import json
import os

def test_main_integration(tmp_path):
    csv1 = tmp_path / "file1.csv"
    csv1.write_text("name,department,hours_worked,rate\nJohn,IT,40,50")
    
    csv2 = tmp_path / "file2.csv"
    csv2.write_text("name,department,hours_worked,rate\nJane,HR,35,45")
    
    output_file = tmp_path / "output.json"
    
    cmd = f"python src/main.py {csv1} {csv2} --report payout --out {output_file}"
    subprocess.run(cmd, shell=True, check=True)
    
    assert os.path.exists(output_file)
    with open(output_file) as f:
        data = json.load(f)
    
    assert len(data) == 2
    assert "IT" in data
    assert "HR" in data
    assert data["IT"]["total_payout"] == 2000
    assert data["HR"]["total_payout"] == 1575