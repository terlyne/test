import json
import os

def to_json(report: list[dict[str, str]], file_path: str) -> None:
    """Функция для сохранения ответа в JSON файле."""
    try:
        json_data = json.dumps(report, indent=4)
        
        # Открываем файл для записи отчета (если файла не существует, то он будет создан)
        with open(file_path, "w") as f:
            f.write(json_data)
    
    except Exception as e:
        print(f"Произошла ошибка при сохранении данных в файл {file_path}: {e}")
        os._exit(1)


def to_standard_output(report: dict[str, dict]) -> None:
    for department, details in report.items():
        print(department)
        print(f"---------")
        print(f"{' ' * 9}  {'Name': <30} {'Hours': <7} {'Rate': <8} {'Payout': <12}\n")
        
        for employee in details["employees"]:
            print(f"{' ' * 9}  {employee['name']: <30} {employee['hours']: <7} {employee['rate']: <8} ${employee['payout']:,.2f}")
        
        print(f"{' ' * 9}  {'Total': <30} {details['total_hours']: <7} {'': <8} ${details['total_payout']:,.2f}\n")