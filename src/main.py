import argparse

from csv_reader import read_csv
from report_generator import generate_payout_report
from output_formatter import to_json, to_standard_output


def main():
    parser = argparse.ArgumentParser(
        description="Подсчёт зарплаты сотрудников"
    )
    parser.add_argument("files", nargs="+", help="CSV-файлы для обработки")
    parser.add_argument("--report", required=True, help="Тип репорта")
    parser.add_argument("--out", help="Файл для сохранения отчета (если не указано, вывод в консоль)")


    args = parser.parse_args()
    
    data = []
    for file in args.files:
        data.extend(read_csv(file))

    if args.report == "payout":
        report = generate_payout_report(data)
        if args.out and args.out.endswith(".json"):
            to_json(report, args.out)
            print(f"Отчет сохранен в файл {args.out}.")
        else:
            to_standard_output(report)

    else:
        print("Неизвестный тип отчета.")

    


if __name__ == "__main__":
    main()