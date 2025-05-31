def generate_payout_report(data: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    """Функция для генерации отчета по зарплате сотрудников."""
    report = {}
    
    for entry in data:
        department = entry["department"]
        hours_worked = int(entry["hours_worked"])
        
        if "hourly_rate" in entry:
            hourly_rate = float(entry["hourly_rate"])
        elif "rate" in entry:
            hourly_rate = float(entry["rate"])
        elif "salary" in entry:
            hourly_rate = float(entry["salary"])
        else:
            raise ValueError("Не указана почасовая ставка для сотрудника.")
        
        payout = hours_worked * hourly_rate
        
        if department not in report:
            report[department] = {
                "employees": [],
                "total_hours": 0,
                "total_payout": 0.0
            }
        
        report[department]["employees"].append({
            "name": entry["name"],
            "hours": hours_worked,
            "rate": hourly_rate,
            "payout": payout
        })
        
        report[department]["total_hours"] += hours_worked
        report[department]["total_payout"] += payout
    
    return report
